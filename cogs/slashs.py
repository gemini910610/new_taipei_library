from discord.ext.commands import Cog, Bot
from discord import Interaction
from discord.app_commands import command


class Slash(Cog):
    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot

    # @app_commands.command()
    # async def SLASH_COMMAND_NAME(self, interaction: Interaction):
    #     await interaction.response.send_message(...)


async def setup(bot: Bot):
    await bot.add_cog(Slash(bot))
