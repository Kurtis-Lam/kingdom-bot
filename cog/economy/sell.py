import discord
from discord.ext import commands
import json
from helpers import checks

class Sell(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @checks.has_registered()
    @commands.command()
    async def sell(self, ctx, item: str = None, amt: int = None):
        ITEM_SELL_PRICES = {
            'fish': 20,
            'fishes': 20,
            'shark': 80,
            'sharks': 80,
            'bunny': 20,
            'bunnies': 20,
            'fox': 40,
            'foxes': 40,
            'carrot': 15,
            'carrots': 15,
            'vegetable': 10,
            'vegetables': 10
        }

        if item is None:
            e = discord.Embed(title="", description="", color=0x0097ff)
            e.set_author(name="Pokétwo Kingdom Shop", icon_url=ctx.guild.icon)
            e.add_field(name="Use `.sell {item} {qty = None}` to sell items!", value="", inline=False)
            e.add_field(name="Usage: (Guide)", value="1. Singular and plural forms are both accepted. (e.g. You can use `.sell fish 10` or `.sell fishes 10`)\n2. The {item} you want to sell cannot be neglected, while the {quantity} can. (e.g. Using `.sell shark` will sell 1 shark)", inline=False)
            await ctx.send(embed=e)
            return
        elif item.lower() not in ITEM_SELL_PRICES:
            await ctx.send(f"Item `{item}` is not a valid item!", delete_after=5)
            return

        if amt is None:
            amt = 1
        elif amt < 1:
            await ctx.send("Nice try...", delete_after=3)
            return

        def load_data(file):
            with open(file, "r") as f:
                return json.load(f)

        def save_data(file, data):
            with open(file, "w") as f:
                json.dump(data, f, indent=4)

        user_id = str(ctx.message.author.id)
        balance = load_data("balance.json")
        if user_id in balance:
            fishes = balance[user_id].get("fishes", 0)
            sharks = balance[user_id].get("sharks", 0)
            bunnies = balance[user_id].get("bunnies", 0)
            foxes = balance[user_id].get("foxes", 0)
            carrots = balance[user_id].get("carrots", 0)
            vegetables = balance[user_id].get("vegetables", 0)

            if item in ITEM_SELL_PRICES:
                total_value = ITEM_SELL_PRICES[item.lower()] * amt
                if item in ['fish', 'fishes']:
                    if fishes < amt:
                        await ctx.send(f"You do not have enough 🐟 to sell **{amt} fish(es)**! You only have **{fishes}** 🐟.")
                        return
                    else:
                        fishes -= amt
                elif item in ['shark', 'sharks']:
                    if sharks < amt:
                        await ctx.send(f"You do not have enough 🦈 to sell **{amt} shark(s)**! You only have **{sharks}** 🦈.")
                        return
                    else:
                        sharks -= amt
                elif item in ['bunny', 'bunnies']:
                    if bunnies < amt:
                        await ctx.send(f"You do not have enough 🐰 to sell **{amt} bunny(ies)**! You only have **{bunnies}** 🐰.")
                        return
                    else:
                        bunnies -= amt
                elif item in ['fox', 'foxes']:
                    if foxes < amt:
                        await ctx.send(f"You do not have enough 🦊 to sell **{amt} fox(es)**! You only have **{foxes}** 🦊.")
                        return
                    else:
                        foxes -= amt
                elif item in ['carrot', 'carrots']:
                    if carrots < amt:
                        await ctx.send(f"You do not have enough 🥕 to sell **{amt} carrot(s)**! You only have **{carrots}** 🥕.")
                        return
                    else:
                        carrots -= amt
                elif item in ['vegetable', 'vegetables']:
                    if vegetables < amt:
                        await ctx.send(f"You do not have enough 🥬 to sell **{amt} vegetable(s)**! You only have **{vegetables}** 🥬.")
                        return
                    else:
                        vegetables -= amt

                await ctx.send(f"You have successfully sold **{amt} {item}(s)** for **{total_value}** 🪙!")
                
        balance[user_id]["fishes"] = fishes
        balance[user_id]["sharks"] = sharks
        balance[user_id]["bunnies"] = bunnies
        balance[user_id]["foxes"] = foxes
        balance[user_id]["carrots"] = carrots
        balance[user_id]["vegetables"] = vegetables
        balance[user_id]["coins"] = balance[user_id].get("coins", 0) + total_value
        save_data("balance.json", balance)

    @sell.error
    async def sell_error(self, ctx, error):
        if isinstance(error, checks.NotStarted):
            need_to_register_embed = error.embed
            await ctx.send(embed=need_to_register_embed)

async def setup(bot):
    await bot.add_cog(Sell(bot))