import random
from game_data import data
from art import logo, vs


def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]

    return "{} is {} from {}.".format(account_name, account_desc, account_country)


def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


score = 0

still_playing = True

account_b = random.choice(data)

while still_playing:

    print(logo)

    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']

    is_correct = check_answer(user_guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")


    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        still_playing = False