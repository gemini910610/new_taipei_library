from discord import Embed, SelectOption, Interaction
from discord.ext.commands import Cog, Bot, Context, command
from library import Library
from discord.ui import View, Select

class FruitSelectView(View):
    def __init__(self, library):
        super().__init__()
        self.library = library
        options = []
        libraries = self.library.get_libraries()
        for value in libraries:
            option = SelectOption(label=value, value = value)
            options.append(option)
        self.menu = Select(placeholder='請選擇要查詢的分館', options=options)
        self.add_item(self.menu)
        self.menu.callback = self.callback
    async def callback(self, interaction: Interaction):
        library = self.menu.values[0]
        channel = interaction.channel
        await interaction.response.defer()
        await self.search(channel, library)
    async def search(self, channel, library):
        message = await channel.send('搜尋中...')
        area_dict = self.library.get_areas(library)
        area_list = area_dict[library]
        embed = Embed(title=library, color=0x5fc3ff)
        for area in area_list:
            embed.add_field(name=area.name, value=f'{area.free}/{area.total}')
        await message.delete()
        await channel.send(embeds=[embed])

class Command(Cog):
    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot
        self.library = Library()

    # @command()
    # async def COMMAND_NAME(self, context: Context):
    #     await context.send(...)

    @command()
    async def cls(self, context: Context, max_count: int = 1):
        await context.channel.purge(limit=max_count + 1)

    @command()
    async def area(self, context: Context):
        view = FruitSelectView(self.library)
        await context.send(view=view)

async def setup(bot: Bot):
    await bot.add_cog(Command(bot))
