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


session_name = 'ethiomart_session2'

channels = [
    '@ZemenExpress',
    '@nevacomputer',
    '@meneshayeofficial',
    '@ethio_brand_collection',
    '@Leyueqa',
    '@sinayelj',
]

async def scrape_channel(client, channel_username, writer):
    entity = await client.get_entity(channel_username)
    channel_title = entity.title
    
    print(f"[INFO] Starting scraping channel: {channel_title} ({channel_username})")
    
    async for message in client.iter_messages(entity, limit=10000):
        writer.writerow([
            channel_title,
            channel_username,
            message.id,
            message.message,
            message.date,
            message.views or 0,
            message.replies or 0,
            message.forwards or 0
        ])
    print(f"[INFO] Finished scraping {channel_title}")

async def main():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start(phone=phone)
    
    with open('./rawtelegram_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Channel Title', 'Channel Username', 'Message ID', 'Message Text', 'Date', 'Views', 'Replies', 'Forwards'])

        for channel in channels:
            await scrape_channel(client, channel, writer)
            print(f"[INFO] Completed scraping for {channel}")

    await client.disconnect()
    print("[INFO] All channels scraped successfully.")

if __name__ == "__main__":
    asyncio.run(main())
