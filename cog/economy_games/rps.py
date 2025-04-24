import discord
from discord.ext import commands
import json
import os
import random
import asyncio
from helpers import checks
import datetime

class choose(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        self.user_choice = None
        super().__init__()

    @discord.ui.button(label="Rock", style=discord.ButtonStyle.green, emoji="🪨")
    async def rock_choice(self, interaction, button):
        if interaction.user == self.ctx.author:
            self.user_choice = "rock"
            button.label = "Rock"
            button.disabled = True
            button.style = discord.ButtonStyle.grey
            for child in self.children:
                if isinstance(child, discord.ui.Button) and child != button:
                    child.disabled = True
            await interaction.response.edit_message(content='', view=self)
            self.stop()

    @discord.ui.button(label="Paper", style=discord.ButtonStyle.green, emoji="📄")
    async def paper_choice(self, interaction, button):
        if interaction.user == self.ctx.author:
            self.user_choice = "paper"
            button.label = "Paper"
            button.disabled = True
            button.style = discord.ButtonStyle.grey
            for child in self.children:
                if isinstance(child, discord.ui.Button) and child != button:
                    child.disabled = True
            await interaction.response.edit_message(content='', view=self)
            self.stop()

    @discord.ui.button(label="Scissors", style=discord.ButtonStyle.green, emoji="✂️")
    async def scissors_choice(self, interaction, button):
        if interaction.user == self.ctx.author:
            self.user_choice = "scissors"
            button.label = "Scissors"
            button.disabled = True
            button.style = discord.ButtonStyle.grey
            for child in self.children:
                if isinstance(child, discord.ui.Button) and child != button:
                    child.disabled = True
            await interaction.response.edit_message(content='', view=self)
            self.stop()
          
        
class RockPaperScissors(commands.Cog):
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
      
    def checkrps(self, ctx, bots_choice, users_choice):
        balance = self.load_data("balance.json")
        user_id = str(ctx.message.author.id)
        winCases = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
        if bots_choice == users_choice:
            coins_earned = 200
            coins = balance[user_id].get("coins")
            coins += coins_earned
            balance[user_id]["coins"] = coins
            self.save_data("balance.json", balance)
            user_choice = users_choice.lower()
            bot_choice = bots_choice.lower()
            return "Rock Paper Scissors", f"Your choice: {user_choice}", f"Bot's choice: {bot_choice}", f"Result: We tied!", f"You got {coins_earned} 🪙 ! GG, play again! ", discord.Color.light_grey()
        elif winCases[users_choice] == bots_choice:
            coins_earned = 300
            coins = balance[user_id].get("coins")
            coins += coins_earned
            balance[user_id]["coins"] = coins
            self.save_data("balance.json", balance)
            user_choice = users_choice.lower()
            bot_choice = bots_choice.lower()
            return "Rock Paper Scissors", f"Your choice: {user_choice}", f"Bot's choice: {bot_choice}", f"Result: You won!", f"You got {coins_earned} 🪙 ! Well done! ", discord.Color.green()
        else:
            coins_earned = 100
            coins = balance[user_id].get("coins")
            coins += coins_earned
            balance[user_id]["coins"] = coins
            self.save_data("balance.json", balance)
            user_choice = users_choice.lower()
            bot_choice = bots_choice.lower()
            return "Rock Paper Scissors", f"Your choice: {user_choice}", f"Bot's choice: {bot_choice}", f"Result: You lost!", f"You got {coins_earned} 🪙 ... No worries, try again and you might beat me!", discord.Color.red()

    @checks.has_registered()
    @commands.hybrid_command(aliases=["rockpaperscissors"], name="rps", description="Play famous game: \"Rock, Paper, Scissors\" with the bot!")
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def rps(self, ctx):
        user_id = str(ctx.message.author.id)
        balance = self.load_data("balance.json")
        if user_id in balance:
            options = ["rock", "paper", "scissors"]
            ask_rps_em = discord.Embed(title="Rock, Paper or Scissors?", color = 0x0097ff)
            view = choose(ctx)
            message = await ctx.send(embed=ask_rps_em, view=view)
            await view.wait()
            user_choice = view.user_choice if view.user_choice else "No choice made"
            bot_choice = random.choice(options)
            test = self.checkrps(ctx, bot_choice, user_choice)
            result_em = discord.Embed(title = test[0], description = test [4], color = test[5])
            result_em.add_field(name = test[3], value = f"{test[2]}\n{test[1]}", inline = False)
            await ctx.send(embed=result_em)

    @rps.error
    async def rps_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            cooldown = error.retry_after
            now = int(datetime.datetime.now().timestamp())
            await ctx.send(f"⏱ **| {ctx.author.display_name}:**\n> You are playing too fast!\n > Please try again in <t:{now + int(cooldown)}:R>.", delete_after=cooldown)
        elif isinstance(error, checks.NotStarted):
            need_to_register_embed = error.embed
            await ctx.send(embed=need_to_register_embed)

async def setup(bot):
    await bot.add_cog(RockPaperScissors(bot))