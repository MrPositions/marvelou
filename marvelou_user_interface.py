import marvelou_functions
import interactions
from interactions import (slash_command, SlashContext,
                          SlashCommand, slash_option,
                          OptionType, SlashCommandChoice)
from decouple import config

all_users = []
try:
    database_filename = "marv_data.json"
    all_users = marvelou_functions.load_users(database_filename)
except:
    pass
# Base command
base_command = SlashCommand(
    name="marv",
    description="Commands involving users"
)
@base_command.subcommand(sub_cmd_name="create_user", sub_cmd_description="Create a user and registers user in point system")
@slash_option(name="user_name",required=True, description="Name of user", opt_type=OptionType.STRING)
@slash_option(name="points",required=True, description="Points earned", opt_type=OptionType.INTEGER)
async def create_user(ctx: SlashContext, user_name:str, points:int):
    user = ctx.author  # Get the user who invoked the command
    #marvelou_functions.pull_database()
    owner_name = user.username.title()
    owner_discord_id = user.id

    name = user_name
    points = 0

if __name__ == "__main__":
    bot = interactions.Client(token=config("BOT_TOKEN"))
    bot.start()
    pass