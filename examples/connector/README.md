# Connector Examples

This directory contains cookbook examples for connector functionality using the SmartSearch SDK. Connectors allow you to search and interact with third-party services.

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

All examples support these 7 connector types. Simply change the `app_name` parameter in the code:

- **`AppName.GOOGLE_CALENDAR`** - Google Calendar integration
- **`AppName.GITHUB`** - GitHub integration
- **`AppName.GOOGLE_DRIVE`** - Google Drive integration
- **`AppName.GOOGLE_MAIL`** - Google Mail integration
- **`AppName.MICROSOFT_ONEDRIVE`** - Microsoft OneDrive (`microsoft_onedrive`)
- **`AppName.MICROSOFT_OUTLOOK`** - Microsoft Outlook (`microsoft_outlook`)
- **`AppName.MICROSOFT_CALENDAR`** - Microsoft Calendar (`microsoft_calendar`)

## Available Examples

### Token Generation
- **`get_token.py`** - Generate SmartSearch token from user credentials (token is reusable across all clients)

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

## Authentication

### SmartSearch Authentication

All examples use token-based authentication (recommended). Here's how to get your token:

#### Getting Your Token

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

4. **Now you can use the token** for all examples. The token is reusable across all SmartSearch clients (WebSearchClient, ConnectorClient, etc.).

#### Using the Token (Current Examples)

All examples use token-based authentication:
```python
await client.authenticate(token=os.getenv("SMART_SEARCH_TOKEN"))
```

#### Alternative: Using Credentials Directly

If you prefer to use credentials directly (less efficient):
```python
await client.authenticate(
    user_identifier=os.getenv("SMARTSEARCH_USER_IDENTIFIER"),
    user_secret=os.getenv("SMARTSEARCH_USER_SECRET")
)
```

**Note:** All examples currently use token authentication. To use credentials directly, simply replace the `authenticate()` call in any example with the credentials-based version above.

### GL Connectors Token (Optional)

Examples with `_with_gl_connectors_token` suffix require you to provide `GL_CONNECTORS_USER_TOKEN` in your `.env` file. This is separate from SmartSearch authentication and is used for connector-specific operations.

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
app_name=AppName.MICROSOFT_ONEDRIVE
app_name=AppName.MICROSOFT_OUTLOOK
app_name=AppName.MICROSOFT_CALENDAR
```

## Features

- **Simple & Minimal**: Each example is a standalone, executable file
- **Async/Await**: All examples use modern async patterns
- **Streaming Support**: Examples for both regular and streaming responses
- **Multiple Connectors**: Google Calendar, GitHub, Google Drive, Google Mail, Microsoft OneDrive, Microsoft Outlook, and Microsoft Calendar
- **Token Flexibility**: Choose between SmartSearch credentials or GL Connectors token
