import discord
from discord.ext import commands
import json
import os
from helpers import checks

class Balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @staticmethod
    def load_data(file):
        if not os.path.exists(file):
            return {}
        with open(file, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
        return data

    @checks.has_registered()
    @commands.hybrid_command(aliases=["bal"], name="balance", description="Check your balance")
    async def balance(self, ctx):
        balance = self.load_data("balance.json")
        user_id = str(ctx.message.author.id)
        if user_id in balance:
            coins = balance[user_id].get("coins")
            gems = balance[user_id].get("gems")
            balance_embed = discord.Embed(
                title=f"{ctx.author.display_name}'s balance", 
                color=discord.Color.green()
            )
            balance_embed.add_field(
                name = "Coins", 
                value = f"{coins} 🪙", 
                inline = True
            )
            balance_embed.add_field(
                name = "Gems",
                value = f"{gems} 💎",
                inline = True
            )
            balance_embed.set_thumbnail(url=ctx.author.display_avatar.url)
            await ctx.send(embed=balance_embed)
            
    @balance.error
    async def balance_error(self, ctx, error):
        if isinstance(error, checks.NotStarted):
            embed = error.embed
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Balance(bot))
