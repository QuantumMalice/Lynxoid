from nextcord.ext import commands
from nextcord import User, Colour, Embed 

class EmbedTool(commands.Cog):
    
    async def prepare_embed(
                            user: User=None,
                            title: str=None,
                            description: str=None,
                            colour: Colour=Colour.green(),
                            ) -> Embed:
        if title == None:
            title = ""
        elif description == None:
            description = ""

        embed = Embed(
            title = title,
            description = description,
            colour = colour
        )

        if not user == None:
            embed.set_author(name=user, icon_url=user.avatar)

        return embed
