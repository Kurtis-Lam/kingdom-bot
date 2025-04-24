import discord
from discord.ext import commands

class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        if amount is not None:
            await ctx.channel.purge(limit = amount + 1)
            await ctx.send(f"✅ Deleted {amount} messages", delete_after = 3)
        else:
            await ctx.send("Please provide an amount of messages to delete!", delete_after=3)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx):
        await ctx.channel.purge(limit = None)
        await ctx.send("✅ Cleared the channel", delete_after = 3)
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, message: str):
        await ctx.message.delete()
        await ctx.send(message)

async def setup(bot):
    await bot.add_cog(Message(bot))