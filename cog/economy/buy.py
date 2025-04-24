import discord
from discord.ext import commands
import json
from helpers import checks

class Buy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @checks.has_registered()
    @commands.command()
    async def buy(self, ctx, item: str= None, amt: int= None):
        COIN_ITEM_PRICES = {
            'gem': 500,
            'gems': 500,
            'lifesaver': 1500,
            'lifesavers': 1500
        }
        GEM_ITEM_PRICES = {
            'ruby': 50,
            'rubies': 50,
            'raffle-ticket': 10,
            'raffle-tickets': 10,
            'redeem-spawn-hint': 15
        }
        if item is None:
            e = discord.Embed(title="", description="", color=0x0097ff)
            e.set_author(name="Pokétwo Kingdom Shop", icon_url=ctx.guild.icon)
            e.add_field(name="Use `.buy {item} {qty = None}` to buy items!", value="", inline=False)
            e.add_field(name="Usage: (Guide)", value="1. Singular and Pural form are both accepted. (e.g. You can use `.buy gem 10` or `.buy gems 10`)\n2. Replace ALL the spaces with a hyphen: \"-\", and replace ALL UPPERCASES to lowercases. (e.g. You can use `.buy redeem-spawn-hint 1` to buy a Redeem Spawn Hint)\n3. The {item} you want to buy cannot be neglected, while the {quantity} can. (e.g. Using `.buy ruby` will buy 1 ruby)", inline=False)
            await ctx.send(embed = e)
            return
        elif item.lower() not in COIN_ITEM_PRICES:
            if item.lower() not in GEM_ITEM_PRICES:
                await ctx.send(f"Item `{item}` is not a valid item!", delete_after = 5)
                return
        
        if amt is None:
            amt = 1
        elif amt < 1:
            await ctx.send("Nice try...", delete_after = 3)
            
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
            gems = balance[user_id].get("gems")
            rubies = balance[user_id].get("rubies")
            lifesavers = balance[user_id].get("lifesavers")
            if item in COIN_ITEM_PRICES:
                total_cost = COIN_ITEM_PRICES[item.lower()] * amt
                if item == "gem" or item == "gems":
                    if coins < total_cost:
                        await ctx.send(f"You do not have enough 🪙 to buy **{amt}  gem(s) 💎**! You need to have at least **{total_cost}** 🪙!")
                        return
                    else:
                        coins -= total_cost
                        gems += amt
                        await ctx.send(f"You have successfully bought **{amt} gem(s) 💎** for **{total_cost}** 🪙s!")
                if item == "lifesaver" or item == "lifesavers":
                    if coins < total_cost:
                        await ctx.send(f"You do not have enough 🪙 to buy **{amt}  lifesaver(s) 🛟**! You need to have at least **{total_cost}** 🪙!")
                        return
                    else:
                        coins -= total_cost
                        lifesavers += amt
                        await ctx.send(f"You have successfully bought **{amt} lifesaver(s) 🛟** for **{total_cost}** 🪙s!")
            if item in GEM_ITEM_PRICES:
                total_cost = GEM_ITEM_PRICES[item.lower()] * amt
                if item == "ruby" or item == "rubies":
                    if gems < total_cost:
                        await ctx.send(f"You do not have enough 💎 to buy **{amt} ruby(ies) <:ruby:1312617052950888538>**! You need to have at least **{total_cost}** 💎!")
                        return
                    else: 
                        gems -= total_cost
                        rubies += amt
                        await ctx.send(f"You have successfully bought **{amt} ruby(ies) <:ruby:1312617052950888538>** for **{total_cost}** 💎!")
                    
        balance[user_id]["coins"] = coins
        balance[user_id]["gems"] = gems
        balance[user_id]["rubies"] = rubies
        balance[user_id]["lifesavers"] = lifesavers
        save_data("balance.json", balance)
    @buy.error
    async def buy_error(self, ctx, error):
        if isinstance(error, checks.NotStarted):
            need_to_register_embed = error.embed
            await ctx.send(embed=need_to_register_embed)
            
async def setup(bot):
    await bot.add_cog(Buy(bot))