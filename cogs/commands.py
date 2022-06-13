import os, nextcord
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
        botUser = bot.users[0]
        botPing = round(bot.latency * 1000)
        embed = await EmbedTool.prepare_embed(botUser, None, f"> ***Ping:*** **`{botPing}ms`**\n", Colour.yellow())
        await interaction.response.send_message(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Commands(bot))