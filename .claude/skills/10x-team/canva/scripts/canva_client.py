"""
Canva API Client
Core module for interacting with Canva Connect API
"""

import os
import json
import time
import logging
from typing import Optional, Dict, Any, List
from pathlib import Path

try:
    import requests
    from dotenv import load_dotenv
except ImportError:
    print("Required packages not installed. Run: pip install requests python-dotenv")
    raise

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=getattr(logging, os.getenv('LOG_LEVEL', 'INFO')),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('canva_client')


class CanvaClient:
    """Client for Canva Connect API"""

    BASE_URL = os.getenv('CANVA_API_BASE_URL', 'https://api.canva.com')

    def __init__(self, access_token: Optional[str] = None):
        """
        Initialize Canva client

        Args:
            access_token: OAuth access token (uses env var if not provided)
        """
        self.access_token = access_token or os.getenv('CANVA_ACCESS_TOKEN')
        self.client_id = os.getenv('CANVA_CLIENT_ID')
        self.client_secret = os.getenv('CANVA_CLIENT_SECRET')
        self.timeout = int(os.getenv('CANVA_API_TIMEOUT', '30'))
        self.rate_limit_delay = int(os.getenv('CANVA_RATE_LIMIT_DELAY', '100')) / 1000

        if not self.access_token:
            logger.warning("No access token configured. Run OAuth flow first.")

    @property
    def headers(self) -> Dict[str, str]:
        """Get request headers"""
        return {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json',
        }

    def _request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None,
        params: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Make API request

        Args:
            method: HTTP method (GET, POST, PATCH, DELETE)
            endpoint: API endpoint path
            data: Request body data
            params: Query parameters

        Returns:
            Response JSON data
        """
        url = f"{self.BASE_URL}{endpoint}"

        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=data,
                params=params,
                timeout=self.timeout
            )

            # Rate limiting
            time.sleep(self.rate_limit_delay)

            response.raise_for_status()

            if response.content:
                return response.json()
            return {}

        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP Error: {e}")
            logger.error(f"Response: {response.text}")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"Request Error: {e}")
            raise

    # ===========================================
    # USER ENDPOINTS
    # ===========================================

    def get_user_info(self) -> Dict[str, Any]:
        """Get authenticated user information"""
        return self._request('GET', '/v1/users/me')

    def get_user_profile(self) -> Dict[str, Any]:
        """Get user profile (display name)"""
        return self._request('GET', '/v1/users/me/profile')

    def get_user_capabilities(self) -> Dict[str, Any]:
        """Get user's API capabilities"""
        return self._request('GET', '/v1/users/me/capabilities')

    # ===========================================
    # DESIGN ENDPOINTS
    # ===========================================

    def list_designs(
        self,
        limit: int = 50,
        continuation: Optional[str] = None,
        ownership: Optional[str] = None,
        sort_by: Optional[str] = None,
        query: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        List all designs

        Args:
            limit: Max number of results (max: 100)
            continuation: Pagination token
            ownership: Filter by ownership ('owned', 'shared')
            sort_by: Sort field ('relevance', 'modified_descending', 'modified_ascending',
                                 'title_descending', 'title_ascending')
            query: Search query string (max 255 chars)
        """
        params = {'limit': min(limit, 100)}
        if continuation:
            params['continuation'] = continuation
        if ownership:
            params['ownership'] = ownership
        if sort_by:
            params['sort_by'] = sort_by
        if query:
            params['query'] = query[:255]  # API limit

        return self._request('GET', '/v1/designs', params=params)

    def get_design(self, design_id: str) -> Dict[str, Any]:
        """Get design metadata"""
        return self._request('GET', f'/v1/designs/{design_id}')

    def get_design_pages(
        self,
        design_id: str,
        offset: int = 1,
        limit: int = 50
    ) -> Dict[str, Any]:
        """
        Get design pages with thumbnails (preview API)

        Args:
            design_id: Design ID
            offset: Page offset (1-indexed, default: 1)
            limit: Max pages to return (max: 200)
        """
        params = {
            'offset': offset,
            'limit': min(limit, 200)
        }
        return self._request('GET', f'/v1/designs/{design_id}/pages', params=params)

    def get_export_formats(self, design_id: str) -> Dict[str, Any]:
        """Get available export formats for a design"""
        return self._request('GET', f'/v1/designs/{design_id}/export-formats')

    def create_design(
        self,
        design_type: Optional[str] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        title: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a new design

        Args:
            design_type: Preset type (e.g., 'instagram_post', 'presentation')
            width: Custom width (if not using preset)
            height: Custom height (if not using preset)
            title: Design title
        """
        data = {}
        if design_type:
            data['design_type'] = {'type': design_type}
        elif width and height:
            data['design_type'] = {
                'type': 'custom',
                'width': width,
                'height': height
            }
        if title:
            data['title'] = title

        return self._request('POST', '/v1/designs', data=data)

    # ===========================================
    # EXPORT ENDPOINTS
    # ===========================================

    def create_export(
        self,
        design_id: str,
        format_type: str,
        pages: Optional[List[int]] = None,
        quality: Optional[str] = None,
        size: Optional[str] = None,
        lossless: Optional[bool] = None,
        export_quality: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Create export job

        Args:
            design_id: Design to export
            format_type: Export format ('pdf', 'png', 'jpg', 'pptx', 'mp4', 'gif')
            pages: Specific pages to export (1-indexed)
            quality: PDF quality ('standard', 'print' for high quality)
            size: PNG/JPG size ('small', 'medium', 'large')
            lossless: PNG lossless compression (True/False)
            export_quality: JPG quality 1-100 (default varies by size)

        Note: Download URLs are valid for 24 hours
        """
        data = {
            'design_id': design_id,
            'format': {'type': format_type}
        }
        if pages:
            data['pages'] = pages
        if quality:
            data['format']['quality'] = quality
        if size:
            data['format']['size'] = size
        if lossless is not None:
            data['format']['lossless'] = lossless
        if export_quality is not None:
            data['format']['export_quality'] = export_quality

        return self._request('POST', '/v1/exports', data=data)

    def get_export(self, export_id: str) -> Dict[str, Any]:
        """Get export job status and download URL"""
        return self._request('GET', f'/v1/exports/{export_id}')

    def wait_for_export(
        self,
        export_id: str,
        timeout: int = 300,
        poll_interval: int = 2
    ) -> Dict[str, Any]:
        """
        Wait for export to complete

        Args:
            export_id: Export job ID
            timeout: Max wait time in seconds
            poll_interval: Seconds between status checks
        """
        start_time = time.time()

        while time.time() - start_time < timeout:
            result = self.get_export(export_id)
            status = result.get('job', {}).get('status')

            if status == 'completed':
                return result
            elif status == 'failed':
                raise Exception(f"Export failed: {result}")

            time.sleep(poll_interval)

        raise TimeoutError(f"Export timed out after {timeout} seconds")

    # ===========================================
    # FOLDER ENDPOINTS
    # ===========================================

    def create_folder(
        self,
        name: str,
        parent_folder_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a new folder

        Args:
            name: Folder name
            parent_folder_id: Parent folder ID (use 'root' for Projects)
        """
        data = {'name': name}
        if parent_folder_id:
            data['parent_folder_id'] = parent_folder_id

        return self._request('POST', '/v1/folders', data=data)

    def get_folder(self, folder_id: str) -> Dict[str, Any]:
        """Get folder details"""
        return self._request('GET', f'/v1/folders/{folder_id}')

    def update_folder(self, folder_id: str, name: str) -> Dict[str, Any]:
        """Rename a folder"""
        return self._request('PATCH', f'/v1/folders/{folder_id}', data={'name': name})

    def delete_folder(self, folder_id: str) -> Dict[str, Any]:
        """Delete a folder (moves to trash)"""
        return self._request('DELETE', f'/v1/folders/{folder_id}')

    def list_folder_items(
        self,
        folder_id: str,
        limit: int = 50,
        continuation: Optional[str] = None,
        item_types: Optional[List[str]] = None,
        sort_by: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        List items in a folder

        Args:
            folder_id: Folder ID ('root' for Projects, 'uploads' for Uploads)
            limit: Max results (max: 100)
            continuation: Pagination token
            item_types: Filter by types - list of 'design', 'folder', 'image'
            sort_by: Sort order ('modified_descending', 'modified_ascending',
                                'name_descending', 'name_ascending')
        """
        params = {'limit': min(limit, 100)}
        if continuation:
            params['continuation'] = continuation
        if item_types:
            # API expects comma-separated string
            params['item_types'] = ','.join(item_types) if isinstance(item_types, list) else item_types
        if sort_by:
            params['sort_by'] = sort_by

        return self._request('GET', f'/v1/folders/{folder_id}/items', params=params)

    def move_items(
        self,
        item_ids: List[str],
        target_folder_id: str
    ) -> Dict[str, Any]:
        """
        Move items to a folder

        Args:
            item_ids: List of item IDs to move
            target_folder_id: Destination folder ID
        """
        data = {
            'item_ids': item_ids,
            'to_folder_id': target_folder_id
        }
        return self._request('POST', '/v1/folders/move', data=data)

    # ===========================================
    # ASSET ENDPOINTS
    # ===========================================

    def get_asset(self, asset_id: str) -> Dict[str, Any]:
        """Get asset metadata"""
        return self._request('GET', f'/v1/assets/{asset_id}')

    def update_asset(
        self,
        asset_id: str,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Update asset name and/or tags"""
        data = {}
        if name:
            data['name'] = name
        if tags is not None:
            data['tags'] = tags
        return self._request('PATCH', f'/v1/assets/{asset_id}', data=data)

    def delete_asset(self, asset_id: str) -> Dict[str, Any]:
        """Delete an asset (moves to trash)"""
        return self._request('DELETE', f'/v1/assets/{asset_id}')

    def create_asset_upload(
        self,
        name: str,
        file_path: str
    ) -> Dict[str, Any]:
        """
        Upload an asset from file

        Args:
            name: Asset name
            file_path: Path to file
        """
        # Get file info
        path = Path(file_path)
        content_type = self._get_content_type(path.suffix)

        with open(file_path, 'rb') as f:
            file_data = f.read()

        # Create upload job
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': content_type,
            'Asset-Upload-Metadata': json.dumps({'name': name})
        }

        response = requests.post(
            f"{self.BASE_URL}/v1/asset-uploads",
            headers=headers,
            data=file_data,
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()

    def get_asset_upload_status(self, job_id: str) -> Dict[str, Any]:
        """Check asset upload job status"""
        return self._request('GET', f'/v1/asset-uploads/{job_id}')

    def create_url_asset_upload(
        self,
        name: str,
        url: str
    ) -> Dict[str, Any]:
        """
        Upload an asset from URL (preview API)

        Args:
            name: Asset name
            url: Source URL (max 100MB for videos)
        """
        data = {'name': name, 'url': url}
        return self._request('POST', '/v1/url-asset-uploads', data=data)

    def get_url_asset_upload_status(self, job_id: str) -> Dict[str, Any]:
        """Check URL asset upload job status (preview API)"""
        return self._request('GET', f'/v1/url-asset-uploads/{job_id}')

    # ===========================================
    # BRAND TEMPLATE ENDPOINTS (Enterprise only)
    # ===========================================

    def list_brand_templates(
        self,
        limit: int = 25,
        continuation: Optional[str] = None,
        query: Optional[str] = None,
        ownership: Optional[str] = None,
        sort_by: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        List brand templates (Enterprise only)

        Args:
            limit: Max results (max: 100)
            continuation: Pagination token
            query: Search query
            ownership: Filter by ownership
            sort_by: Sort order
        """
        params = {'limit': min(limit, 100)}
        if continuation:
            params['continuation'] = continuation
        if query:
            params['query'] = query
        if ownership:
            params['ownership'] = ownership
        if sort_by:
            params['sort_by'] = sort_by

        return self._request('GET', '/v1/brand-templates', params=params)

    def get_brand_template(self, brand_template_id: str) -> Dict[str, Any]:
        """Get brand template metadata (Enterprise only)"""
        return self._request('GET', f'/v1/brand-templates/{brand_template_id}')

    def get_brand_template_dataset(self, brand_template_id: str) -> Dict[str, Any]:
        """Get brand template dataset definition for autofill (Enterprise only)"""
        return self._request('GET', f'/v1/brand-templates/{brand_template_id}/dataset')

    # ===========================================
    # AUTOFILL ENDPOINTS (Enterprise only)
    # ===========================================

    def create_autofill(
        self,
        brand_template_id: str,
        data: Dict[str, Any],
        title: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create autofill job from brand template (Enterprise only)

        Args:
            brand_template_id: Brand template to use
            data: Autofill data mapping
            title: Optional title for generated design
        """
        request_data = {
            'brand_template_id': brand_template_id,
            'data': data
        }
        if title:
            request_data['title'] = title

        return self._request('POST', '/v1/autofills', data=request_data)

    def get_autofill_status(self, job_id: str) -> Dict[str, Any]:
        """Get autofill job status (Enterprise only)"""
        return self._request('GET', f'/v1/autofills/{job_id}')

    # ===========================================
    # COMMENT ENDPOINTS (Preview API)
    # ===========================================

    def create_comment_thread(
        self,
        design_id: str,
        message: str,
        attached_to: Optional[Dict[str, Any]] = None,
        assignee_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a new comment thread on a design

        Args:
            design_id: Design ID
            message: Comment message
            attached_to: Attachment point (page_id, element_id, region)
            assignee_id: User ID to assign the thread to
        """
        data = {'message': message}
        if attached_to:
            data['attached_to'] = attached_to
        if assignee_id:
            data['assignee_id'] = assignee_id

        return self._request('POST', f'/v1/designs/{design_id}/comments', data=data)

    def get_comment_thread(self, design_id: str, thread_id: str) -> Dict[str, Any]:
        """Get comment thread details"""
        return self._request('GET', f'/v1/designs/{design_id}/comments/{thread_id}')

    def create_reply(
        self,
        design_id: str,
        thread_id: str,
        message: str
    ) -> Dict[str, Any]:
        """
        Reply to a comment thread

        Args:
            design_id: Design ID
            thread_id: Thread ID
            message: Reply message
        """
        return self._request(
            'POST',
            f'/v1/designs/{design_id}/comments/{thread_id}/replies',
            data={'message': message}
        )

    def list_replies(
        self,
        design_id: str,
        thread_id: str,
        limit: int = 50,
        continuation: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        List replies in a comment thread

        Args:
            design_id: Design ID
            thread_id: Thread ID
            limit: Max results (max: 100)
            continuation: Pagination token
        """
        params = {'limit': min(limit, 100)}
        if continuation:
            params['continuation'] = continuation

        return self._request(
            'GET',
            f'/v1/designs/{design_id}/comments/{thread_id}/replies',
            params=params
        )

    def get_reply(self, design_id: str, thread_id: str, reply_id: str) -> Dict[str, Any]:
        """Get a specific reply"""
        return self._request(
            'GET',
            f'/v1/designs/{design_id}/comments/{thread_id}/replies/{reply_id}'
        )

    # ===========================================
    # DESIGN IMPORT ENDPOINTS
    # ===========================================

    def create_design_import(
        self,
        file_path: str,
        title: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Import a design from file (PDF, PPTX, AI, PSD)

        Args:
            file_path: Path to file
            title: Optional title for imported design
        """
        path = Path(file_path)
        content_type = self._get_content_type(path.suffix)

        with open(file_path, 'rb') as f:
            file_data = f.read()

        metadata = {}
        if title:
            metadata['title'] = title

        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/octet-stream',
            'Import-Metadata': json.dumps(metadata) if metadata else '{}'
        }

        response = requests.post(
            f"{self.BASE_URL}/v1/imports",
            headers=headers,
            data=file_data,
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()

    def get_design_import_status(self, job_id: str) -> Dict[str, Any]:
        """Check design import job status"""
        return self._request('GET', f'/v1/imports/{job_id}')

    def create_url_design_import(
        self,
        url: str,
        title: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Import a design from URL

        Args:
            url: Source URL of the file
            title: Optional title for imported design
        """
        data = {'url': url}
        if title:
            data['title'] = title

        return self._request('POST', '/v1/url-imports', data=data)

    def get_url_design_import_status(self, job_id: str) -> Dict[str, Any]:
        """Check URL design import job status"""
        return self._request('GET', f'/v1/url-imports/{job_id}')

    # ===========================================
    # RESIZE ENDPOINTS (Premium feature)
    # ===========================================

    def create_resize(
        self,
        design_id: str,
        width: int,
        height: int,
        title: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a resized copy of a design (Premium feature)

        Args:
            design_id: Design to resize
            width: New width in pixels
            height: New height in pixels (max 25M total pixels)
            title: Optional title for resized design
        """
        data = {
            'design_id': design_id,
            'width': width,
            'height': height
        }
        if title:
            data['title'] = title

        return self._request('POST', '/v1/resizes', data=data)

    def get_resize_status(self, job_id: str) -> Dict[str, Any]:
        """Check resize job status"""
        return self._request('GET', f'/v1/resizes/{job_id}')

    # ===========================================
    # APP ENDPOINTS
    # ===========================================

    def get_app_jwks(self, app_id: str) -> Dict[str, Any]:
        """
        Get JSON Web Key Set for app JWT verification

        Args:
            app_id: The app ID to get JWKS for
        """
        return self._request('GET', f'/v1/apps/{app_id}/jwks')

    # ===========================================
    # CONNECT ENDPOINTS
    # ===========================================

    def get_signing_public_keys(self) -> Dict[str, Any]:
        """Get JSON Web Keys for webhook signature verification (preview API)"""
        return self._request('GET', '/v1/connect/keys')

    # ===========================================
    # OIDC ENDPOINTS
    # ===========================================

    def get_oidc_jwks(self) -> Dict[str, Any]:
        """Get OIDC JSON Web Keys"""
        return self._request('GET', '/v1/oidc/jwks')

    def get_user_info_oidc(self) -> Dict[str, Any]:
        """Get UserInfo claims via OIDC (requires openid scope)"""
        return self._request('GET', '/v1/oidc/userinfo')

    # ===========================================
    # HELPER METHODS
    # ===========================================

    def wait_for_import(
        self,
        job_id: str,
        timeout: int = 300,
        poll_interval: int = 3
    ) -> Dict[str, Any]:
        """
        Wait for design import job to complete

        Args:
            job_id: Import job ID
            timeout: Max wait time in seconds
            poll_interval: Seconds between status checks

        Returns:
            Import result with design info
        """
        start_time = time.time()

        while time.time() - start_time < timeout:
            result = self.get_design_import_status(job_id)
            status = result.get('job', {}).get('status')

            if status == 'success':
                return result
            elif status == 'failed':
                error = result.get('job', {}).get('error', {})
                raise Exception(f"Import failed: {error.get('message', 'Unknown error')}")

            time.sleep(poll_interval)

        raise TimeoutError(f"Import timed out after {timeout} seconds")

    def wait_for_asset_upload(
        self,
        job_id: str,
        timeout: int = 300,
        poll_interval: int = 2
    ) -> Dict[str, Any]:
        """
        Wait for asset upload job to complete

        Args:
            job_id: Upload job ID
            timeout: Max wait time in seconds
            poll_interval: Seconds between status checks

        Returns:
            Upload result with asset info
        """
        start_time = time.time()

        while time.time() - start_time < timeout:
            result = self.get_asset_upload_status(job_id)
            status = result.get('job', {}).get('status')

            if status == 'success':
                return result
            elif status == 'failed':
                error = result.get('job', {}).get('error', {})
                raise Exception(f"Upload failed: {error.get('message', 'Unknown error')}")

            time.sleep(poll_interval)

        raise TimeoutError(f"Upload timed out after {timeout} seconds")

    def wait_for_autofill(
        self,
        job_id: str,
        timeout: int = 300,
        poll_interval: int = 3
    ) -> Dict[str, Any]:
        """
        Wait for autofill job to complete

        Args:
            job_id: Autofill job ID
            timeout: Max wait time in seconds
            poll_interval: Seconds between status checks

        Returns:
            Autofill result with design info
        """
        start_time = time.time()

        while time.time() - start_time < timeout:
            result = self.get_autofill_status(job_id)
            status = result.get('job', {}).get('status')

            if status == 'success':
                return result
            elif status == 'failed':
                error = result.get('job', {}).get('error', {})
                raise Exception(f"Autofill failed: {error.get('message', 'Unknown error')}")

            time.sleep(poll_interval)

        raise TimeoutError(f"Autofill timed out after {timeout} seconds")

    def wait_for_resize(
        self,
        job_id: str,
        timeout: int = 300,
        poll_interval: int = 2
    ) -> Dict[str, Any]:
        """
        Wait for resize job to complete

        Args:
            job_id: Resize job ID
            timeout: Max wait time in seconds
            poll_interval: Seconds between status checks

        Returns:
            Resize result with design info
        """
        start_time = time.time()

        while time.time() - start_time < timeout:
            result = self.get_resize_status(job_id)
            status = result.get('job', {}).get('status')

            if status == 'success':
                return result
            elif status == 'failed':
                error = result.get('job', {}).get('error', {})
                raise Exception(f"Resize failed: {error.get('message', 'Unknown error')}")

            time.sleep(poll_interval)

        raise TimeoutError(f"Resize timed out after {timeout} seconds")

    def download_export(
        self,
        export_id: str,
        output_dir: str,
        filename: Optional[str] = None,
        timeout: int = 300
    ) -> List[str]:
        """
        Wait for export to complete and download the files

        Args:
            export_id: Export job ID
            output_dir: Directory to save files
            filename: Base filename (without extension). If None, uses design title
            timeout: Max wait time for export in seconds

        Returns:
            List of downloaded file paths
        """
        # Wait for export to complete
        result = self.wait_for_export(export_id, timeout)

        # Get download URLs
        urls = result.get('job', {}).get('result', {}).get('urls', [])
        if not urls:
            raise Exception("No download URLs in export result")

        # Create output directory
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        downloaded_files = []

        for i, url_info in enumerate(urls):
            url = url_info if isinstance(url_info, str) else url_info.get('url')

            # Determine filename
            if filename:
                if len(urls) > 1:
                    base_name = f"{filename}_{i+1}"
                else:
                    base_name = filename
            else:
                base_name = f"export_{export_id}_{i+1}"

            # Get extension from URL or content-type
            response = requests.get(url, stream=True, timeout=self.timeout)
            response.raise_for_status()

            content_type = response.headers.get('content-type', '')
            ext = self._get_extension_from_content_type(content_type)

            file_path = output_path / f"{base_name}{ext}"

            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            downloaded_files.append(str(file_path))
            logger.info(f"Downloaded: {file_path}")

        return downloaded_files

    def import_and_wait(
        self,
        file_path: str,
        title: Optional[str] = None,
        timeout: int = 300
    ) -> Dict[str, Any]:
        """
        Import a file (PDF, PPTX, AI, PSD) and wait for completion

        Args:
            file_path: Path to file to import
            title: Optional title for imported design
            timeout: Max wait time in seconds

        Returns:
            Import result with design info including design ID and URL
        """
        # Start import job
        job_result = self.create_design_import(file_path, title)
        job_id = job_result.get('job', {}).get('id')

        if not job_id:
            raise Exception(f"Failed to start import job: {job_result}")

        logger.info(f"Import job started: {job_id}")

        # Wait for completion
        return self.wait_for_import(job_id, timeout)

    def export_and_download(
        self,
        design_id: str,
        format_type: str,
        output_dir: str,
        filename: Optional[str] = None,
        pages: Optional[List[int]] = None,
        quality: Optional[str] = None,
        timeout: int = 300
    ) -> List[str]:
        """
        Export a design and download the result

        Args:
            design_id: Design to export
            format_type: Export format ('pdf', 'png', 'jpg', 'pptx', 'mp4', 'gif')
            output_dir: Directory to save files
            filename: Base filename (without extension)
            pages: Specific pages to export (1-indexed)
            quality: PDF quality ('standard', 'print')
            timeout: Max wait time in seconds

        Returns:
            List of downloaded file paths
        """
        # Start export job
        export_result = self.create_export(
            design_id=design_id,
            format_type=format_type,
            pages=pages,
            quality=quality
        )
        export_id = export_result.get('job', {}).get('id')

        if not export_id:
            raise Exception(f"Failed to start export job: {export_result}")

        logger.info(f"Export job started: {export_id}")

        # Download
        return self.download_export(export_id, output_dir, filename, timeout)

    def upload_asset_and_wait(
        self,
        file_path: str,
        name: Optional[str] = None,
        timeout: int = 300
    ) -> Dict[str, Any]:
        """
        Upload an asset and wait for completion

        Args:
            file_path: Path to file to upload
            name: Optional asset name (defaults to filename)
            timeout: Max wait time in seconds

        Returns:
            Upload result with asset info
        """
        path = Path(file_path)
        asset_name = name or path.stem

        # Start upload job
        job_result = self.create_asset_upload(asset_name, file_path)
        job_id = job_result.get('job', {}).get('id')

        if not job_id:
            raise Exception(f"Failed to start upload job: {job_result}")

        logger.info(f"Upload job started: {job_id}")

        # Wait for completion
        return self.wait_for_asset_upload(job_id, timeout)

    @staticmethod
    def _get_extension_from_content_type(content_type: str) -> str:
        """Get file extension from content type"""
        type_map = {
            'application/pdf': '.pdf',
            'image/png': '.png',
            'image/jpeg': '.jpg',
            'image/gif': '.gif',
            'video/mp4': '.mp4',
            'application/vnd.openxmlformats-officedocument.presentationml.presentation': '.pptx',
        }
        for mime, ext in type_map.items():
            if mime in content_type:
                return ext
        return '.bin'

    @staticmethod
    def _get_content_type(extension: str) -> str:
        """Get MIME type for file extension"""
        types = {
            # Images
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.svg': 'image/svg+xml',
            '.webp': 'image/webp',
            '.heic': 'image/heic',
            '.heif': 'image/heif',
            '.tiff': 'image/tiff',
            '.tif': 'image/tiff',
            # Videos
            '.mp4': 'video/mp4',
            '.mov': 'video/quicktime',
            '.avi': 'video/x-msvideo',
            '.webm': 'video/webm',
            '.mkv': 'video/x-matroska',
            '.m4v': 'video/x-m4v',
            '.mpeg': 'video/mpeg',
            '.mpg': 'video/mpeg',
            # Audio
            '.mp3': 'audio/mpeg',
            '.wav': 'audio/wav',
            '.m4a': 'audio/mp4',
            '.ogg': 'audio/ogg',
            # Design files (for import)
            '.pdf': 'application/pdf',
            '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
            '.ppt': 'application/vnd.ms-powerpoint',
            '.ai': 'application/illustrator',
            '.psd': 'image/vnd.adobe.photoshop',
            '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        }
        return types.get(extension.lower(), 'application/octet-stream')


def get_client() -> CanvaClient:
    """Get configured Canva client instance"""
    return CanvaClient()


if __name__ == '__main__':
    # Test connection
    client = get_client()
    try:
        user = client.get_user_info()
        print(f"Connected as: {user}")
    except Exception as e:
        print(f"Connection failed: {e}")
