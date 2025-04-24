import discord 
from discord.ext import commands
import json

class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.hybrid_command(aliases=["reg"], name="register", description="Registers yourself!")
    async def register(self, ctx):
        def load_data(file):
            with open(file, "r") as f:
                return json.load(f)
        def save_data(file, data):
            with open(file, "w") as f:
                json.dump(data, f, indent=4)
        user_id = str(ctx.message.author.id)
        balance = load_data("balance.json")
        if user_id not in balance:
            balance[user_id] = {
                "coins": 0, #coins are coins
                "gems": 0, #dig
                "rubies": 0, #burgle
                "lifesavers": 0, 
                "fishes": 0, #fish
                "sharks": 0, #fish
                "bunnies": 0, #hunt
                "foxes": 0, #hunt
                "carrots": 0, #farm
                "vegetables": 0, #farm
            }
            save_data("balance.json", balance)
            register_embed = discord.Embed(
                title="Account Successfully Registered ✅",
                color = discord.Color.green()
            )
            await ctx.send(embed=register_embed)
        else:
            registered_embed = discord.Embed(
                title="Account Already Registered ❗",
                color = discord.Color.red()
            )
            await ctx.send(embed=registered_embed)

async def setup(bot):
    await bot.add_cog(Register(bot))