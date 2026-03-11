"""Web page keypoints example."""

import asyncio
import json
import os
from dotenv import load_dotenv
from smart_search_sdk.web.client import WebSearchClient
from smart_search_sdk.web.models import GetWebPageKeypointsRequest

load_dotenv()

async def main():
    client = WebSearchClient(base_url=os.getenv("SMARTSEARCH_BASE_URL"))
    await client.authenticate(token=os.getenv("SMARTSEARCH_TOKEN"))
    result = await client.get_web_page_keypoints(GetWebPageKeypointsRequest(query="Python programming concepts", source="https://docs.python.org/3/tutorial/", size=3))
    print(json.dumps(result, indent=4))

asyncio.run(main())
