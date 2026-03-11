"""Web search URLs example."""

import asyncio
import json
import os
from dotenv import load_dotenv
from smart_search_sdk.web.client import WebSearchClient
from smart_search_sdk.web.models import GetWebSearchUrlsRequest
from smart_search_sdk.web.models.model import WebSearchEngine

load_dotenv()

async def main():
    client = WebSearchClient(base_url=os.getenv("SMARTSEARCH_BASE_URL"))
    await client.authenticate(token=os.getenv("SMARTSEARCH_TOKEN"))
    result = await client.search_web_urls(GetWebSearchUrlsRequest(query="Python programming tutorials", size=5, site=["https://python.org", "https://realpython.com"], search_mode=WebSearchEngine.AUTO))
    print(json.dumps(result, indent=4))

asyncio.run(main())
