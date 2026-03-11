"""Streaming connector search example.

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
from smart_search_sdk.config.constants import EventType, SmartSearchEmitDataValue
from smart_search_sdk.connector.client import ConnectorClient
from smart_search_sdk.connector.models import ConnectorRequest, AppName

load_dotenv()

async def _handle_stream(client_method, request):
    response = {}
    stream = await client_method(request, stream=True)
    async for chunk in stream:
        if chunk.type == EventType.RESPONSE:
            response["data"] = [item.model_dump(mode="json") for item in chunk.value.data]
        elif chunk.value.data_type == SmartSearchEmitDataValue.ACTIVITY:
            print(json.dumps(chunk.value.data_value.model_dump(mode="json"), indent=4))
    return response

async def main():
    client = ConnectorClient(base_url=os.getenv("SMARTSEARCH_BASE_URL"))
    await client.authenticate(token=os.getenv("SMARTSEARCH_TOKEN"))
    result = await _handle_stream(lambda req, stream: client.search_connector(app_name=AppName.GOOGLE_CALENDAR, request=req, stream=stream), ConnectorRequest(query="List all my upcoming meetings today"))
    print(json.dumps(result, indent=4))

asyncio.run(main())
