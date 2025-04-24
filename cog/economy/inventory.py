import discord
from discord.ext import commands
import json
from helpers import checks

class Inventory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @checks.has_registered()
    @commands.hybrid_command(aliases=["inv"], name="inventory", description="Checks your inventory!")
    async def inventory(self, ctx, user: discord.Member = None):
        def load_data(file):
            with open(file, "r") as f:
                return json.load(f)
            
        if user is not None and ctx.author.guild_permissions.administrator:
            user_id = str(user.id)
            inventory = load_data("balance.json")
            if user_id in inventory:
                lifesavers = inventory[user_id].get("lifesavers", 0)
                fishes = inventory[user_id].get("fishes", 0)
                sharks = inventory[user_id].get("sharks", 0)
                bunnies = inventory[user_id].get("bunnies", 0)
                foxes = inventory[user_id].get("foxes", 0)
                carrots = inventory[user_id].get("carrots", 0)
                vegetables = inventory[user_id].get("vegetables", 0)

                inventory_embed = discord.Embed(
                    title=f"{user.display_name}'s Inventory",
                    color=0x0097ff
                )
                inventory_embed.add_field(name="Lifesavers", value=f"{lifesavers:,} 🛟", inline=False)
                inventory_embed.add_field(name="Fishes", value=f"{fishes:,} 🐟", inline=False)
                inventory_embed.add_field(name="Sharks", value=f"{sharks:,} 🦈", inline=False)
                inventory_embed.add_field(name="Bunnies", value=f"{bunnies:,} 🐰", inline=False)
                inventory_embed.add_field(name="Foxes", value=f"{foxes:,} 🦊", inline=False)
                inventory_embed.add_field(name="Carrots", value=f"{carrots:,} 🥕", inline=False)
                inventory_embed.add_field(name="Vegetables", value=f"{vegetables:,} 🥬", inline=False)
                inventory_embed.set_thumbnail(url=ctx.author.display_avatar.url)

                await ctx.send(embed=inventory_embed)
        else:
            user_id = str(ctx.message.author.id)
            inventory = load_data("balance.json")
            if user_id in inventory:
                lifesavers = inventory[user_id].get("lifesavers", 0)
                fishes = inventory[user_id].get("fishes", 0)
                sharks = inventory[user_id].get("sharks", 0)
                bunnies = inventory[user_id].get("bunnies", 0)
                foxes = inventory[user_id].get("foxes", 0)
                carrots = inventory[user_id].get("carrots", 0)
                vegetables = inventory[user_id].get("vegetables", 0)

                inventory_embed = discord.Embed(
                    title=f"{ctx.author.display_name}'s Inventory",
                    color=0x0097ff
                )
                inventory_embed.add_field(name="Lifesavers", value=f"{lifesavers:,} 🛟", inline=False)
                inventory_embed.add_field(name="Fishes", value=f"{fishes:,} 🐟", inline=False)
                inventory_embed.add_field(name="Sharks", value=f"{sharks:,} 🦈", inline=False)
                inventory_embed.add_field(name="Bunnies", value=f"{bunnies:,} 🐰", inline=False)
                inventory_embed.add_field(name="Foxes", value=f"{foxes:,} 🦊", inline=False)
                inventory_embed.add_field(name="Carrots", value=f"{carrots:,} 🥕", inline=False)
                inventory_embed.add_field(name="Vegetables", value=f"{vegetables:,} 🥬", inline=False)
                inventory_embed.set_thumbnail(url=ctx.author.display_avatar.url)

                await ctx.send(embed=inventory_embed)

    @inventory.error
    async def inventory_error(self, ctx, error):
        if isinstance(error, checks.NotStarted):
            need_to_register_embed = error.embed
            await ctx.send(embed=need_to_register_embed)

async def setup(bot):
    await bot.add_cog(Inventory(bot))