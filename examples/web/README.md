# Web Search Examples

This directory contains cookbook examples for web search functionality using the SmartSearch SDK.

## Quick Start

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Set up your environment variables** in `.env`:
   ```env
   SMART_SEARCH_BASE_URL=https://your-api-endpoint.com/
   SMART_SEARCH_USER_IDENTIFIER=your-user-identifier
   SMART_SEARCH_USER_SECRET=your-user-secret
   ```

3. **Run any example:**
   ```bash
   uv run web_search_basic.py
   ```

## Available Examples

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

## Features

- **Simple & Minimal**: Each example is a standalone, executable file
- **Async/Await**: All examples use modern async patterns
- **Streaming Support**: Examples for both regular and streaming responses
- **Multiple Search Modes**: Support for different search engines and result types
