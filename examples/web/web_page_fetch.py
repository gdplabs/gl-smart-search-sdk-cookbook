"""Fetch web page example."""

import asyncio
import json
import os
from dotenv import load_dotenv
from smart_search_sdk.web.client import WebSearchClient
from smart_search_sdk.web.models import GetWebPageRequest
from smart_search_sdk.web.models.model import WebSearchEngine

load_dotenv()


async def main():
    client = WebSearchClient(base_url=os.getenv("SMARTSEARCH_BASE_URL"))
    await client.authenticate(token=os.getenv("SMARTSEARCH_TOKEN"))
    result = await client.fetch_web_page(
        GetWebPageRequest(
            source="https://docs.python.org/3/tutorial/",
            return_html=False,
            json_schema={
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "content": {"type": "string"},
                },
                "required": ["title", "content"],
            },
            search_mode=WebSearchEngine.AUTO,
        )
    )
    print(json.dumps(result, indent=4))


asyncio.run(main())
