from discord import Intents, Interaction, Activity, ActivityType
from discord.app_commands import AppCommandError
from discord.ext.commands import Bot, Context

intents = Intents.default()
intents.message_content = True
intents.members = True
activity = Activity(name='.help', type=ActivityType.watching)
bot = Bot(command_prefix='.', intents=intents, activity=activity)


@bot.event
async def on_ready():
    print('bot is online')
    await bot.load_extension('cogs.extensions')


@bot.event
async def on_command_error(context: Context, error):
    if hasattr(context.command, 'on_error'):
        return
    await context.send(error)


@bot.tree.error
async def on_app_command_error(interaction: Interaction, error: AppCommandError):
    await interaction.response.send_message(error)


with open('token.txt') as file:
    token = file.read()
bot.run(token)
