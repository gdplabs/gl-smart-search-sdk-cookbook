"""Connector connect example.

Available AppNames:
    - AppName.GOOGLE_CALENDAR
    - AppName.GITHUB
    - AppName.GOOGLE_DRIVE
    - AppName.GOOGLE_MAIL

Change the app_name parameter below to use a different connector.

Note: This example uses GL_CONNECTORS_DEFAULT_CALLBACK_URL for the callback URL.
This is required for connector connection regardless of whether you're using
SmartSearch credentials or GL Connectors token.
"""

import asyncio
import json
import os
from dotenv import load_dotenv
from smart_search_sdk.connector.client import ConnectorClient
from smart_search_sdk.connector.models import ConnectorConnectRequest, AppName

load_dotenv()


async def main():
    client = ConnectorClient(base_url=os.getenv("SMARTSEARCH_BASE_URL"))
    await client.authenticate(token=os.getenv("SMARTSEARCH_TOKEN"))
    result = await client.connect_connector(
        app_name=AppName.GOOGLE_CALENDAR,
        request=ConnectorConnectRequest(
            callback_url=os.getenv("GL_CONNECTORS_DEFAULT_CALLBACK_URL")
        ),
    )
    print(json.dumps(result, indent=4))


asyncio.run(main())
