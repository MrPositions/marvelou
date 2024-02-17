from interactions import (slash_command, SlashContext,
                          SlashCommand, slash_option,
                          OptionType, SlashCommandChoice)

all_users = []
try:
    all_users = marvelou_functions.load_users(database_filename)
except:
    pass
# Base command
base_command = SlashCommand(
    name="command name",
    description="Commands involving users"
)
@base_command.subcommand()
@slash_option()
async def create_user():

  pass

@base_command.subcommand(sub_cmd_name="create_user", sub_cmd_description="Create a user and registers user in point system")
@slash_option(name="user_name",required=True, description="Name of user", opt_type=OptionType.STRING)
async def create_user(ctx: SlashContext, user_name:str, points:int):
    user = ctx.author  # Get the user who invoked the command
    marvelou_functions.pull_database()
    owner_name = user.username.title()
    owner_discord_id = user.id

    name = user_name
    points = 0