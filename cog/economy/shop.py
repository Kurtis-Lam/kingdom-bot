import discord
from discord.ext import commands
import json
from helpers import checks

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=["gstats"])
    async def grindingstatistics(self, ctx):
        statistics = {
            "BURGLE 🥷": {
                "Highest": "500c; 1r / burgle",
                "Lowest": "100c; 0r / burgle",
                "Average": "300c; ¹⁄₅₀r / burgle",
                "Cooldown": "120s",
                "Highest (af)": "360,000c; 720r",
                "Lowest (af)": "72,000c; 0r",
                "Average (af)": "216,000c; 14r"
            },
            "COINFLIP 🎲": {
                "Highest": "10,000c / game",
                "Lowest": "-10,000c / game",
                "Average": "0c / game",
               "Cooldown": "30s",
                "Highest (af)": "28,800,000c",
                "Lowest (af)": "-28,000,000c",
                "Average (af)": "0c"
            },
            "DIG 🌱": {
                "Highest": "10,000c; 1g / dig",
                "Lowest": "10c; 0g / dig",
                "Average": "70c; ⅒g / dig",
                "Cooldown": "15s",
                "Highest (af)": "57,600,000c; 5,760g",
                "Lowest (af)": "57,600c; 0g",
                "Average (af)": "403,200c; 576g"
            },
            "FISH 🐟": {
                "Highest": "200c; 1fish; 1shark / fish",
                "Lowest": "50c; 0fish; 0shark / fish",
                "Average": "125c; ¹⁄₁₀fish; ¹⁄₂₀shark; / fish",
                "Cooldown": "15s",
                "Highest (af)": "1,152,000c; 5,760fish; 5,760shark",
                "Lowest (af)": "388,000c; 0fish; 0shark",
                "Average (af)": "720,000c; 576fish; 288shark"
            },
            "HUNT 🦌": {
                "Highest": "300c; 1bunny; 1fox / hunt",
                "Lowest": "1c; 0bunny; 0fox / hunt",
                "Average": "150c; ¹⁄₅bunny; ⅒fox / hunt",
                "Cooldown": "15s",
                "Highest (af)": "1,728,000c; 5,760bunny; 5,760fox",
                "Lowest (af)": "5,760c; 0bunny; 0fox",
                "Average (af)": "864,000c; 1,152bunny, 576fox"
            },
            "RPS 🪨📃✂️": {
                "Highest": "300c / game",
                "Lowest": "100c / game",
                "Average": "200c / game",
                "Cooldown": "60s",
                "Highest (af)": "432,000c",
                "Lowest (af)": "144,000c",
                "Average (af)": "288,000c"
            },
            "Overall (ALL commands)": {
                "Highest (af)": "90,072,000c",
                "Lowest (af)": "-28,132,640c",
                "Average (af)": "2,491,200c"
            }
        }
        e = discord.Embed(
            title="Grinding Statistics",
            description=(
                "In this command, you will find the statistics of every command to get you coins, gems, rubies, and things in inventory.\n"
                "`c`: coins 🪙\n"
                "`g`: gems 💎\n"
                "`r`: rubies <:ruby:1312617052950888538>\n"
                "`s`: seconds ⌛\n"
                "`af`: auto-farm for 1 day 🚜\n"
                "PLEASE BE AWARE THAT THE AUTO-FARMING MENTIONED IS ILLEGAL.\n"
                "IT IS FOR REFERENCE ONLY."
            ),
            color=0x0097ff
        )
        for command, stats in statistics.items():
            field_value = "\n".join(f"{key}: {value}" for key, value in stats.items())
            e.add_field(name=command, value=field_value, inline=False)
        await ctx.send(embed=e)
        
    @commands.command()
    async def shop(self, ctx, page: int= None):
        e = discord.Embed(title="", description="Use `.shop {page}` to view different pages!", color = 0x0097ff)
        e.set_author(name="Pokétwo Kingdom Shop", icon_url=ctx.guild.icon)
        if page == None:
            e.add_field(name="Page 1", value="Items that can be bought by coins 🪙")
            e.add_field(name="Page 2", value="Items that can be bought by gems 💎")
            e.add_field(name="Page 3", value="Items that can be bought by rubies <:ruby:1312617052950888538>")
        elif page == 1:
            e.add_field(name="Gems 💎", value="Cost: 500", inline=False)
            e.add_field(name="Lifesavers 🛟", value="Cost: 1,500", inline=False)
        elif page == 2:
            e.add_field(name="Rubies <:ruby:1312617052950888538>", value="Cost: 50", inline=False)
            e.add_field(name="Raffle Tickets 🎫", value="Cost: 10", inline=False)
            e.add_field(name="Redeem Spawn Hint 🎁", value="Cost: 15", inline=False)
        elif page == 3:
            e.add_field(name="Coming Soon...", value="", inline=False)
        e.set_footer(text="Use `.buy {item: str} {qty = None}` to buy specific items!", icon_url=ctx.guild.icon.url if ctx.guild.icon else None)
        await ctx.send(embed = e)
    
async def setup(bot):
    await bot.add_cog(Shop(bot))