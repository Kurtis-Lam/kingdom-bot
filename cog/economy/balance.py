import discord
from discord.ext import commands
import json
from helpers import checks

class Balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @checks.has_registered()
    @commands.hybrid_command(aliases=["bal"], name="balance", description="Checks your balance!")
    async def balance(self, ctx, user: discord.Member = None):
        def load_data(file):
            with open(file, "r") as f:
                return json.load(f)

        if user is not None and ctx.author.guild_permissions.administrator:
            user_id = str(user.id)
            balance = load_data("balance.json")
            if user_id in balance:
                coins = balance[user_id].get("coins")
                gems = balance[user_id].get("gems")
                rubies = balance[user_id].get("rubies")
                
                balance_embed = discord.Embed(
                    title=f"{user.display_name}'s balance",
                    color = 0x0097ff
                )
                balance_embed.add_field(name = "Coins", value = f"{coins:,} 🪙", inline = True)
                balance_embed.add_field(name = "Gems", value = f"{gems:,} 💎", inline = True)
                balance_embed.add_field(name = "Rubies", value = f"{rubies:,} <:ruby:1312617052950888538>", inline = True)
                balance_embed.set_thumbnail(url=user.display_avatar.url)
                
                await ctx.send(embed=balance_embed)
        else:
            user_id = str(ctx.message.author.id)
            balance = load_data("balance.json")
            if user_id in balance:
                coins = balance[user_id].get("coins")
                gems = balance[user_id].get("gems")
                rubies = balance[user_id].get("rubies")
                
                balance_embed = discord.Embed(
                    title=f"{ctx.author.display_name}'s balance",
                    color = 0x0097ff
                )
                balance_embed.add_field(name = "Coins", value = f"{coins:,} 🪙", inline = True)
                balance_embed.add_field(name = "Gems", value = f"{gems:,} 💎", inline = True)
                balance_embed.add_field(name = "Rubies", value = f"{rubies:,} <:ruby:1312617052950888538>", inline = True)
                balance_embed.set_thumbnail(url=ctx.author.display_avatar.url)
                
                await ctx.send(embed=balance_embed)
    @balance.error
    async def balance_error(self, ctx, error):
        if isinstance(error, checks.NotStarted):
            need_to_register_embed = error.embed
            await ctx.send(embed=need_to_register_embed)

    @commands.hybrid_command(aliases=["blb"], name="balanceleaderboard", description="Shows the balance leaderboard.")
    async def balanceleaderboard(self, ctx):
        def load_data(file):
            with open(file, "r") as f:
                return json.load(f)

        balance = load_data("balance.json")
    
        leaderboard = []
        for user_id, data in balance.items():
            coins = data.get("coins", 0)
            gems = data.get("gems", 0) * 500
            rubies = data.get("rubies", 0) * 25000
            total_coins = coins + gems + rubies
            leaderboard.append((user_id, total_coins, data))

        leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)

        leaderboard_embed = discord.Embed(title="Balance Leaderboard", color=0x0097ff)
        for index, (user_id, total_coins, data) in enumerate(leaderboard[:10]):
            user = await self.bot.fetch_user(int(user_id))
            coins = data.get("coins", 0)
            gems = data.get("gems", 0)
            rubies = data.get("rubies", 0)
            leaderboard_embed.add_field(
                name=f"{index + 1}: {user.name}",
                value=f"Coins: {coins:,} 🪙, Gems: {gems:,} 💎, Rubies: {rubies:,} <:ruby:1312617052950888538>",
                inline=False
            )
        await ctx.send(embed=leaderboard_embed)

async def setup(bot):
    await bot.add_cog(Balance(bot))