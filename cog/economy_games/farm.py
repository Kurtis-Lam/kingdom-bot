import discord
from discord.ext import commands
import asyncio
import datetime
import random
import json
from helpers import checks

class Farm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @checks.has_registered()
    @commands.hybrid_command(name="farm", description="Farm your farm to earn money!")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def farm(self, ctx):
        def load_data(file):
            with open(file, "r") as f:
                return json.load(f)
        def save_data(file, data):
            with open(file, "w") as f:
                json.dump(data, f, indent=4)
        user_id = str(ctx.message.author.id)
        balance = load_data("balance.json")
        if user_id in balance:
            ce1 = random.randint(5, 10)
            ce2 = random.randint(5, 10)
            ce3 = random.randint(5, 10)
            ce4 = random.randint(5, 10)
            ce5 = random.randint(5, 10)
            ce6 = random.randint(5, 10)
            ce7 = random.randint(5, 10)
            ce8 = random.randint(5, 10)
            ce9 = random.randint(5, 10)
            ce10 = random.randint(5, 10)
            ce11 = random.randint(5, 10)
            ce12 = random.randint(5, 10)
            ce13 = random.randint(5, 10)
            ce14 = random.randint(5, 10)
            ce15 = random.randint(5, 10)
            coins = balance[user_id].get("coins")
            coins_earned = ce1+ce2+ce3+ce4+ce5+ce6+ce7+ce8+ce9+ce10+ce11+ce12+ce13+ce14+ce15
            coins += coins_earned
            balance[user_id]["coins"] = coins
            save_data("balance.json", balance)
            
            farm_embed = discord.Embed(
                title = "Farming in in your farm... 🚜", 
                color = 0x0097ff
            )
            earned_embed = discord.Embed(
                title = f"{ctx.author.display_name} went farming! 🚜", 
                description = f"You sold your crops for {ce1} {ce2} {ce3} {ce4} {ce5} {ce6} {ce7} {ce8} {ce9} {ce10} {ce11} {ce12} {ce13} {ce14} {ce15} 🪙!\nYou earned a total of {coins_earned} 🪙!", 
                color = 0x0097ff
            )
            send = await ctx.send(embed = farm_embed)
            await asyncio.sleep(random.randint(1, 5))
            await send.edit(embed = earned_embed)
            carrot = random.randint(1, 6)
            vege = random.randint(1, 12)
            if carrot == 1:
                carrots_farmed = 1
                carrots = balance[user_id].get("carrots")
                carrots += carrots_farmed
                balance[user_id]["carrots"] = carrots
                save_data("balance.json", balance)
                await asyncio.sleep(0.1)
                carrot_embed = discord.Embed(
                    title = "Wait...",
                    color = 0x0079CC
                )
                carrot_embed.add_field(
                    name = "",
                    value = "A merchant buys something orange from you... 🥕",
                    inline = False
                )
                await ctx.send(embed = carrot_embed)
            if vege == 1:
                veges_earned = 1
                veges = balance[user_id].get("vegetables")
                vegetables += veges_earned
                balance[user_id]["vegetables"] = vegetables
                save_data("balance.json", balance)
                await asyncio.sleep(0.1)
                vege_embed = discord.Embed(
                    title = "Hmmmm...",
                    color = 0x004ecc
                )
                vege_embed.add_field(
                    name = "",
                    value = "A wealthy man buys a bunch of green food from you... 🥬",
                    inline = False
                )
                await ctx.send(embed = vege_embed)
    @farm.error
    async def farm_error(self, ctx, error):
        if isinstance(error, checks.NotStarted):
            need_to_register_embed = error.embed
            await ctx.send(embed=need_to_register_embed)
        elif isinstance(error, commands.CommandOnCooldown):
            cooldown = error.retry_after
            now = int(datetime.datetime.now().timestamp())
            await ctx.send(f"⏱ **| {ctx.author.display_name}:**\n> You are farming too fast!\n > Please try again in <t:{now + int(cooldown)}:R>.", delete_after=cooldown)
            
async def setup(bot):
    await bot.add_cog(Farm(bot))