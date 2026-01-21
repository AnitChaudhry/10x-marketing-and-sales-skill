#!/usr/bin/env python3
"""
Canva OAuth Flow - Get Access Token
Run this script to authorize and get your access token.
"""

import os
import sys
import json
import webbrowser
import urllib.parse
from pathlib import Path
from threading import Thread
import time

try:
    import requests
    from flask import Flask, request
    from dotenv import load_dotenv
except ImportError:
    print("Required packages not installed.")
    print("Run: pip install requests flask python-dotenv")
    sys.exit(1)

# Load environment
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

CLIENT_ID = os.getenv('CANVA_CLIENT_ID')
CLIENT_SECRET = os.getenv('CANVA_CLIENT_SECRET')
REDIRECT_URI = os.getenv('CANVA_REDIRECT_URI', 'http://127.0.0.1:3001/oauth/redirect')

# Scopes to request - Full list based on Canva Connect API documentation
SCOPES = [
    # Design scopes
    'design:content:read',
    'design:content:write',
    'design:meta:read',
    # Asset scopes
    'asset:read',
    'asset:write',
    # Folder scopes
    'folder:read',
    'folder:write',
    # Profile scope
    'profile:read',
    # Comment scopes (preview API)
    'comment:read',
    'comment:write',
    # Brand template scopes (Enterprise only)
    'brandtemplate:meta:read',
    'brandtemplate:content:read',
]

app = Flask(__name__)
auth_code = None
server_should_stop = False


@app.route('/oauth/redirect')
def oauth_callback():
    """Handle OAuth callback"""
    global auth_code, server_should_stop

    auth_code = request.args.get('code')
    error = request.args.get('error')

    if error:
        return f"""
        <html><body style="font-family: Arial; padding: 50px; text-align: center;">
        <h1 style="color: red;">Authorization Failed</h1>
        <p>Error: {error}</p>
        <p>{request.args.get('error_description', '')}</p>
        </body></html>
        """

    if auth_code:
        server_should_stop = True
        return """
        <html><body style="font-family: Arial; padding: 50px; text-align: center;">
        <h1 style="color: green;">Authorization Successful!</h1>
        <p>You can close this window and return to the terminal.</p>
        </body></html>
        """

    return "No authorization code received"


def get_auth_url():
    """Generate authorization URL"""
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'scope': ' '.join(SCOPES),
        'state': 'canva_auth_state'
    }
    base_url = 'https://www.canva.com/api/oauth/authorize'
    return f"{base_url}?{urllib.parse.urlencode(params)}"


def exchange_code_for_token(code):
    """Exchange authorization code for access token"""
    token_url = 'https://api.canva.com/v1/oauth/token'

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    response = requests.post(token_url, data=data)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

    return response.json()


def refresh_access_token(refresh_token=None):
    """
    Refresh an expired access token using refresh token.

    Args:
        refresh_token: The refresh token (uses env var if not provided)

    Returns:
        New tokens dict or None if failed
    """
    token_url = 'https://api.canva.com/v1/oauth/token'

    refresh_token = refresh_token or os.getenv('CANVA_REFRESH_TOKEN')

    if not refresh_token:
        print("Error: No refresh token available")
        return None

    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    response = requests.post(token_url, data=data)

    if response.status_code != 200:
        print(f"Error refreshing token: {response.status_code}")
        print(response.text)
        return None

    return response.json()


def revoke_token(token, token_type_hint='access_token'):
    """
    Revoke an access or refresh token.

    Args:
        token: The token to revoke
        token_type_hint: 'access_token' or 'refresh_token'

    Returns:
        True if successful, False otherwise
    """
    revoke_url = 'https://api.canva.com/v1/oauth/revoke'

    data = {
        'token': token,
        'token_type_hint': token_type_hint,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    response = requests.post(revoke_url, data=data)

    return response.status_code == 200


def introspect_token(token):
    """
    Check if a token is valid and get its metadata.

    Args:
        token: The token to introspect

    Returns:
        Token info dict or None if invalid
    """
    introspect_url = 'https://api.canva.com/v1/oauth/introspect'

    data = {
        'token': token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    response = requests.post(introspect_url, data=data)

    if response.status_code != 200:
        return None

    return response.json()


def update_env_file(access_token, refresh_token):
    """Update .env file with tokens"""
    env_content = env_path.read_text()

    # Update or add access token
    if 'CANVA_ACCESS_TOKEN=' in env_content:
        lines = env_content.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('CANVA_ACCESS_TOKEN='):
                lines[i] = f'CANVA_ACCESS_TOKEN={access_token}'
            elif line.startswith('CANVA_REFRESH_TOKEN='):
                lines[i] = f'CANVA_REFRESH_TOKEN={refresh_token}'
        env_content = '\n'.join(lines)
    else:
        env_content += f'\nCANVA_ACCESS_TOKEN={access_token}'
        env_content += f'\nCANVA_REFRESH_TOKEN={refresh_token}'

    env_path.write_text(env_content)
    print(f"\n[OK] Tokens saved to {env_path}")


def run_server():
    """Run Flask server"""
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(host='127.0.0.1', port=3001, debug=False, use_reloader=False)


def main():
    global auth_code, server_should_stop

    print("=" * 50)
    print("CANVA OAUTH AUTHORIZATION")
    print("=" * 50)

    if not CLIENT_ID or not CLIENT_SECRET:
        print("\n[X] Error: Missing credentials in .env file")
        print("   CANVA_CLIENT_ID and CANVA_CLIENT_SECRET required")
        sys.exit(1)

    print(f"\nClient ID: {CLIENT_ID[:10]}...")
    print(f"Redirect URI: {REDIRECT_URI}")

    # Start server in background
    print("\n[*] Starting local server on port 3001...")
    server_thread = Thread(target=run_server, daemon=True)
    server_thread.start()
    time.sleep(1)

    # Generate and open auth URL
    auth_url = get_auth_url()
    print("\n[*] Opening browser for authorization...")
    print(f"\nIf browser doesn't open, visit this URL:\n{auth_url}\n")

    webbrowser.open(auth_url)

    # Wait for callback
    print("[*] Waiting for authorization...")
    timeout = 300
    start = time.time()

    while not server_should_stop and (time.time() - start) < timeout:
        time.sleep(1)

    if not auth_code:
        print("\n[X] Timeout or no authorization code received")
        sys.exit(1)

    print(f"\n[OK] Authorization code received!")

    # Exchange for token
    print("[*] Exchanging code for access token...")
    tokens = exchange_code_for_token(auth_code)

    if not tokens:
        print("[X] Failed to get access token")
        sys.exit(1)

    access_token = tokens.get('access_token')
    refresh_token = tokens.get('refresh_token', '')

    print(f"\n[OK] Access token received!")
    print(f"    Token: {access_token[:20]}...")
    print(f"    Expires in: {tokens.get('expires_in', 'unknown')} seconds")

    # Save to .env
    update_env_file(access_token, refresh_token)

    print("\n" + "=" * 50)
    print("AUTHORIZATION COMPLETE!")
    print("=" * 50)
    print("\nYou can now use Canva API features.")
    print("Run 'python scripts/auth_check.py' to verify.")


if __name__ == '__main__':
    main()
