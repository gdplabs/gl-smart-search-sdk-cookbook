"""Connector search example (with GL Connectors token).

Available AppNames:
    - AppName.GOOGLE_CALENDAR
    - AppName.GITHUB
    - AppName.GOOGLE_DRIVE
    - AppName.GOOGLE_MAIL
    - AppName.MICROSOFT_ONEDRIVE
    - AppName.MICROSOFT_OUTLOOK
    - AppName.MICROSOFT_CALENDAR

Change the app_name parameter below to use a different connector.

IMPORTANT: The GL_CONNECTORS_USER_TOKEN must match the GL Connectors API Key
and Base URL configured in your Smart Search server settings.
"""

import asyncio
import json
import os
from dotenv import load_dotenv
from smart_search_sdk.connector.client import ConnectorClient
from smart_search_sdk.connector.models import ConnectorRequest, AppName

load_dotenv()


async def main():
    client = ConnectorClient(base_url=os.getenv("SMARTSEARCH_BASE_URL"))
    await client.authenticate(token=os.getenv("SMARTSEARCH_TOKEN"))
    result = await client.search_connector(
        app_name=AppName.GOOGLE_CALENDAR,
        gl_token=os.getenv("GL_CONNECTORS_USER_TOKEN"),
        request=ConnectorRequest(query="List all my upcoming meetings today"),
    )
    print(json.dumps(result, indent=4))


asyncio.run(main())
