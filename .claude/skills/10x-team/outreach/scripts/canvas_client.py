#!/usr/bin/env python3
"""
Canvas Client - Control the 10x-Team Visual Workflow Canvas from Claude Code

This script allows Claude Code to programmatically create workflows
visually in the canvas web app in real-time.

Usage:
    # Check if canvas is running
    python canvas_client.py status

    # Create a workflow with nodes and connections
    python canvas_client.py workflow '{"nodes": [...], "connections": [...]}'

    # Add a single node
    python canvas_client.py add-node '{"skillType": "linkedin", "label": "Connect"}'

    # Clear the canvas
    python canvas_client.py clear
"""

import sys
import json
import urllib.request
import urllib.error
from typing import Optional, Dict, Any, List

CANVAS_URL = "http://localhost:3000"


def check_canvas_status() -> Dict[str, Any]:
    """Check if the canvas is running and accepting commands."""
    try:
        req = urllib.request.Request(f"{CANVAS_URL}/api/canvas/status")
        with urllib.request.urlopen(req, timeout=2) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        return {"running": False, "error": str(e)}


def send_command(command_type: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Send a single command to the canvas."""
    data = json.dumps({"type": command_type, "payload": payload}).encode()
    req = urllib.request.Request(
        f"{CANVAS_URL}/api/canvas/command",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            return json.loads(response.read().decode())
    except urllib.error.URLError as e:
        return {"success": False, "error": str(e)}


def create_workflow(workflow: Dict[str, Any]) -> Dict[str, Any]:
    """Create a complete workflow with nodes and connections."""
    data = json.dumps(workflow).encode()
    req = urllib.request.Request(
        f"{CANVAS_URL}/api/canvas/workflow",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode())
    except urllib.error.URLError as e:
        return {"success": False, "error": str(e)}


def clear_canvas() -> Dict[str, Any]:
    """Clear all nodes and connections from the canvas."""
    return send_command("clear", {})


def add_node(
    skill_type: str,
    label: str,
    description: str = "",
    x: Optional[int] = None,
    y: Optional[int] = None,
    node_id: Optional[str] = None,
    config: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Add a single node to the canvas."""
    payload = {
        "id": node_id or f"node-{label.lower().replace(' ', '-')}",
        "skillType": skill_type,
        "label": label,
        "description": description,
        "x": x or 200,
        "y": y or 200,
        "config": config or {}
    }
    return send_command("add-node", payload)


def add_connection(from_id: str, to_id: str) -> Dict[str, Any]:
    """Add a connection between two nodes."""
    payload = {
        "from": from_id,
        "to": to_id,
        "fromX": 440,  # Will be adjusted by canvas
        "fromY": 240,
        "toX": 200,
        "toY": 240
    }
    return send_command("add-connection", payload)


def create_b2b_workflow() -> Dict[str, Any]:
    """Create a sample B2B outreach workflow."""
    workflow = {
        "name": "B2B Professional Outreach",
        "nodes": [
            {"id": "discover", "skill": "discovery", "label": "Find Prospects", "description": "Search for AI founders"},
            {"id": "linkedin-view", "skill": "linkedin", "label": "View Profile", "description": "View their LinkedIn"},
            {"id": "linkedin-like", "skill": "linkedin", "label": "Like Post", "description": "Engage with content"},
            {"id": "delay-1", "skill": "delay", "label": "Wait 24h", "description": "Let them see the activity"},
            {"id": "linkedin-connect", "skill": "linkedin", "label": "Send Connection", "description": "Connection request"},
            {"id": "delay-2", "skill": "delay", "label": "Wait 48h", "description": "Wait for acceptance"},
            {"id": "linkedin-msg", "skill": "linkedin", "label": "Send Message", "description": "Introduction message"},
            {"id": "email", "skill": "email", "label": "Follow-up Email", "description": "Email if no response"},
        ],
        "connections": [
            {"from": "discover", "to": "linkedin-view"},
            {"from": "linkedin-view", "to": "linkedin-like"},
            {"from": "linkedin-like", "to": "delay-1"},
            {"from": "delay-1", "to": "linkedin-connect"},
            {"from": "linkedin-connect", "to": "delay-2"},
            {"from": "delay-2", "to": "linkedin-msg"},
            {"from": "linkedin-msg", "to": "email"},
        ]
    }
    return create_workflow(workflow)


def create_influencer_workflow() -> Dict[str, Any]:
    """Create a sample influencer outreach workflow."""
    workflow = {
        "name": "Influencer Outreach",
        "nodes": [
            {"id": "discover", "skill": "discovery", "label": "Find Influencers", "description": "Search for content creators"},
            {"id": "twitter-follow", "skill": "twitter", "label": "Follow on X", "description": "Follow their account"},
            {"id": "twitter-like", "skill": "twitter", "label": "Like Tweets", "description": "Engage with content"},
            {"id": "delay-1", "skill": "delay", "label": "Wait 24h", "description": "Build familiarity"},
            {"id": "twitter-reply", "skill": "twitter", "label": "Reply to Tweet", "description": "Add value to thread"},
            {"id": "delay-2", "skill": "delay", "label": "Wait 48h", "description": "Let them notice"},
            {"id": "instagram-follow", "skill": "instagram", "label": "Follow on IG", "description": "Cross-platform follow"},
            {"id": "instagram-dm", "skill": "instagram", "label": "Send DM", "description": "Pitch collaboration"},
        ],
        "connections": [
            {"from": "discover", "to": "twitter-follow"},
            {"from": "twitter-follow", "to": "twitter-like"},
            {"from": "twitter-like", "to": "delay-1"},
            {"from": "delay-1", "to": "twitter-reply"},
            {"from": "twitter-reply", "to": "delay-2"},
            {"from": "delay-2", "to": "instagram-follow"},
            {"from": "instagram-follow", "to": "instagram-dm"},
        ]
    }
    return create_workflow(workflow)


def create_custom_workflow(
    name: str,
    steps: List[Dict[str, str]],
    connect_sequential: bool = True
) -> Dict[str, Any]:
    """
    Create a custom workflow from a list of steps.

    Args:
        name: Workflow name
        steps: List of step dicts with 'skill', 'label', and optional 'description'
        connect_sequential: Whether to connect steps in order

    Example:
        create_custom_workflow("My Flow", [
            {"skill": "discovery", "label": "Find People"},
            {"skill": "linkedin", "label": "Connect"},
            {"skill": "email", "label": "Send Email"}
        ])
    """
    nodes = []
    connections = []

    for i, step in enumerate(steps):
        node_id = f"step-{i}"
        nodes.append({
            "id": node_id,
            "skill": step.get("skill", "discovery"),
            "label": step.get("label", f"Step {i+1}"),
            "description": step.get("description", ""),
        })

        if connect_sequential and i > 0:
            connections.append({
                "from": f"step-{i-1}",
                "to": node_id
            })

    return create_workflow({
        "name": name,
        "nodes": nodes,
        "connections": connections
    })


def main():
    if len(sys.argv) < 2:
        print("Usage: python canvas_client.py <command> [args]")
        print("\nCommands:")
        print("  status              - Check if canvas is running")
        print("  clear               - Clear the canvas")
        print("  workflow <json>     - Create a workflow from JSON")
        print("  add-node <json>     - Add a single node")
        print("  b2b                 - Create sample B2B workflow")
        print("  influencer          - Create sample influencer workflow")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "status":
        result = check_canvas_status()
        if result.get("running"):
            print(f"Canvas is running. Queue length: {result.get('queueLength', 0)}")
        else:
            print(f"Canvas is not running: {result.get('error', 'Unknown error')}")
            print("\nTo start the canvas:")
            print("  cd canvas && npm run dev -- --port 3000")

    elif command == "clear":
        result = clear_canvas()
        print(f"Clear canvas: {'Success' if result.get('success') else result.get('error')}")

    elif command == "workflow":
        if len(sys.argv) < 3:
            print("Usage: python canvas_client.py workflow '<json>'")
            sys.exit(1)
        try:
            workflow = json.loads(sys.argv[2])
            result = create_workflow(workflow)
            print(f"Workflow created: {result.get('nodesQueued', 0)} nodes, {result.get('connectionsQueued', 0)} connections")
        except json.JSONDecodeError as e:
            print(f"Invalid JSON: {e}")
            sys.exit(1)

    elif command == "add-node":
        if len(sys.argv) < 3:
            print("Usage: python canvas_client.py add-node '<json>'")
            sys.exit(1)
        try:
            node = json.loads(sys.argv[2])
            result = add_node(
                skill_type=node.get("skillType", "discovery"),
                label=node.get("label", "New Node"),
                description=node.get("description", ""),
                x=node.get("x"),
                y=node.get("y"),
                node_id=node.get("id"),
                config=node.get("config")
            )
            print(f"Node added: {'Success' if result.get('success') else result.get('error')}")
        except json.JSONDecodeError as e:
            print(f"Invalid JSON: {e}")
            sys.exit(1)

    elif command == "b2b":
        print("Creating B2B Professional Outreach workflow...")
        result = create_b2b_workflow()
        print(f"Created: {result.get('nodesQueued', 0)} nodes, {result.get('connectionsQueued', 0)} connections")
        print("Watch the canvas at http://localhost:3000")

    elif command == "influencer":
        print("Creating Influencer Outreach workflow...")
        result = create_influencer_workflow()
        print(f"Created: {result.get('nodesQueued', 0)} nodes, {result.get('connectionsQueued', 0)} connections")
        print("Watch the canvas at http://localhost:3000")

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
