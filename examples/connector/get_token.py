"""Get SmartSearch token from user credentials.

Run this script to generate a SMARTSEARCH_TOKEN from your user credentials.
The token is reusable across all SmartSearch clients (WebSearchClient, ConnectorClient, etc.).

Copy the printed token to your .env file as SMARTSEARCH_TOKEN.
"""

import asyncio
import os
from dotenv import load_dotenv
from smart_search_sdk.connector.client import ConnectorClient

load_dotenv()


async def main():
    client = ConnectorClient(base_url=os.getenv("SMARTSEARCH_BASE_URL"))
    await client.authenticate(
        user_identifier=os.getenv("SMARTSEARCH_USER_IDENTIFIER"),
        user_secret=os.getenv("SMARTSEARCH_USER_SECRET"),
    )
    token = client.token
    print(f"SMARTSEARCH_TOKEN={token}")


asyncio.run(main())
