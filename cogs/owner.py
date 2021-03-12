from discord.ext import commands
from discord.ext.commands import AutoShardedBot
from discord.ext.commands.context import Context

from utils.autocogs import AutoCogsReload


class Owner(commands.Cog):
    def __init__(self, bot: AutoShardedBot):
        self.bot = bot

    @commands.command(aliases=['r', '리로드'])
    @commands.is_owner()
    async def reload(self, ctx: Context):
        try:
            AutoCogsReload(self.bot)
        except Exception as e:
            return await ctx.reply(f'리로드 중 오류가 발생하였습니다. [{e}]')
        return await ctx.reply('정상적으로 리로드 되었습니다.')


def setup(bot: AutoShardedBot):
    bot.add_cog(Owner(bot))