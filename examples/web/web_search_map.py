"""Web search map example."""

import asyncio
import json
import os
from dotenv import load_dotenv
from smart_search_sdk.web.client import WebSearchClient
from smart_search_sdk.web.models import GetWebSearchMapRequest

load_dotenv()

async def main():
    client = WebSearchClient(base_url=os.getenv("SMARTSEARCH_BASE_URL"))
    await client.authenticate(token=os.getenv("SMARTSEARCH_TOKEN"))
    result = await client.search_web_map(GetWebSearchMapRequest(base_url="https://firecrawl.dev", size=10, include_subdomains=False, query="scraping", page=1, return_all_map=False))
    print(json.dumps(result, indent=4))

asyncio.run(main())
