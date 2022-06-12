# Import library
import os
from nextcord import Intents
from nextcord.ext import commands

# Import/Load variables from .env
from dotenv import load_dotenv
load_dotenv()

# Initialize bot parameters
bot = commands.Bot(
    command_prefix=os.getenv('PREFIX'),
    intents=Intents().all()
)

# Main Class
class Main():
    
    def bootup():

        # Load every existing cog
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[0:-3]}')

        # Grab token and run bot
        bot.run(os.getenv('TOKEN'))

# Execute
Main.bootup()
