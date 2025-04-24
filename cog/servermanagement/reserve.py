import discord
from discord.ext import commands
import json

class Reserves(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["ra", "reserveadd"])
    async def reservesadd(self, ctx, pokemon: str, user: discord.User, amount: int):
        def load_reserves():
            with open('reserves.json', 'r') as file:
                return json.load(file)
        def save_reserves(reserves):
            with open('reserves.json', 'w') as file:
                json.dump(reserves, file, indent=4)
        reserves = load_reserves()
        if pokemon in reserves:
            reserves[pokemon]['amount'] += amount
        else:
            reserves[pokemon] = {'user_id': user.id, 'amount': amount}
        save_reserves(reserves)
        e = discord.Embed(title="✅ Successfully added", color = discord.Color.green())
        e.add_field(name = f"Pokemon: {pokemon}", value = "", inline= False)
        e.add_field(name = f"User: {user.display_name}\nUser ID: `{user.id}`", value = "", inline= False)
        e.add_field(name = f"Amount: {amount}\nRemaining: {reserves[pokemon]['amount']}", value = "", inline= False)
        await ctx.send(embed = e)

    
async def setup(bot):
    await bot.add_cog(Reserves(bot))