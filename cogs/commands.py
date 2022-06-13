import nextcord
from nextcord import Colour, slash_command
from nextcord.ext import commands
from tools.embeds import *


class Commands(commands.Cog, name="Commands"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # [Ping]: Bot Latency
    @slash_command(name='ping', description='Return a message with bot latency', guild_ids=[])
    async def ping(self, interaction: nextcord.Interaction):
        bot = self.bot
        botPing = round(bot.latency * 1000)
        embed = Embed(
            title = "",
            description = f"> ***Latency:*** **`{botPing}ms`**\n",
            colour = Colour.yellow()
        )
        embed.set_author(name=bot.users[0], icon_url=bot.users[0].avatar)
        await interaction.response.send_message(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Commands(bot))