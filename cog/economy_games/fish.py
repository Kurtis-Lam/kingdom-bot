import discord
from discord.ext import commands
import asyncio
import datetime
import random
import json
from helpers import checks

class Fish(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @checks.has_registered()
    @commands.hybrid_command(name="fish", description="Fish for coins and fishes in the sea!")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def fish(self, ctx):
        def load_data(file):
            with open(file, "r") as f:
                return json.load(f)
        def save_data(file, data):
            with open(file, "w") as f:
                json.dump(data, f, indent=4)
        user_id = str(ctx.message.author.id)
        balance = load_data("balance.json")
        if user_id in balance:
            coins_earned = random.randint(50, 150)
            coins = balance[user_id].get("coins")
            coins += coins_earned
            balance[user_id]["coins"] = coins
            save_data("balance.json", balance)
            
            fish_embed = discord.Embed(
                title = "Fishing in the sea... 🎣", 
                color = 0x0097ff
            )
            earned_embed = discord.Embed(
                title = f"{ctx.author.display_name} went fishing! 🎣", 
                description = f"You fished out {coins_earned} 🪙!", 
                color = 0x0097ff
            )
            send = await ctx.send(embed = fish_embed)
            await asyncio.sleep(0.1)
            await send.edit(embed = earned_embed)
            fish = random.randint(1, 12)
            shark = random.randint(1, 24)
            if fish == 1:
                fishes_fished = 1
                fishes = balance[user_id].get("fishes")
                fishes += fishes_fished
                balance[user_id]["fishes"] = fishes
                save_data("balance.json", balance)
                await asyncio.sleep(0.1)
                fishes_embed = discord.Embed(
                    title = "Hold on...",
                    color = 0x0079CC
                )
                fishes_embed.add_field(
                    name = "",
                    value = "You see something wriggling... 🐟",
                    inline = False
                )
                await ctx.send(embed = fishes_embed)
            if shark == 1:
                sharkes_fished = 1
                sharks = balance[user_id].get("sharks")
                sharks += sharkes_fished
                balance[user_id]["sharks"] = sharks
                save_data("balance.json", balance)
                await asyncio.sleep(0.1)
                sharks_embed = discord.Embed(
                    title = "Hold your horses...",
                    color = 0x004ecc
                )
                sharks_embed.add_field(
                    name = "",
                    value = "Something big and huge is looking into your eyes... 🦈",
                    inline = False
                )
                await ctx.send(embed = sharks_embed)
    @fish.error
    async def fish_error(self, ctx, error):
        if isinstance(error, checks.NotStarted):
            need_to_register_embed = error.embed
            await ctx.send(embed=need_to_register_embed)
        elif isinstance(error, commands.CommandOnCooldown):
            cooldown = error.retry_after
            now = int(datetime.datetime.now().timestamp())
            await ctx.send(f"⏱ **| {ctx.author.display_name}:**\n> You are fishing too fast!\n > Please try again in <t:{now + int(cooldown)}:R>.", delete_after=cooldown)
            
async def setup(bot):
    await bot.add_cog(Fish(bot))