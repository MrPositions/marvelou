import random
def create_user(custom_name, dare1, dare2, dare3):
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
    # Create a dictionary to store user information
    user_info = {
        "name": custom_name,
        "dares": [dare1, dare2, dare3]
    }

    return user_info

# Example usage:
custom_name = "John Doe"
dare1 = "Do a funny dance."
dare2 = "Sing your favorite song loudly."
dare3 = "Tell a joke to a friend."
user_data = create_user(custom_name, dare1, dare2, dare3)
print(f"User Information:\nName: {user_data['name']}\nDares: {user_data['dares']}")
def draw_card():
    cards = {"card1":"dare","card2":"dare","card3":"dare","card4":"iou","card5":"iou","card6":"truth"}
#we need to figure out how to randomly select a card and set it to our chosen card
    chosen_card = random.choice(list(cards.values()))
    return chosen_card
print(draw_card())
def points(user_input):
    """
    Validate the provided number is within the range -10 to +10.

    Parameters:
    - user_input (int): The user-provided number.

    Returns:
    - int: The validated number.
    - None: If the input is not within the valid range.
    """
    if -10 <= user_input <= 10:
        return user_input
    else:
        print("Please provide a number within the valid range.")
        return None

# Example usage:
# You need to provide the number as an argument when calling the function.
# For instance, assuming the user provides the number 5.
user_provided_number = 5
validated_number = points(user_provided_number)

if validated_number is not None:
    print("Selected number:", validated_number)
else:
    print("Number not within the valid range.")