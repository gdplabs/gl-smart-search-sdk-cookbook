"""Connector disconnect example.

Available AppNames:
    - AppName.GOOGLE_CALENDAR
    - AppName.GITHUB
    - AppName.GOOGLE_DRIVE
    - AppName.GOOGLE_MAIL
    - AppName.MICROSOFT_ONEDRIVE
    - AppName.MICROSOFT_OUTLOOK
    - AppName.MICROSOFT_CALENDAR

Change the app_name parameter below to use a different connector.
"""

import asyncio
import json
import os
from dotenv import load_dotenv
from smart_search_sdk.connector.client import ConnectorClient
from smart_search_sdk.connector.models import AppName

load_dotenv()


async def main():
    client = ConnectorClient(base_url=os.getenv("SMARTSEARCH_BASE_URL"))
    await client.authenticate(token=os.getenv("SMARTSEARCH_TOKEN"))
    result = await client.disconnect_connector(app_name=AppName.GOOGLE_CALENDAR)
    print(json.dumps(result, indent=4))


asyncio.run(main())
