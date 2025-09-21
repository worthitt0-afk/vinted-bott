import discord
import os
import aiohttp
import asyncio
from discord.ext import tasks
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)

LE_TUE_RICERCHE = [
    {"name": "Ralph Lauren", "url": "https://www.vinted.it/catalog?search_text=ralph+lauren&price_to=20&order=newest_first"},
    {"name": "Levi's Jeans", "url": "https://www.vinted.it/catalog?search_text=jeans+levis&price_to=20&order=newest_first"},
    {"name": "Carhartt", "url": "https://www.vinted.it/catalog?search_text=carhartt&price_to=20&order=newest_first"},
    {"name": "Lacoste Felpe", "url": "https://www.vinted.it/catalog?search_text=felpa+lacoste&price_to=20&order=newest_first"},
    {"name": "Tommy Hilfiger Felpe", "url": "https://www.vinted.it/catalog?search_text=felpa+tommy+hilfiger&price_to=20&order=newest_first"},
    {"name": "The North Face", "url": "https://www.vinted.it/catalog?search_text=the+north+face&price_to=20&order=newest_first"},
    {"name": "Burberry Abbigliamento", "url": "https://www.vinted.it/catalog?search_text=burberry+maglia+felpa+camicia&price_to=20&order=newest_first"},
    {"name": "Stussy", "url": "https://www.vinted.it/catalog?search_text=stussy&price_to=20&order=newest_first"},
    {"name": "Supreme Abbigliamento", "url": "https://www.vinted.it/catalog?search_text=supreme+maglia+felpa+tshirt&price_to=20&order=newest_first"}
]

@tasks.loop(minutes=3)
async def check_vinted():
    print("🔄 Scansionando Vinted...")

@bot.event
async def on_ready():
    print(f'✅ Bot {bot.user} è online!')
    check_vinted.start()

bot.run(os.getenv('DISCORD_TOKEN'))