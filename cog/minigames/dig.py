import discord
from discord.ext import commands
import json
import os
import random
import asyncio
from helpers import checks
from discord.utils import format_dt
from datetime import datetime, timedelta

class Dig(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @staticmethod
    def load_data(file):
        if not os.path.exists(file):
            with open(file, "w") as f:
                json.dump({}, f)
        with open(file, "r") as f:
            return json.load(f)
    @staticmethod
    def save_data(file, data):
        with open(file, "w") as f:
            json.dump(data, f, indent=4)

    @checks.has_registered()
    @commands.hybrid_command(aliases=["mine"], name="dig", description="Dig for coins in the earth! You may rarely find gems too!")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def dig(self, ctx):
        user_id = str(ctx.message.author.id)
        balance = self.load_data("balance.json")
        if user_id in balance:
            randomn = 0
            randomn = random.randint(1, 1024)
            coins_earned = 0
            if 1 <= randomn <= 2:
                coins_earned = 1000
            elif 3 <= randomn <= 7:
                coins_earned = 500
            elif 8 <= randomn <= 22:
                coins_earned = 200
            elif 23 <= randomn <= 52:
                coins_earned = 100
            elif 53 <= randomn <= 98:
                coins_earned = 95
            elif 99 <= randomn <= 145:
                coins_earned = 90
            elif 146 <= randomn <= 193:
                coins_earned = 85
            elif 194 <= randomn <= 242:
                coins_earned = 80
            elif 243 <= randomn <= 292:
                coins_earned = 75
            elif 293 <= randomn <= 343:
                coins_earned = 70
            elif 344 <= randomn <= 395:
                coins_earned = 65
            elif 396 <= randomn <= 448:
                coins_earned = 60
            elif 449 <= randomn <= 502:
                coins_earned = 55
            elif 503 <= randomn <= 556:
                coins_earned = 50
            elif 557 <= randomn <= 611:
                coins_earned = 45
            elif 612 <= randomn <= 667:
                coins_earned = 40
            elif 668 <= randomn <= 724:
                coins_earned = 35
            elif 725 <= randomn <= 782:
                coins_earned = 30
            elif 783 <= randomn <= 841:
                coins_earned = 25
            elif 842 <= randomn <= 901:
                coins_earned = 20
            elif 902 <= randomn <= 962:
                coins_earned = 15
            elif 963 <= randomn <= 1024:
                coins_earned = 10
            gem = 0
            gem = random.randint(1,10)
            coins = balance[user_id].get("coins")
            coins += coins_earned
            balance[user_id]["coins"] = coins
            self.save_data("balance.json", balance)
            dig_embed = discord.Embed(
                title = "Digging coins...", 
                color=discord.Color.blue()
            )
            earned_embed = discord.Embed(
                title = f"{ctx.author.display_name} went digging!", 
                description = f"You found {coins_earned} 🪙!", 
                color=discord.Color.blue()
            )
            send = await ctx.send(embed = dig_embed)
            await asyncio.sleep(0.1)
            await send.edit(embed = earned_embed)
            if gem == 1:
                gems_earned = 1
                gems = balance[user_id].get("gems")
                gems += gems_earned
                balance[user_id]["gems"] = gems
                self.save_data("balance.json", balance)
                await asyncio.sleep(0.1)
                gem_embed = discord.Embed(
                    title = "Wait a second...",
                    color = discord.Color.blue()
                )
                gem_embed.add_field(
                    name = "You lucky ducky!",
                    value = "You found a gem 💎 ! Added to your balance!",
                    inline = False
                )
                await ctx.send(embed = gem_embed)
    @dig.error
    async def dig_error(self,ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            cooldown = error.retry_after
            cooldown_dt = datetime.utcnow() + timedelta(seconds=cooldown)
            cooldown_timestamp = format_dt(cooldown_dt, style="R")
            await ctx.send(f"⏱ **| {ctx.author.display_name}:**\n> You are digging too fast!\n > Please try again in **{cooldown_timestamp}**.", delete_after=cooldown)
        elif isinstance(error, checks.NotStarted):
            need_to_register_embed = error.embed
            await ctx.send(embed=need_to_register_embed)
                
async def setup(bot):
    await bot.add_cog(Dig(bot))
