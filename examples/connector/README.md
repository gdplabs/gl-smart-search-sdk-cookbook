# Connector Examples

This directory contains cookbook examples for connector functionality using the SmartSearch SDK. Connectors allow you to search and interact with third-party services.

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
   # Optional: Only needed for examples with GL Connectors token
   GL_CONNECTORS_USER_TOKEN=your-gl-connectors-token
   GL_CONNECTORS_DEFAULT_CALLBACK_URL=https://your-callback-url.com
   ```

3. **Workflow: Connect → Search → Disconnect**
   
   **⚠️ Important:** You must connect a connector before you can search it. Follow this sequence:
   
   ```bash
   # Step 1: Connect a connector (required first)
   uv run connector_connect.py
   
   # Step 2: Search the connected connector
   uv run connector_search.py
   
   # Step 3: Disconnect when done (optional)
   uv run connector_disconnect.py
   ```
   
   If you try to search before connecting, you'll get an error. Always run `connector_connect.py` first.

## Available Connectors

All examples support these 4 connector types. Simply change the `app_name` parameter in the code:

- **`AppName.GOOGLE_CALENDAR`** - Google Calendar integration
- **`AppName.GITHUB`** - GitHub integration
- **`AppName.GOOGLE_DRIVE`** - Google Drive integration
- **`AppName.GOOGLE_MAIL`** - Google Mail integration

## Available Examples

### Connect (Run First!)
- **`connector_connect.py`** - Connect connector using SmartSearch credentials
- **`connector_connect_with_gl_connectors_token.py`** - Connect connector using GL Connectors token
- **⚠️ Required:** You must connect before searching. Run one of these first.

### Search (After Connecting)
- **`connector_search.py`** - Search connector using SmartSearch credentials
- **`connector_search_with_gl_connectors_token.py`** - Search connector using GL Connectors token
- **`connector_search_stream.py`** - Streaming search (SmartSearch credentials)
- **`connector_search_with_gl_connectors_token_stream.py`** - Streaming search (GL Connectors token)

### Disconnect (Optional)
- **`connector_disconnect.py`** - Disconnect connector using SmartSearch credentials
- **`connector_disconnect_with_gl_connectors_token.py`** - Disconnect connector using GL Connectors token

## Authentication Types

### SmartSearch Credentials (Default)
Examples without `_with_gl_connectors_token` suffix use `SMART_SEARCH_USER_IDENTIFIER` and `SMART_SEARCH_USER_SECRET` for authentication. No additional `GL_CONNECTORS_USER_TOKEN` is required.

### With GL Connectors Token
Examples with `_with_gl_connectors_token` suffix require you to provide `GL_CONNECTORS_USER_TOKEN` in your `.env` file.

**⚠️ IMPORTANT:** The `GL_CONNECTORS_USER_TOKEN` must match the GL Connectors API Key and Base URL configured in your Smart Search server settings. Ensure these values are correctly set in your Smart Search server configuration before using these examples.

## Changing the Connector

To use a different connector, simply change the `app_name` parameter in the example file:

```python
# Change this line:
app_name=AppName.GOOGLE_CALENDAR

# To any of:
app_name=AppName.GITHUB
app_name=AppName.GOOGLE_DRIVE
app_name=AppName.GOOGLE_MAIL
```

## Features

- **Simple & Minimal**: Each example is a standalone, executable file
- **Async/Await**: All examples use modern async patterns
- **Streaming Support**: Examples for both regular and streaming responses
- **Multiple Connectors**: Support for Google Calendar, GitHub, Google Drive, and Google Mail
- **Token Flexibility**: Choose between SmartSearch credentials or GL Connectors token
