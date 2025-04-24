import discord

class PingView(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx 
        self.cog = self.ctx.bot.get_cog('FPing')
        super().__init__()

    @discord.ui.button(label="24/7 ping", style=discord.ButtonStyle.green)
    async def ping_callback(self, interaction, button):
        if interaction.user == self.ctx.author:
            if self.ctx.cog.editing:
                await self.ctx.send(
                    f"Updating of the bot's latency is already in progress."
                    f"{self.cog.current_message.jump_url}"
                )
                return
            self.cog.editing = True
            self.cog.current_channel = self.ctx.channel
            message = await self.ctx.send('Pong!')
            self.cog.current_message = message
            self.cog.task = self.ctx.bot.loop.create_task(self.cog.update_latency(message))
            button.label = "Started!"
            button.disabled = True
            await interaction.response.edit_message(view=self)