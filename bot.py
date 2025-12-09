# AUTO ADVERTISER 2025 — FINAL RENDER.COM VERSION (RESPONDS TO "hi" + FULL UI)
import discord, os
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"BOT ONLINE — {bot.user} — EMPIRE 24/7")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    embed = discord.Embed(title="AUTO ADVERTISER 2025", color=0x00ff00)
    embed.description = "Click below for free access"
    view = View()
    view.add_item(Button(label="FREE ACCESS (24H)", style=discord.ButtonStyle.link, url="https://direct-link.net/1459521/dbnK1AmtsYTw"))
    
    await message.channel.send(embed=embed, view=view)

bot.run(os.getenv("DISCORD_TOKEN"))
