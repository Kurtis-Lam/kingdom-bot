import discord
from discord.ext import commands
import json
import os

class Register(commands.Cog):
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
    @staticmethod
    def save_data(file, data):
        with open(file, "w") as f:
            json.dump(data, f)
      
    @commands.hybrid_command(aliases=["reg"], name="register", description="Register yourself to use our economy-related commands!")
    async def register(self, ctx):
        user_id = str(ctx.message.author.id)
        balance = self.load_data("balance.json")
        registered = self.load_data("registered.json")
        if user_id not in registered:
            registered[user_id] = True
            balance[user_id] = {
                "coins": 0,
                "gems": 0
            }
            self.save_data("registered.json", registered)
            self.save_data("balance.json", balance)
            register_embed = discord.Embed(
                title="Account Successfully Registered ✅", 
                description="You are now registered!", 
                color = discord.Color.green()
            )
            await ctx.send(embed=register_embed)
        else:
            registered_embed = discord.Embed(
                title="Account Already Registered", 
                description="You already have an account!", 
                color = discord.Color.red()
            )
            await ctx.send(embed=registered_embed)

async def setup(bot):
    await bot.add_cog(Register(bot))
