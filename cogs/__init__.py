from nextcord.ext import commands

class __Init__(commands.Cog, name="Init"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Lynxiod is alive!")

def setup(bot):
    bot.add_cog(__Init__(bot))
