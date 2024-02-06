import random

def create_user(owner_name,owner_discord_id, custom_name, dare1, dare2, dare3):
    """
    Create a user with a custom name and three dares.

    Parameters:
    - custom_name (str): The custom name of the user.
    - dare1 (str): The first dare.
    - dare2 (str): The second dare.
    - dare3 (str): The third dare.

    Returns:
    - dict: A dictionary containing user information.
    """

    user_info = {
        "owner_name": owner_name
        "owner_discord_id" : owner_discord_id,
        "name": custom_name,
        "dares": [dare1, dare2, dare3],
        "points": 0  # Initialize points to 0 for the user
    }

    return user_info

# Example usage:
custom_name = "John Doe"
dare1 = "Kat"
dare2 = "Rasp"
dare3 = "Grey"
user_data = create_user(custom_name, dare1, dare2, dare3)
print(f"User Information:\nName: {user_data['name']}\nDares: {user_data['dares']}\nPoints: {user_data['points']}")

def draw_card():
    cards = {"card1": "dare", "card2": "dare", "card3": "dare", "card4": "iou", "card5": "command1", "card6": "command2", "card7": "command3"}
    # Randomly select a card
    chosen_card = random.choice(list(cards.values()))
    return chosen_card

# Example usage:
selected_card = draw_card()
print(f"Selected card: {selected_card}")
def random_user(all_users):
    return random.choice(all_users)
def earn_points(user, points):
    """
    Earn points for a user.

    Parameters:
    - user (dict): The user dictionary containing information.
    - points (int): Points to be earned.

    Returns:
    - int: Updated points for the user.
    """
    if -10 <= points <= 10:
        return points
    else:
        print("Please provide a number within the valid range.")
        return None
    user['points'] += points
    return user['points']

# Example usage:
points_earned = 12
user_data['points'] = earn_points(user_data, points_earned)
print(f"Updated points for {user_data['name']}: {user_data['points']}")

# List to store all users
all_users = [user_data]
# Example usage of random_user function
randomly_chosen_user = random_user(all_users)
print(f"Randomly chosen user: {randomly_chosen_user['name']}")

def read_user_by_discord_id(users,owner_discord_id):
    # logic for how to find user info here
    result_user = []
    for user in users:
        if user['owner_discord_id'] == owner_discord_id:
            result_user.append(user)
    pass