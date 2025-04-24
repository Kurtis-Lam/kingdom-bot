import discord
from discord.ext import commands
import asyncio
import datetime
import random
import json
from helpers import checks

class Dig(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.hybrid_command(aliases=["di"], name="diginfo", description="Views the chances of getting different amount of coins from .dig")
    async def diginfo(self, ctx):
        e = discord.Embed(title="Below are the chances for the amount of coins you can get from `.dig`", color = 0x0097ff)
        e.add_field(name="", value = "**10,000**: 1/2048\n**5,000**: 1/1024\n**1,000**: 1/512\n**500**: 1/256\n**300**: 1/128\n**200**: 1/64\n**100**: 1/32\n For the others, they range from 45/1024 ~ 61/1024", inline = False)
        await ctx.send(embed = e)
        
    @checks.has_registered()
    @commands.hybrid_command(name="dig", description="Dig for coins in the earth!")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def dig(self, ctx):
        def load_data(file):
            with open(file, "r") as f:
                return json.load(f)
        def save_data(file, data):
            with open(file, "w") as f:
                json.dump(data, f, indent=4)
        user_id = str(ctx.message.author.id)
        balance = load_data("balance.json")
        if user_id in balance:
            randomn = 0
            randomn = random.randint(1, 2048)
            coins_earned = 0
            if randomn == 1:
                coins_earned = 10000
            elif 2 <= randomn <= 3:
                coins_earned = 5000
            elif 4 <= randomn <= 7:
                coins_earned = 1000
            elif 8 <= randomn <= 15:
                coins_earned = 500
            elif 16 <= randomn <= 31:
                coins_earned = 300
            elif 32 <= randomn <= 63:
                coins_earned = 200
            elif 64 <= randomn <= 127:
                coins_earned = 100
            elif 128 <= randomn <= 217:
                coins_earned = 95
            elif 218 <= randomn <= 309:
                coins_earned = 90
            elif 310 <= randomn <= 403:
                coins_earned = 85
            elif 404 <= randomn <= 499:
                coins_earned = 80
            elif 500 <= randomn <= 597:
                coins_earned = 75
            elif 598 <= randomn <= 698:
                coins_earned = 70
            elif 699 <= randomn <= 801:
                coins_earned = 65
            elif 802 <= randomn <= 906:
                coins_earned = 60
            elif 907 <= randomn <= 1013:
                coins_earned = 55
            elif 1014 <= randomn <= 1120:
                coins_earned = 50
            elif 1121 <= randomn <= 1229:
                coins_earned = 45
            elif 1230 <= randomn <= 1340:
                coins_earned = 40
            elif 1341 <= randomn <= 1453:
                coins_earned = 35
            elif 1454 <= randomn <= 1568:
                coins_earned = 30
            elif 1569 <= randomn <= 1685:
                coins_earned = 25
            elif 1686 <= randomn <= 1804:
                coins_earned = 20
            elif 1805 <= randomn <= 1925:
                coins_earned = 15
            elif 1926 <= randomn <= 2048:
                coins_earned = 10
            gem = 0
            gem = random.randint(1,10)
            coins = balance[user_id].get("coins")
            coins += coins_earned
            balance[user_id]["coins"] = coins
            save_data("balance.json", balance)
            dig_embed = discord.Embed(
                title = "Digging coins... 🌱", 
                color = 0x0097ff
            )
            earned_embed = discord.Embed(
                title = f"{ctx.author.display_name} went digging! 🌱", 
                description = f"You dug {coins_earned} 🪙!", 
                color = 0x0097ff
            )
            send = await ctx.send(embed = dig_embed)
            await asyncio.sleep(0.1)
            await send.edit(embed = earned_embed)
            if gem == 1:
                gems_earned = 1
                gems = balance[user_id].get("gems")
                gems += gems_earned
                balance[user_id]["gems"] = gems
                save_data("balance.json", balance)
                await asyncio.sleep(0.1)
                gem_embed = discord.Embed(
                    title = "Wait a second...",
                    color = 0x0079CC
                )
                gem_embed.add_field(
                    name = "",
                    value = "You find something blue and shiny... 💎",
                    inline = False
                )
                await ctx.send(embed = gem_embed)
    @dig.error
    async def dig_error(self, ctx, error):
        if isinstance(error, checks.NotStarted):
            need_to_register_embed = error.embed
            await ctx.send(embed=need_to_register_embed)
        elif isinstance(error, commands.CommandOnCooldown):
            cooldown = error.retry_after
            now = int(datetime.datetime.now().timestamp())
            await ctx.send(f"⏱ **| {ctx.author.display_name}:**\n> You are digging too fast!\n > Please try again in <t:{now + int(cooldown)}:R>.", delete_after=cooldown)
            
async def setup(bot):
    await bot.add_cog(Dig(bot))