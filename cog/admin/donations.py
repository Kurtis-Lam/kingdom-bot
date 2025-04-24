import discord
from discord.ext import commands

class Donations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["dcl"])
    @commands.has_permissions(manage_messages=True)
    async def donationschecklist(self, ctx):

async def setup(bot):
    await bot.add_cog(Donations(bot))