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
    base_url = os.getenv("SMART_SEARCH_BASE_URL")
    user_identifier = os.getenv("SMART_SEARCH_USER_IDENTIFIER")
    user_secret = os.getenv("SMART_SEARCH_USER_SECRET")
    if not base_url or not user_identifier or not user_secret:
        raise ValueError("SMART_SEARCH_BASE_URL, SMART_SEARCH_USER_IDENTIFIER, and SMART_SEARCH_USER_SECRET must be set. Copy .env.example to .env and fill in your values.")
    client = WebSearchClient(base_url=base_url)
    await client.authenticate(user_identifier=user_identifier, user_secret=user_secret)
    result = await client.search_web(GetWebSearchResultsRequest(
        query="What is cloud computing?", result_type="snippets", size=5,
        site=["https://firecrawl.dev", "https://python.org"], search_mode=WebSearchEngine.AUTO
    ))
    print(json.dumps(result, indent=4))

asyncio.run(main())
