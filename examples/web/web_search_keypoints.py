"""Web search with keypoints example."""

import asyncio
import json
import os
from dotenv import load_dotenv
from smart_search_sdk.web.client import WebSearchClient
from smart_search_sdk.web.models import GetWebSearchResultsRequest
from smart_search_sdk.web.models.model import WebSearchEngine

load_dotenv()


async def main():
    client = WebSearchClient(base_url=os.getenv("SMARTSEARCH_BASE_URL"))
    await client.authenticate(token=os.getenv("SMARTSEARCH_TOKEN"))
    result = await client.search_web(
        GetWebSearchResultsRequest(
            query="Python programming best practices",
            result_type="keypoints",
            size=3,
            search_mode=WebSearchEngine.AUTO,
        )
    )
    print(json.dumps(result, indent=4))


asyncio.run(main())
