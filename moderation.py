from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(description="Ban a user.")
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned for {reason}.")

    @commands.hybrid_command(description="Mute a user.")
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            muted_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted_role, speak=False, send_messages=False)
        await member.add_roles(muted_role, reason=reason)
        await ctx.send(f"{member.mention} has been muted.")

    @commands.hybrid_command(description="Timeout a user.")
    async def timeout(self, ctx, member: discord.Member, duration: int, *, reason=None):
        await member.timeout_for(duration, reason=reason)
        await ctx.send(f"{member.mention} has been timed out for {duration} seconds.")

    @commands.hybrid_command(description="Warn a user.")
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        await ctx.send(f"{member.mention} has been warned for {reason}.")

    @commands.hybrid_command(description="Purge messages.")
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"Purged {amount} messages.", delete_after=5)
