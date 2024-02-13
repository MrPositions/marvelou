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