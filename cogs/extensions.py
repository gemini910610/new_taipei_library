from discord.ext.commands import Bot, Cog, command, Context
from discord.ext.commands.errors import (
    ExtensionNotFound,
    ExtensionNotLoaded,
    ExtensionAlreadyLoaded,
)


class Extension(Cog):
    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot

    @command()
    async def load(self, context: Context, extension: str):
        try:
            await self.bot.load_extension(f'cogs.{extension}')
            await context.send(f'load `{extension}` success')
        except ExtensionNotFound:
            await context.send(f'extension `{extension}` not found')
        except ExtensionAlreadyLoaded:
            await context.send(f'extension `{extension}` already loaded')

    @command()
    async def unload(self, context: Context, extension: str):
        try:
            await self.bot.unload_extension(f'cogs.{extension}')
            await context.send(f'unload `{extension}` success')
        except ExtensionNotLoaded:
            await context.send(f'extension `{extension}` not loaded')

    @command()
    async def reload(self, context: Context, extension: str):
        try:
            await self.bot.reload_extension(f'cogs.{extension}')
            await context.send(f'reload `{extension}` success')
        except ExtensionNotLoaded:
            await context.send(f'extension `{extension}` not loaded')

    @command()
    async def sync(self, context: Context):
        command = await self.bot.tree.sync()
        await context.send(f'sync `{len(command)}` commands')


async def setup(bot: Bot):
    await bot.add_cog(Extension(bot))
