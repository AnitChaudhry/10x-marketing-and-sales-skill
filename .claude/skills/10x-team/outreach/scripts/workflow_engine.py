#!/usr/bin/env python3
"""
Workflow Engine for 100X Outreach System

Orchestrates multi-step, multi-platform outreach workflows.
Supports discovery → warm-up → engagement → outreach sequences
with intelligent rate limiting and progress tracking.
"""

import json
import yaml
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict, field
from enum import Enum
import uuid

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False


class WorkflowStatus(str, Enum):
    DRAFT = "draft"
    PENDING_APPROVAL = "pending_approval"
    APPROVED = "approved"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class PhaseStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    SKIPPED = "skipped"
    FAILED = "failed"


class ActionStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


@dataclass
class WorkflowAction:
    """A single action in a workflow phase"""
    id: str
    action_type: str  # view_profile, like_post, connect, message, follow, dm, etc.
    platform: str  # linkedin, twitter, instagram, gmail
    target_id: str  # Person ID from discovery
    target_info: Dict = field(default_factory=dict)  # Name, URL, etc.
    template: str = ""
    message: str = ""
    status: str = ActionStatus.PENDING.value
    scheduled_at: Optional[str] = None
    executed_at: Optional[str] = None
    result: Dict = field(default_factory=dict)
    error: str = ""
    retry_count: int = 0
    max_retries: int = 3


@dataclass
class WorkflowPhase:
    """A phase in the workflow containing multiple actions"""
    id: str
    name: str
    platform: str
    action_type: str
    template: str = ""
    delay_min_seconds: int = 120
    delay_max_seconds: int = 600
    condition: str = ""  # e.g., "has_twitter", "connection_accepted"
    status: str = PhaseStatus.PENDING.value
    actions: List[WorkflowAction] = field(default_factory=list)
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    stats: Dict = field(default_factory=lambda: {'completed': 0, 'failed': 0, 'skipped': 0})


@dataclass
class WorkflowTarget:
    """A target person in the workflow"""
    person_id: str
    name: str
    platforms: Dict[str, str] = field(default_factory=dict)  # platform -> profile URL/handle
    current_phase: int = 0
    status: str = "pending"  # pending, in_progress, completed, failed
    phase_statuses: Dict[str, str] = field(default_factory=dict)  # phase_id -> status


@dataclass
class Workflow:
    """A complete workflow definition and execution state"""
    id: str
    name: str
    description: str
    created_at: str
    created_by: str  # Team member ID
    status: str = WorkflowStatus.DRAFT.value

    # Discovery configuration
    discovery_query: str = ""
    discovery_source: str = "exa"  # exa, manual, sheet
    max_targets: int = 10

    # Phases
    phases: List[WorkflowPhase] = field(default_factory=list)

    # Targets
    targets: List[WorkflowTarget] = field(default_factory=list)

    # Schedule
    schedule_days: List[str] = field(default_factory=lambda: ["monday", "tuesday", "wednesday", "thursday", "friday"])
    schedule_hours: Dict[str, str] = field(default_factory=lambda: {"start": "09:00", "end": "17:00"})
    timezone: str = "UTC"

    # Execution state
    approved_at: Optional[str] = None
    approved_by: Optional[str] = None
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    paused_at: Optional[str] = None

    # Stats
    stats: Dict = field(default_factory=lambda: {
        'total_targets': 0,
        'completed_targets': 0,
        'failed_targets': 0,
        'total_actions': 0,
        'completed_actions': 0,
        'failed_actions': 0
    })


class WorkflowEngine:
    """
    Orchestrates workflow execution.

    Features:
    - Create workflows from YAML definitions
    - Execute multi-phase campaigns
    - Track progress and status
    - Handle rate limiting
    - Pause/resume workflows
    """

    def __init__(self, data_dir: str = "campaigns"):
        self.data_dir = Path(data_dir)
        self.active_dir = self.data_dir / "active"
        self.completed_dir = self.data_dir / "completed"
        self.logs_dir = self.data_dir / "logs"

        # Create directories
        self.active_dir.mkdir(parents=True, exist_ok=True)
        self.completed_dir.mkdir(parents=True, exist_ok=True)
        self.logs_dir.mkdir(parents=True, exist_ok=True)

        self._workflows: Dict[str, Workflow] = {}
        self._load_workflows()

    def _load_workflows(self):
        """Load all active workflows"""
        for wf_file in self.active_dir.glob("*.json"):
            try:
                with open(wf_file, 'r') as f:
                    data = json.load(f)
                    workflow = self._dict_to_workflow(data)
                    self._workflows[workflow.id] = workflow
            except Exception as e:
                print(f"Warning: Could not load workflow {wf_file}: {e}")

    def _save_workflow(self, workflow: Workflow):
        """Save workflow to disk"""
        data = self._workflow_to_dict(workflow)

        # Save to active or completed based on status
        if workflow.status in [WorkflowStatus.COMPLETED.value, WorkflowStatus.CANCELLED.value]:
            path = self.completed_dir / f"{workflow.id}.json"
        else:
            path = self.active_dir / f"{workflow.id}.json"

        with open(path, 'w') as f:
            json.dump(data, f, indent=2)

    def _workflow_to_dict(self, workflow: Workflow) -> Dict:
        """Convert workflow to dictionary for serialization"""
        return {
            'id': workflow.id,
            'name': workflow.name,
            'description': workflow.description,
            'created_at': workflow.created_at,
            'created_by': workflow.created_by,
            'status': workflow.status,
            'discovery_query': workflow.discovery_query,
            'discovery_source': workflow.discovery_source,
            'max_targets': workflow.max_targets,
            'phases': [
                {
                    **asdict(phase),
                    'actions': [asdict(a) for a in phase.actions]
                }
                for phase in workflow.phases
            ],
            'targets': [asdict(t) for t in workflow.targets],
            'schedule_days': workflow.schedule_days,
            'schedule_hours': workflow.schedule_hours,
            'timezone': workflow.timezone,
            'approved_at': workflow.approved_at,
            'approved_by': workflow.approved_by,
            'started_at': workflow.started_at,
            'completed_at': workflow.completed_at,
            'paused_at': workflow.paused_at,
            'stats': workflow.stats
        }

    def _dict_to_workflow(self, data: Dict) -> Workflow:
        """Convert dictionary to Workflow object"""
        phases = []
        for p in data.get('phases', []):
            actions = [WorkflowAction(**a) for a in p.get('actions', [])]
            phase = WorkflowPhase(
                id=p['id'],
                name=p['name'],
                platform=p['platform'],
                action_type=p['action_type'],
                template=p.get('template', ''),
                delay_min_seconds=p.get('delay_min_seconds', 120),
                delay_max_seconds=p.get('delay_max_seconds', 600),
                condition=p.get('condition', ''),
                status=p.get('status', PhaseStatus.PENDING.value),
                actions=actions,
                started_at=p.get('started_at'),
                completed_at=p.get('completed_at'),
                stats=p.get('stats', {'completed': 0, 'failed': 0, 'skipped': 0})
            )
            phases.append(phase)

        targets = [WorkflowTarget(**t) for t in data.get('targets', [])]

        return Workflow(
            id=data['id'],
            name=data['name'],
            description=data.get('description', ''),
            created_at=data['created_at'],
            created_by=data.get('created_by', 'default'),
            status=data.get('status', WorkflowStatus.DRAFT.value),
            discovery_query=data.get('discovery_query', ''),
            discovery_source=data.get('discovery_source', 'exa'),
            max_targets=data.get('max_targets', 10),
            phases=phases,
            targets=targets,
            schedule_days=data.get('schedule_days', ["monday", "tuesday", "wednesday", "thursday", "friday"]),
            schedule_hours=data.get('schedule_hours', {"start": "09:00", "end": "17:00"}),
            timezone=data.get('timezone', 'UTC'),
            approved_at=data.get('approved_at'),
            approved_by=data.get('approved_by'),
            started_at=data.get('started_at'),
            completed_at=data.get('completed_at'),
            paused_at=data.get('paused_at'),
            stats=data.get('stats', {})
        )

    def create_workflow(self, name: str, description: str, created_by: str,
                       discovery_query: str = "", max_targets: int = 10) -> Workflow:
        """Create a new workflow"""
        workflow = Workflow(
            id=str(uuid.uuid4())[:8],
            name=name,
            description=description,
            created_at=datetime.now().isoformat(),
            created_by=created_by,
            discovery_query=discovery_query,
            max_targets=max_targets
        )

        self._workflows[workflow.id] = workflow
        self._save_workflow(workflow)
        return workflow

    def load_from_yaml(self, yaml_path: str, created_by: str) -> Workflow:
        """Load workflow definition from YAML file"""
        with open(yaml_path, 'r') as f:
            config = yaml.safe_load(f)

        workflow = Workflow(
            id=str(uuid.uuid4())[:8],
            name=config.get('name', 'Unnamed Workflow'),
            description=config.get('description', ''),
            created_at=datetime.now().isoformat(),
            created_by=created_by,
            discovery_query=config.get('discovery', {}).get('query', ''),
            discovery_source=config.get('discovery', {}).get('source', 'exa'),
            max_targets=config.get('discovery', {}).get('max_results', 10),
            schedule_days=config.get('schedule', {}).get('days', ["monday", "tuesday", "wednesday", "thursday", "friday"]),
            schedule_hours={
                'start': config.get('schedule', {}).get('hours', {}).get('start', '09:00'),
                'end': config.get('schedule', {}).get('hours', {}).get('end', '17:00')
            },
            timezone=config.get('schedule', {}).get('timezone', 'UTC')
        )

        # Parse phases
        for i, phase_config in enumerate(config.get('phases', [])):
            phase = WorkflowPhase(
                id=str(uuid.uuid4())[:8],
                name=phase_config.get('name', f'Phase {i+1}'),
                platform=phase_config.get('platform', 'linkedin'),
                action_type=phase_config.get('action', 'view_profile'),
                template=phase_config.get('template', ''),
                delay_min_seconds=self._parse_delay(phase_config.get('delay_after', '2 minutes'), 'min'),
                delay_max_seconds=self._parse_delay(phase_config.get('delay_after', '5 minutes'), 'max'),
                condition=phase_config.get('condition', '')
            )
            workflow.phases.append(phase)

        self._workflows[workflow.id] = workflow
        self._save_workflow(workflow)
        return workflow

    def _parse_delay(self, delay_str: str, mode: str = 'min') -> int:
        """Parse delay string like '2-5 minutes' or '1-3 hours'"""
        if isinstance(delay_str, int):
            return delay_str

        import re
        # Match patterns like "2-5 minutes", "1-3 hours", "30 seconds"
        match = re.match(r'(\d+)(?:-(\d+))?\s*(second|minute|hour)s?', str(delay_str), re.I)

        if not match:
            return 120 if mode == 'min' else 300

        min_val = int(match.group(1))
        max_val = int(match.group(2)) if match.group(2) else min_val
        unit = match.group(3).lower()

        multiplier = {'second': 1, 'minute': 60, 'hour': 3600}.get(unit, 60)

        if mode == 'min':
            return min_val * multiplier
        else:
            return max_val * multiplier

    def add_phase(self, workflow_id: str, name: str, platform: str, action_type: str,
                 template: str = "", delay_min: int = 120, delay_max: int = 600,
                 condition: str = "") -> Optional[WorkflowPhase]:
        """Add a phase to a workflow"""
        workflow = self._workflows.get(workflow_id)
        if not workflow:
            return None

        phase = WorkflowPhase(
            id=str(uuid.uuid4())[:8],
            name=name,
            platform=platform,
            action_type=action_type,
            template=template,
            delay_min_seconds=delay_min,
            delay_max_seconds=delay_max,
            condition=condition
        )

        workflow.phases.append(phase)
        self._save_workflow(workflow)
        return phase

    def add_targets(self, workflow_id: str, targets: List[Dict]) -> int:
        """Add targets to a workflow from discovery results"""
        workflow = self._workflows.get(workflow_id)
        if not workflow:
            return 0

        added = 0
        for target_data in targets:
            target = WorkflowTarget(
                person_id=target_data.get('id', str(uuid.uuid4())[:8]),
                name=target_data.get('name', ''),
                platforms={
                    'linkedin': target_data.get('linkedin_url', ''),
                    'twitter': target_data.get('twitter_handle', ''),
                    'instagram': target_data.get('instagram_handle', ''),
                    'email': target_data.get('email', '')
                }
            )
            workflow.targets.append(target)
            added += 1

        workflow.stats['total_targets'] = len(workflow.targets)
        self._save_workflow(workflow)
        return added

    def get_workflow(self, workflow_id: str) -> Optional[Workflow]:
        """Get a workflow by ID"""
        return self._workflows.get(workflow_id)

    def list_workflows(self, status: str = None) -> List[Workflow]:
        """List all workflows, optionally filtered by status"""
        workflows = list(self._workflows.values())
        if status:
            workflows = [w for w in workflows if w.status == status]
        return sorted(workflows, key=lambda w: w.created_at, reverse=True)

    def submit_for_approval(self, workflow_id: str) -> bool:
        """Submit workflow for user approval"""
        workflow = self._workflows.get(workflow_id)
        if not workflow:
            return False

        if workflow.status != WorkflowStatus.DRAFT.value:
            return False

        workflow.status = WorkflowStatus.PENDING_APPROVAL.value
        self._save_workflow(workflow)
        return True

    def approve_workflow(self, workflow_id: str, approved_by: str) -> bool:
        """Approve a workflow for execution"""
        workflow = self._workflows.get(workflow_id)
        if not workflow:
            return False

        if workflow.status != WorkflowStatus.PENDING_APPROVAL.value:
            return False

        workflow.status = WorkflowStatus.APPROVED.value
        workflow.approved_at = datetime.now().isoformat()
        workflow.approved_by = approved_by
        self._save_workflow(workflow)
        return True

    def start_workflow(self, workflow_id: str) -> bool:
        """Start executing a workflow"""
        workflow = self._workflows.get(workflow_id)
        if not workflow:
            return False

        if workflow.status not in [WorkflowStatus.APPROVED.value, WorkflowStatus.PAUSED.value]:
            return False

        workflow.status = WorkflowStatus.RUNNING.value
        workflow.started_at = workflow.started_at or datetime.now().isoformat()
        workflow.paused_at = None

        # Initialize actions for first phase if not done
        if workflow.phases and not workflow.phases[0].actions:
            self._generate_phase_actions(workflow, workflow.phases[0])

        self._save_workflow(workflow)
        return True

    def pause_workflow(self, workflow_id: str) -> bool:
        """Pause a running workflow"""
        workflow = self._workflows.get(workflow_id)
        if not workflow or workflow.status != WorkflowStatus.RUNNING.value:
            return False

        workflow.status = WorkflowStatus.PAUSED.value
        workflow.paused_at = datetime.now().isoformat()
        self._save_workflow(workflow)
        return True

    def cancel_workflow(self, workflow_id: str) -> bool:
        """Cancel a workflow"""
        workflow = self._workflows.get(workflow_id)
        if not workflow:
            return False

        workflow.status = WorkflowStatus.CANCELLED.value
        workflow.completed_at = datetime.now().isoformat()
        self._save_workflow(workflow)
        return True

    def _generate_phase_actions(self, workflow: Workflow, phase: WorkflowPhase):
        """Generate actions for a phase based on targets"""
        for target in workflow.targets:
            # Check condition
            if phase.condition:
                if not self._check_condition(phase.condition, target):
                    continue

            # Check if platform is available for target
            platform_url = target.platforms.get(phase.platform, '')
            if not platform_url and phase.platform != 'gmail':
                continue

            action = WorkflowAction(
                id=str(uuid.uuid4())[:8],
                action_type=phase.action_type,
                platform=phase.platform,
                target_id=target.person_id,
                target_info={
                    'name': target.name,
                    'url': platform_url
                },
                template=phase.template
            )
            phase.actions.append(action)

        workflow.stats['total_actions'] = sum(len(p.actions) for p in workflow.phases)

    def _check_condition(self, condition: str, target: WorkflowTarget) -> bool:
        """Check if a condition is met for a target"""
        conditions = {
            'has_linkedin': bool(target.platforms.get('linkedin')),
            'has_twitter': bool(target.platforms.get('twitter')),
            'has_instagram': bool(target.platforms.get('instagram')),
            'has_email': bool(target.platforms.get('email')),
            'has_recent_posts': True,  # Assume true, would need external check
            'connection_accepted': target.phase_statuses.get('connect') == 'completed'
        }
        return conditions.get(condition, True)

    def get_next_action(self, workflow_id: str) -> Optional[WorkflowAction]:
        """Get the next action to execute"""
        workflow = self._workflows.get(workflow_id)
        if not workflow or workflow.status != WorkflowStatus.RUNNING.value:
            return None

        for phase in workflow.phases:
            if phase.status == PhaseStatus.COMPLETED.value:
                continue

            if phase.status == PhaseStatus.PENDING.value:
                phase.status = PhaseStatus.IN_PROGRESS.value
                phase.started_at = datetime.now().isoformat()

                if not phase.actions:
                    self._generate_phase_actions(workflow, phase)

            for action in phase.actions:
                if action.status == ActionStatus.PENDING.value:
                    return action

            # Phase complete
            phase.status = PhaseStatus.COMPLETED.value
            phase.completed_at = datetime.now().isoformat()

        # All phases complete
        workflow.status = WorkflowStatus.COMPLETED.value
        workflow.completed_at = datetime.now().isoformat()
        self._save_workflow(workflow)
        return None

    def record_action_result(self, workflow_id: str, action_id: str,
                            success: bool, result: Dict = None, error: str = None):
        """Record the result of an action execution"""
        workflow = self._workflows.get(workflow_id)
        if not workflow:
            return

        for phase in workflow.phases:
            for action in phase.actions:
                if action.id == action_id:
                    action.status = ActionStatus.COMPLETED.value if success else ActionStatus.FAILED.value
                    action.executed_at = datetime.now().isoformat()
                    action.result = result or {}
                    action.error = error or ""

                    if success:
                        phase.stats['completed'] += 1
                        workflow.stats['completed_actions'] += 1
                    else:
                        phase.stats['failed'] += 1
                        workflow.stats['failed_actions'] += 1

                    self._save_workflow(workflow)
                    return

    def get_workflow_summary(self, workflow_id: str) -> Dict:
        """Get a summary of workflow status for approval display"""
        workflow = self._workflows.get(workflow_id)
        if not workflow:
            return {}

        return {
            'id': workflow.id,
            'name': workflow.name,
            'description': workflow.description,
            'status': workflow.status,
            'discovery': {
                'query': workflow.discovery_query,
                'source': workflow.discovery_source,
                'max_targets': workflow.max_targets
            },
            'targets': {
                'total': len(workflow.targets),
                'sample': [{'name': t.name, 'platforms': list(k for k, v in t.platforms.items() if v)} for t in workflow.targets[:5]]
            },
            'phases': [
                {
                    'name': p.name,
                    'platform': p.platform,
                    'action': p.action_type,
                    'delay': f"{p.delay_min_seconds//60}-{p.delay_max_seconds//60} minutes"
                }
                for p in workflow.phases
            ],
            'schedule': {
                'days': workflow.schedule_days,
                'hours': f"{workflow.schedule_hours['start']} - {workflow.schedule_hours['end']}",
                'timezone': workflow.timezone
            },
            'stats': workflow.stats,
            'estimated_duration': self._estimate_duration(workflow)
        }

    def _estimate_duration(self, workflow: Workflow) -> str:
        """Estimate workflow duration"""
        total_actions = len(workflow.targets) * len(workflow.phases)
        avg_delay = sum((p.delay_min_seconds + p.delay_max_seconds) / 2 for p in workflow.phases) / max(len(workflow.phases), 1)
        total_seconds = total_actions * avg_delay

        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)

        if hours > 0:
            return f"~{hours}h {minutes}m"
        return f"~{minutes} minutes"


def main():
    """CLI interface for workflow engine"""
    import argparse

    parser = argparse.ArgumentParser(description="Workflow Engine CLI")
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Create workflow
    create_parser = subparsers.add_parser('create', help='Create workflow')
    create_parser.add_argument('--name', required=True, help='Workflow name')
    create_parser.add_argument('--description', default='', help='Description')
    create_parser.add_argument('--user', default='default', help='Creator user ID')
    create_parser.add_argument('--query', default='', help='Discovery query')

    # Load from YAML
    load_parser = subparsers.add_parser('load', help='Load from YAML')
    load_parser.add_argument('--file', required=True, help='YAML file path')
    load_parser.add_argument('--user', default='default', help='Creator user ID')

    # List workflows
    list_parser = subparsers.add_parser('list', help='List workflows')
    list_parser.add_argument('--status', help='Filter by status')

    # Get workflow
    get_parser = subparsers.add_parser('get', help='Get workflow details')
    get_parser.add_argument('--id', required=True, help='Workflow ID')

    # Approve workflow
    approve_parser = subparsers.add_parser('approve', help='Approve workflow')
    approve_parser.add_argument('--id', required=True, help='Workflow ID')
    approve_parser.add_argument('--user', default='default', help='Approver user ID')

    # Pause/cancel
    pause_parser = subparsers.add_parser('pause', help='Pause workflow')
    pause_parser.add_argument('--id', required=True, help='Workflow ID')

    cancel_parser = subparsers.add_parser('cancel', help='Cancel workflow')
    cancel_parser.add_argument('--id', required=True, help='Workflow ID')

    args = parser.parse_args()

    engine = WorkflowEngine()

    if args.command == 'create':
        workflow = engine.create_workflow(
            args.name,
            args.description,
            args.user,
            args.query
        )
        print(f"Created workflow: {workflow.id}")
        print(json.dumps(engine.get_workflow_summary(workflow.id), indent=2))

    elif args.command == 'load':
        workflow = engine.load_from_yaml(args.file, args.user)
        print(f"Loaded workflow: {workflow.id}")
        print(json.dumps(engine.get_workflow_summary(workflow.id), indent=2))

    elif args.command == 'list':
        workflows = engine.list_workflows(args.status)
        for w in workflows:
            print(f"{w.id}: {w.name} [{w.status}] - {len(w.targets)} targets, {len(w.phases)} phases")

    elif args.command == 'get':
        summary = engine.get_workflow_summary(args.id)
        print(json.dumps(summary, indent=2))

    elif args.command == 'approve':
        engine.submit_for_approval(args.id)
        if engine.approve_workflow(args.id, args.user):
            print(f"Workflow {args.id} approved")
        else:
            print("Failed to approve workflow")

    elif args.command == 'pause':
        if engine.pause_workflow(args.id):
            print(f"Workflow {args.id} paused")
        else:
            print("Failed to pause workflow")

    elif args.command == 'cancel':
        if engine.cancel_workflow(args.id):
            print(f"Workflow {args.id} cancelled")
        else:
            print("Failed to cancel workflow")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
