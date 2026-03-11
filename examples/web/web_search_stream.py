"""Streaming web search example."""

import asyncio
import json
import os
from dotenv import load_dotenv
from pydantic import AnyHttpUrl
from smart_search_sdk.config.constants import EventType, SmartSearchEmitDataValue
from smart_search_sdk.web.client import WebSearchClient
from smart_search_sdk.web.models import GetWebSearchResultsRequest
from smart_search_sdk.web.models.model import WebSearchEngine

load_dotenv()


async def _handle_stream(client_method, request):
    response = {}
    stream = await client_method(request, stream=True)
    async for chunk in stream:
        if chunk.type == EventType.RESPONSE:
            response["data"] = [
                item.model_dump(mode="json")
                if not isinstance(item, AnyHttpUrl)
                else str(item)
                for item in chunk.value.data
            ]
        elif chunk.value.data_type == SmartSearchEmitDataValue.ACTIVITY:
            print(json.dumps(chunk.value.data_value.model_dump(mode="json"), indent=4))
    return response


async def main():
    client = WebSearchClient(base_url=os.getenv("SMARTSEARCH_BASE_URL"))
    await client.authenticate(token=os.getenv("SMARTSEARCH_TOKEN"))
    result = await _handle_stream(
        client.search_web,
        GetWebSearchResultsRequest(
            query="What is cloud computing?",
            result_type="snippets",
            size=5,
            site=["https://python.org", "https://docs.python.org"],
            search_mode=WebSearchEngine.AUTO,
        ),
    )
    print(json.dumps(result, indent=4))


asyncio.run(main())
