import discord
from discord.ext import commands
import asyncio
import datetime
import random
import json
from helpers import checks

class Hunt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @checks.has_registered()
    @commands.hybrid_command(name="hunt", description="Hunt for coins and bunnies in the forest!")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def hunt(self, ctx):
        def load_data(file):
            with open(file, "r") as f:
                return json.load(f)
        def save_data(file, data):
            with open(file, "w") as f:
                json.dump(data, f, indent=4)
        user_id = str(ctx.message.author.id)
        balance = load_data("balance.json")
        if user_id in balance:
            coins_earned = random.randint(1, 200)
            coins = balance[user_id].get("coins")
            coins += coins_earned
            balance[user_id]["coins"] = coins
            save_data("balance.json", balance)
            
            hunt_embed = discord.Embed(
                title = "Hunting in the woods... 🏹", 
                color = 0x0097ff
            )
            earned_embed = discord.Embed(
                title = f"{ctx.author.display_name} went hunting! 🏹", 
                description = f"You hunted {coins_earned} 🪙!", 
                color = 0x0097ff
            )
            send = await ctx.send(embed = hunt_embed)
            await asyncio.sleep(0.1)
            await send.edit(embed = earned_embed)
            bunny = random.randint(1, 8)
            fox = random.randint(1, 16)
            if bunny == 1:
                bunnies_hunted = 1
                bunnies = balance[user_id].get("bunnies")
                bunnies += bunnies_hunted
                balance[user_id]["bunnies"] = bunnies
                save_data("balance.json", balance)
                await asyncio.sleep(0.1)
                bunnies_embed = discord.Embed(
                    title = "Hey, look...",
                    color = 0x0079CC
                )
                bunnies_embed.add_field(
                    name = "",
                    value = "You see two fuffly ears sticking out your bag... 🐰",
                    inline = False
                )
                await ctx.send(embed = bunnies_embed)
            if fox == 1:
                foxes_hunted = 1
                foxes = balance[user_id].get("foxes")
                foxes += foxes_hunted
                balance[user_id]["foxes"] = foxes
                save_data("balance.json", balance)
                await asyncio.sleep(0.1)
                foxes_embed = discord.Embed(
                    title = "AYO WHAT?",
                    color = 0x004ecc
                )
                foxes_embed.add_field(
                    name = "",
                    value = "You got a brown furry animal... 🦊",
                    inline = False
                )
                await ctx.send(embed = foxes_embed)
    @hunt.error
    async def hunt_error(self, ctx, error):
        if isinstance(error, checks.NotStarted):
            need_to_register_embed = error.embed
            await ctx.send(embed=need_to_register_embed)
        elif isinstance(error, commands.CommandOnCooldown):
            cooldown = error.retry_after
            now = int(datetime.datetime.now().timestamp())
            await ctx.send(f"⏱ **| {ctx.author.display_name}:**\n> You are hunting too fast!\n > Please try again in <t:{now + int(cooldown)}:R>.", delete_after=cooldown)
            
async def setup(bot):
    await bot.add_cog(Hunt(bot))