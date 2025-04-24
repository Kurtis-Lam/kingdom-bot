import discord
from discord.ext import commands
import json

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addcoins(self, ctx, user: discord.Member, amt: int):
        def load_data(file):
            with open(file, "r") as f:
                return json.load(f)
        def save_data(file, data):
            with open(file, "w") as f:
                json.dump(data, f, indent=4)
        balance = load_data("balance.json")
        user_id = str(user.id)
        if user_id not in balance:
            await ctx.send(f"**{user.name}** has not registered yet!")
        balance[user_id]["coins"] += amt
        save_data("balance.json", balance)
        await ctx.send(f"Added {amt} 🪙 to {user.mention}. New balance: {balance[user_id]['coins']} 🪙.")
    @addcoins.error
    async def addcoins_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to use this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please provide a valid user and amount.")
        else:
            await ctx.send("An error occurred while trying to add coins.")
            
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addgems(self, ctx, user: discord.Member, amt: int):
        def load_data(file):
            with open(file, "r") as f:
                return json.load(f)
        def save_data(file, data):
            with open(file, "w") as f:
                json.dump(data, f, indent=4)
        balance = load_data("balance.json")
        user_id = str(user.id)
        if user_id not in balance:
            await ctx.send(f"**{user.name}** has not registered yet!")
        balance[user_id]["gems"] += amt
        save_data("balance.json", balance)
        await ctx.send(f"Added {amt} 💎 to {user.mention}. New balance: {balance[user_id]['gems']} 💎.")
    @addgems.error
    async def addgems_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to use this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please provide a valid user and amount.")
        else:
            await ctx.send("An error occurred while trying to add gems.")
            
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addrubies(self, ctx, user: discord.Member, amt: int):
        def load_data(file):
            with open(file, "r") as f:
                return json.load(f)
        def save_data(file, data):
            with open(file, "w") as f:
                json.dump(data, f, indent=4)
        balance = load_data("balance.json")
        user_id = str(user.id)
        if user_id not in balance:
            await ctx.send(f"**{user.name}** has not registered yet!")
        balance[user_id]["rubies"] += amt
        save_data("balance.json", balance)
        await ctx.send(f"Added {amt} <:ruby:1312617052950888538> to {user.mention}. New balance: {balance[user_id]['rubies']} <:ruby:1312617052950888538>.")
    @addrubies.error
    async def addrubies_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to use this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please provide a valid user and amount.")
        else:
            await ctx.send("An error occurred while trying to add rubies.")

async def setup(bot):
    await bot.add_cog(Admin(bot))