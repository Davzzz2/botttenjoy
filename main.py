import discord
from discord import app_commands
from discord.ext import commands
import json

from moderation import Moderation
from kick_integration import KickIntegration
from crypto_integration import CryptoIntegration
from keep_alive import keep_alive
keep_alive()


# Load config
with open('config.json') as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)
tree = bot.tree

# Load cogs
@bot.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {bot.user}")

# Add cogs
async def setup():
    await bot.add_cog(Moderation(bot))
    await bot.add_cog(KickIntegration(bot, config['KICK_CHANNEL']))
    await bot.add_cog(CryptoIntegration(bot))

bot.loop.create_task(setup())
bot.run(config['DISCORD_TOKEN'])
