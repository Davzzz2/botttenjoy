from discord.ext import commands
import discord
import requests
import matplotlib.pyplot as plt

class CryptoIntegration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(description="Check crypto prices with chart.")
    async def check(self, ctx, coin: str):
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd&include_24hr_change=true"
        response = requests.get(url)
        data = response.json()
        
        if coin not in data:
            await ctx.send("Invalid coin name.")
            return
        
        price = data[coin]['usd']
        change = data[coin]['usd_24h_change']

        chart_url = f"https://www.coingecko.com/en/coins/{coin}"
        
        embed = discord.Embed(title=f"{coin.upper()} Price", color=discord.Color.gold())
        embed.add_field(name="Current Price", value=f"${price}", inline=True)
        embed.add_field(name="24h Change", value=f"{change:.2f}%", inline=True)
        embed.add_field(name="More Details", value=f"[Click here]({chart_url})", inline=False)
        await ctx.send(embed=embed)
