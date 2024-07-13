import discord

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
                new_channel = await self.channel.clone()
                await self.channel.delete()
                await new_channel.send(f"Nuked! {self.ctx.author.mention}", delete_after=0.01)
                await new_channel.send(f"Nuked by `{self.ctx.author.name}`")
            elif self.command == "delete":
                await self.channel.delete()
            button.label = "Yes"
            button.disabled = True
            for child in self.children:
                if isinstance(child, discord.ui.Button) and child != button:
                    child.disabled = True
            try:
                await interaction.response.edit_message(view=self)
            except discord.errors.NotFound:
                print("Channel not found")
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
            try: 
                await interaction.response.edit_message(view=self)
            except discord.errors.NotFound:
                print("Channel not found")
