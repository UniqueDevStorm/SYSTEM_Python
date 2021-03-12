from discord.ext import commands

from utils.autocogs import AutoCogs

from dotenv import load_dotenv
import os

load_dotenv(verbose=True)
TOKEN = os.getenv('TOKEN')


class SYSTEM(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='../',
            help_command=None
        )
        AutoCogs(self)

    async def on_ready(self):
        print(f'{str(self.user)} on Ready.')


SYSTEM().run(TOKEN)