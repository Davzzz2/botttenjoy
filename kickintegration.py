from discord.ext import commands
import discord
import requests

class KickIntegration(commands.Cog):
    def __init__(self, bot, channel_name):
        self.bot = bot
        self.channel_name = channel_name

    @commands.hybrid_command(description="Check Kick follower count and live status.")
    async def kick_status(self, ctx):
        url = f"https://kick.com/api/v1/channels/{self.channel_name}"
        response = requests.get(url)
        data = response.json()
        
        if 'slug' not in data:
            await ctx.send("Failed to retrieve data from Kick.")
            return
        
        embed = discord.Embed(title=f"Kick Channel: {data['slug']}", color=discord.Color.green())
        embed.add_field(name="Follower Count", value=data.get('followers', 'N/A'), inline=True)
        embed.add_field(name="Live Status", value="Live ✅" if data.get('livestream') else "Offline ❌", inline=True)
        embed.add_field(name="Current Viewers", value=data.get('livestream', {}).get('viewer_count', 'N/A'), inline=True)
        await ctx.send(embed=embed)
