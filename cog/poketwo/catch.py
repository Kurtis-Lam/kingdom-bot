import discord
from discord.ext import commands
import json
import asyncio

class Catch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["clb", "catchlb", "catcheslb", "catchesleaderboard", "cleaderboard"])
    async def catchleaderboard(self, ctx):
        def load_json():
            if ctx.guild.id == 1261873096147865642:
                with open("kingdomcatch.json", 'r') as f:
                    return json.load(f)
            elif ctx.guild.id == 1297077471262281729:
                with open("reservecatch.json", 'r') as f:
                    return json.load(f)
            elif ctx.guild.id == 1079212152814043188:
                with open("grindingcatch.json", 'r') as f:
                    return json.load(f)
            else:
                with open("kingdomcatch.json", 'r') as f:
                    return json.load(f)
        data = load_json()
        sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)[:25]
        leaderboard_message = "|            Trainer           |  Caught  |\n"
        leaderboard_message += "+------------------------------+----------+\n"
        for user_id, catches in sorted_data:
            await asyncio.sleep(0.1)
            user = await self.bot.fetch_user(user_id) 
            username = user.name if user else user_id
            leaderboard_message += f"| {username:<25}    |  {catches:>6}  |\n"
        leaderboard_message += "+------------------------------+----------+"
        await ctx.send(f"```\n{leaderboard_message}\n```")
    
    @commands.command(aliases=["c", "catches", "caught", "stats"])
    async def catch(self, ctx):
        def load_json():
            if ctx.guild.id == 1261873096147865642:
                with open("kingdomcatch.json", 'r') as f:
                    return json.load(f)
            elif ctx.guild.id == 1297077471262281729:
                with open("reservecatch.json", 'r') as f:
                    return json.load(f)
            elif ctx.guild.id == 1079212152814043188:
                with open("grindingcatch.json", 'r') as f:
                    return json.load(f)
            else:
                with open("kingdomcatch.json", 'r') as f:
                    return json.load(f)
        user_id = str(ctx.author.id)
        data = load_json()
        catches = data.get(user_id, 0)
        e = discord.Embed(title=f"{ctx.author.name}\'s Stats", color = 0x0097ff)
        e.add_field(name="Catches:", value = f"{catches}", inline=False)
        e.set_thumbnail(url=ctx.author.display_avatar.url)
        await ctx.send(embed = e)
    
    
async def setup(bot):
    await bot.add_cog(Catch(bot))