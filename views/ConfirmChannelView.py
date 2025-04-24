import discord
import asyncio

class channelActionConfirm(discord.ui.View):
    def __init__(self, ctx, command, channel):
        self.ctx = ctx 
        self.channel = channel
        self.command = command
        super().__init__()

    @discord.ui.button(label="Yes", style=discord.ButtonStyle.green)
    async def yes_callback(self, interaction, button):
        if interaction.user == self.ctx.author:
            if self.command == "nuke":
                await asyncio.sleep(2)
                new_channel = await self.channel.clone(reason=f"Nuked by {self.ctx.author}")
                await self.channel.delete(reason=f"Nuked by {self.ctx.author}")
                await new_channel.send(f"Nuked! {self.ctx.author.mention}", delete_after = 0.01)
                await new_channel.send(f"Nuked by `{self.ctx.author.name}`")
            elif self.command == "delete":
                await asyncio.sleep(2)
                await self.channel.delete(reason=f"Deleted by {self.ctx.author}")
            button.label = "Yes"
            button.disabled = True
            for child in self.children:
                if isinstance(child, discord.ui.Button) and child != button:
                    child.disabled = True
            try:
                await interaction.response.edit_message(view=self)
            except discord.errors.NotFound:
                pass
        elif interaction.user != self.ctx.author:
            await self.channel.send(f"{self.ctx.author.mention} This is not for you!", delete_after = 3)
            

    @discord.ui.button(label="No", style=discord.ButtonStyle.red)
    async def no_callback(self, interaction, button):
        if interaction.user == self.ctx.author:
            button.label = "No"
            button.disabled = True
            for child in self.children:
                if isinstance(child, discord.ui.Button) and child != button:
                    child.disabled = True
            await self.channel.send("Aborted")
            try: 
                await interaction.response.edit_message(view=self)
            except discord.errors.NotFound:
                print("Channel not found")