from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)
TOKEN = os.getenv('TOKEN')


class SYSTEM(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='S',
            help_command=None
        )

    async def on_ready(self):
        print(f'{str(self.user)} on Ready.')


SYSTEM().run(TOKEN)