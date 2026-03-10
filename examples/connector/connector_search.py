"""Connector search example.

Available AppNames:
    - AppName.GOOGLE_CALENDAR
    - AppName.GITHUB
    - AppName.GOOGLE_DRIVE
    - AppName.GOOGLE_MAIL

Change the app_name parameter below to use a different connector.
"""

import asyncio
import json
import os
from dotenv import load_dotenv
from smart_search_sdk.connector.client import ConnectorClient
from smart_search_sdk.connector.models import ConnectorRequest, AppName

load_dotenv()

async def main():
    base_url = os.getenv("SMART_SEARCH_BASE_URL")
    user_identifier = os.getenv("SMART_SEARCH_USER_IDENTIFIER")
    user_secret = os.getenv("SMART_SEARCH_USER_SECRET")
    if not base_url or not user_identifier or not user_secret:
        raise ValueError("SMART_SEARCH_BASE_URL, SMART_SEARCH_USER_IDENTIFIER, and SMART_SEARCH_USER_SECRET must be set. Copy .env.example to .env and fill in your values.")
    client = ConnectorClient(base_url=base_url)
    await client.authenticate(user_identifier=user_identifier, user_secret=user_secret)
    result = await client.search_connector(
        app_name=AppName.GOOGLE_CALENDAR,  # Change to GITHUB, GOOGLE_DRIVE, or GOOGLE_MAIL
        request=ConnectorRequest(query="List all my upcoming meetings today")
    )
    print(json.dumps(result, indent=4))

asyncio.run(main())
