import os
import csv
import asyncio
from dotenv import load_dotenv
from telethon import TelegramClient

# Load environment variables
load_dotenv('.env')
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
phone = os.getenv('TELEGRAM_PHONE')

session_name = 'ethiomart_session'

channels = [
    '@ZemenExpress',
    '@nevacomputer',
    '@meneshayeofficial',
    '@ethio_brand_collection',
    '@Leyueqa',
    '@sinayelj',
]

MEDIA_DIR = 'photos'
os.makedirs('../data/raw' + MEDIA_DIR, exist_ok=True)

async def scrape_channel(client, channel_username, writer):
    entity = await client.get_entity(channel_username)
    channel_title = entity.title  # Extract the channel's title
    
    print(f"[INFO] Starting scraping channel: {channel_title} ({channel_username})")
    
    async for message in client.iter_messages(entity, limit=10000):
        media_path = None
        # Check if media exists and is a photo
        if message.media and hasattr(message.media, 'photo'):
            filename = f"{channel_username}_{message.id}.jpg"
            media_path = os.path.join(MEDIA_DIR, filename)
            await client.download_media(message.media, media_path)
            print(f"  [MEDIA] Downloaded {media_path}")

        writer.writerow([
            channel_title,
            channel_username,
            message.id,
            message.message,
            message.date,
            media_path
        ])
    print(f"[INFO] Finished scraping {channel_title}")

async def main():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start(phone=phone)
    
    with open('../data/rawtelegram_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])

        for channel in channels:
            await scrape_channel(client, channel, writer)
            print(f"[INFO] Completed scraping for {channel}")

    await client.disconnect()
    print("[INFO] All channels scraped successfully.")

if __name__ == "__main__":
    asyncio.run(main())
