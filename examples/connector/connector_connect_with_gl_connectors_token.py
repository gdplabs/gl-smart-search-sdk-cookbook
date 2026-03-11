"""Connector connect example (with GL Connectors token).

Available AppNames:
    - AppName.GOOGLE_CALENDAR
    - AppName.GITHUB
    - AppName.GOOGLE_DRIVE
    - AppName.GOOGLE_MAIL

Change the app_name parameter below to use a different connector.

IMPORTANT: The GL_CONNECTORS_USER_TOKEN must match the GL Connectors API Key
and Base URL configured in your Smart Search server settings.
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
        gl_token=os.getenv("GL_CONNECTORS_USER_TOKEN"),
        request=ConnectorConnectRequest(
            callback_url=os.getenv("GL_CONNECTORS_DEFAULT_CALLBACK_URL")
        ),
    )
    print(json.dumps(result, indent=4))


asyncio.run(main())
