import discord
from discord.ext import commands
import random
import json
import datetime
import asyncio
from helpers import checks

class Coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    @checks.has_registered()
    @commands.hybrid_command(aliases=["cf"], name="coinflip", description="Bet your coins and test for your luck!")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def coinflip(self, ctx, amt: int):
        def load_data(file):
            with open(file, "r") as f:
                return json.load(f)
        def save_data(file, data):
            with open(file, "w") as f:
                json.dump(data, f, indent=4)
        user_id = str(ctx.message.author.id)
        balance = load_data("balance.json")
        if user_id in balance:
            coins = balance[user_id].get("coins")
            if amt > coins:
                await ctx.send("You can’t flip more than you have!", delete_after = 3)
            elif amt > 10000:
                await ctx.send("Thats too risky...\n> Try betting less than `10,000`!", delete_after = 3)
            else:
                e = await ctx.send(f"**{ctx.author.display_name}** flips a coin and bets 🪙 **{amt}**...")
                w = random.randint(1,2)
                if w == 1:
                    coins_earned = amt
                    await asyncio.sleep(2)
                    await e.edit(content=f"**{ctx.author.display_name}** fliped a coin and bet 🪙 **{amt}**...\n> ...and ***won*** 🪙 **{amt}**!")
                elif w == 2:
                    coins_earned = -amt
                    await asyncio.sleep(2)
                    await e.edit(content=f"**{ctx.author.display_name}** flips a coin and bet 🪙 **{amt}**...\n> ...and ***loss*** 🪙 **{amt}**...")
                coins += coins_earned
                balance[user_id]["coins"] = coins
                save_data("balance.json", balance)    
    @coinflip.error
    async def coinflip_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            cooldown = error.retry_after
            now = int(datetime.datetime.now().timestamp())
            await ctx.send(f"⏱ **| {ctx.author.display_name}:**\n> You are betting too fast!\n > Please try again in <t:{now + int(cooldown)}:R>.", delete_after=cooldown)
        elif isinstance(error, checks.NotStarted):
            need_to_register_embed = error.embed
            await ctx.send(embed=need_to_register_embed)
            
async def setup(bot):
    await bot.add_cog(Coinflip(bot))