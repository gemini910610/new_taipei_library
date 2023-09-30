from discord.ext.commands import Cog, Bot


class Event(Cog):
    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot

    # @Cog.listener()
    # async def EVENT_NAME(self, EVENT_PARAMETER):
    #     ...


async def setup(bot: Bot):
    await bot.add_cog(Event(bot))
