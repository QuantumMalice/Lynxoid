from nextcord import Game, Status
from nextcord.ext import commands

class __Init__(commands.Cog, name="Init"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        activity = Game(name="/help", type=3)
        await self.bot.change_presence(status=Status.online, activity=activity)

        print("Lynxiod is alive!")

def setup(bot):
    bot.add_cog(__Init__(bot))
