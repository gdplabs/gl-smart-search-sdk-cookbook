"""Basic web search example."""

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
    result = await client.search_web(GetWebSearchResultsRequest(query="What is cloud computing?", result_type="snippets", size=5, site=["https://firecrawl.dev", "https://python.org"], search_mode=WebSearchEngine.AUTO))
    print(json.dumps(result, indent=4))

asyncio.run(main())
