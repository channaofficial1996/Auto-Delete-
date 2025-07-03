# Auto Delete Link Telegram Bot

Deletes any message containing a link (URL) except if the sender is an admin.

## Usage

1. Put your bot token in `.env` file:

    BOT_TOKEN=YOUR_BOT_TOKEN

2. Deploy to [Railway](https://railway.app/) or run locally:

    ```
    pip install -r requirements.txt
    python main.py
    ```

## Deploy to Railway

1. Upload this project as ZIP
2. Set the BOT_TOKEN environment variable in Railway settings
3. Click "Deploy"

## Features

- Auto deletes message if it contains a link (URL)
- Does **not** delete if the sender is admin/owner
