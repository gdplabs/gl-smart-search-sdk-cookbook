# Web Search Examples

This directory contains cookbook examples for web search functionality using the SmartSearch SDK.

## Quick Start

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Set up your environment variables** in `.env`:
   ```env
   SMARTSEARCH_BASE_URL=https://your-api-endpoint.com/
   SMARTSEARCH_TOKEN=your-authentication-token
   # If you don't have a token yet, use these to generate one (see Authentication section below):
   # SMARTSEARCH_USER_IDENTIFIER=your-user-identifier
   # SMARTSEARCH_USER_SECRET=your-user-secret
   ```

3. **Run any example:**
   ```bash
   uv run web_search_basic.py
   ```

## Available Examples

### Token Generation
- **`get_token.py`** - Generate SmartSearch token from user credentials (token is reusable across all clients)

### Basic Web Search
- **`web_search_basic.py`** - Basic web search with snippets
- **`web_search_stream.py`** - Streaming web search

### Web Search with Keypoints
- **`web_search_keypoints.py`** - Web search returning keypoints
- **`web_search_keypoints_stream.py`** - Streaming web search with keypoints

### Web Search Map
- **`web_search_map.py`** - Web search map functionality
- **`web_search_map_stream.py`** - Streaming web search map

### Web Search URLs
- **`web_search_urls.py`** - Search and return URLs only
- **`web_search_urls_stream.py`** - Streaming URL search

### Web Page Operations
- **`web_page_fetch.py`** - Fetch specific web page content
- **`web_page_fetch_stream.py`** - Streaming web page fetch
- **`web_page_snippets.py`** - Extract snippets from a web page
- **`web_page_snippets_stream.py`** - Streaming snippet extraction
- **`web_page_keypoints.py`** - Extract keypoints from a web page
- **`web_page_keypoints_stream.py`** - Streaming keypoint extraction

## Authentication

All examples use token-based authentication (recommended). Here's how to get your token:

### Getting Your Token

If you don't have a token yet, generate one using the provided example:

1. **Set up your user credentials** in `.env`:
   ```env
   SMARTSEARCH_BASE_URL=https://your-api-endpoint.com/
   SMARTSEARCH_USER_IDENTIFIER=your-user-identifier
   SMARTSEARCH_USER_SECRET=your-user-secret
   ```

2. **Run the token generation script:**
   ```bash
   uv run get_token.py
   ```

3. **Copy the printed token** and add it to your `.env` file:
   ```env
   SMARTSEARCH_TOKEN=your-token-here
   ```

4. **Now you can use the token** for all examples. **Important:** The token is reusable across all SmartSearch clients (WebSearchClient, ConnectorClient, etc.). You only need to generate it once and can use it in both web and connector examples.

### Using the Token (Current Examples)

All examples use token-based authentication:
```python
await client.authenticate(token=os.getenv("SMARTSEARCH_TOKEN"))
```

### Alternative: Using Credentials Directly

If you prefer to use credentials directly (less efficient):
```python
await client.authenticate(
    user_identifier=os.getenv("SMARTSEARCH_USER_IDENTIFIER"),
    user_secret=os.getenv("SMARTSEARCH_USER_SECRET")
)
```

**Note:** All examples currently use token authentication. To use credentials directly, simply replace the `authenticate()` call in any example with the credentials-based version above.

## Features

- **Simple & Minimal**: Each example is a standalone, executable file
- **Async/Await**: All examples use modern async patterns
- **Streaming Support**: Examples for both regular and streaming responses
- **Multiple Search Modes**: Support for different search engines and result types
