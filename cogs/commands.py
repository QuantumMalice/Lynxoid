from nextcord.ext import commands

class Commands(commands.Cog, name="Commands"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Commands(bot))