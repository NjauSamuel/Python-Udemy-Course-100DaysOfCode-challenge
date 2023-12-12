from art import logo
from game_data import data
from art import vs
import random

# print(logo)

"""
first we'll print the logo

Then we need to ask a user the first question and compare it to the second question
Above then what is required is to display the data in the dictionaries to each other, e.g NBA from United States has X followers and is a basketball competition, what about camila cabellow from Cuba who is a musician?

While the given answer after comparison above is true, we

The comparison will begin by comparing the values inside of the items in the list first and then later just 
asking the question and then displaying the answer. 

# If indeed the user haas chosen a great choice between higher or lower, the user should then be greeted with the next 
round for the game, in this next round, the user can have 
"""


# Attempt to ask a question and then display the answer:

# Which of the following is greater,

# {Rihana} whi is {a mucisian} from {connecticut} with {followers}

# Or {Neymar} who is a {football player } from {Brazil}

# The choices from the two code pieces above is either higher or lower


# data
# i = 0
# print(f"{data[i]['name']} a {data[i]['description']} from {data[i]['country']} with {data[i]['follower_count']} million followers. ")
# print(f"{data[i + 1]['name']} a {data[i + 1]['description']} from {data[i + 1]['country']}")


def format_data(account):
    """
# Formatting the account data into a printable format.
"""

    account_name = account["name"]
    account_descr = account['description']
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


# Displaying the art logo from the art.py module
print(logo)

# Generating a roandom account from the game data

account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
    account_b = random.choice(data)

print(f"Campare A: {format_data(account_a)}")
print(f"Campare A: {format_data(account_b)}")


# Asking the user for a guess.

# checking if the user is correct.
# Get the follower count for each account.
# Use the if statement to check if user is correct.

# Give the user feedback on their guess.

# Score keeping.

# Make the game repeatable.

# Making account at position b become the next account at position A

# Clear the screen in between rounds.
