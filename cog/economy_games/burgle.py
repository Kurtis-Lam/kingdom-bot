import discord
from discord.ext import commands
import asyncio
import datetime
import random
import json
from helpers import checks

class Burgle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @checks.has_registered()
    @commands.hybrid_command(name="burgle", description="Burgle some coins bank!")
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def burgle(self, ctx):
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
            randomn = random.randint(1, 16)
            coins_earned = 0
            if randomn == 1:
                coins_earned = 500
            elif 2 <= randomn <= 3:
                coins_earned = 400
            elif 4 <= randomn <= 6:
                coins_earned = 300
            elif 7 <= randomn <= 10:
                coins_earned = 200
            elif 11 <= randomn <= 16:
                coins_earned = 100
            rubies = 0
            rubies = random.randint(1, 50)
            coins = balance[user_id].get("coins")
            coins += coins_earned
            balance[user_id]["coins"] = coins
            save_data("balance.json", balance)
            burgle_embed = discord.Embed(
                title = "Burgling from a random bank... 🥷🥷🥷", 
                color = 0x0097ff
            )
            earned_embed = discord.Embed(
                title = f"{ctx.author.display_name} went burgling! 🥷🥷🥷", 
                description = f"You stole {coins_earned} 🪙!", 
                color = 0x0097ff
            )
            send = await ctx.send(embed = burgle_embed)
            await asyncio.sleep(0.1)
            await send.edit(embed = earned_embed)
            if rubies == 1:
                rubies_earned = 1
                rubies = balance[user_id].get("rubies")
                rubies += rubies_earned
                balance[user_id]["rubies"] = rubies
                save_data("balance.json", balance)
                await asyncio.sleep(0.1)
                ruby_embed = discord.Embed(
                    title = "WAIT WHAT???",
                    color = 0xd90e39
                )
                ruby_embed.add_field(
                    name = "",
                    value = "Something red is GLEAMING in your bag... <:ruby:1312617052950888538>",
                    inline = False
                )
                await ctx.send(embed = ruby_embed)
    @burgle.error
    async def burgle_error(self, ctx, error):
        if isinstance(error, checks.NotStarted):
            need_to_register_embed = error.embed
            await ctx.send(embed=need_to_register_embed)
        elif isinstance(error, commands.CommandOnCooldown):
            cooldown = error.retry_after
            now = int(datetime.datetime.now().timestamp())
            await ctx.send(f"⏱ **| {ctx.author.display_name}:**\n> You are burgling too fast!\n > Please try again in <t:{now + int(cooldown)}:R>.", delete_after=cooldown)
            
async def setup(bot):
    await bot.add_cog(Burgle(bot))