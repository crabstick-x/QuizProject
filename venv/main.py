from database import *
from quiz import *

topics = ["ALL", "Maths", "Music"]
difficulties = ["ALL","Easy", "Medium", "Hard"]


def init_menu():

    print("   ___        _     ")
    print("  / _ \ _   _(_)____")
    print(" | | | | | | | |_  /")
    print(" | |_| | |_| | |/ /")
    print("  \__\_\\__,_|_/___|")
    print("\n")
    print("=========== MENU ===========")
    print("1) Take a Quiz")
    print("2) Get user quizzes")

    choice = int(input("\nChoice: "))

    if choice == 1:
        start_quiz(topics, difficulties)
        init_menu()
    elif choice == 2:
        display_users()


def display_users():
    print("\nPlease choose a user by entering the corresponding number:")
    usernames = get_usernames()
    choice_number = 1

    for user in usernames:
        print(str(choice_number) + ") " + user)
        choice_number = choice_number + 1

    choice_number = 1

    chosen_username = usernames[int((input("\nChoice: "))) - 1]

    print("\nPlease enter a topic (Type 0 for all topics listed):")
    for topic in [topic for topic in topics if topic != "ALL"]:
        print(str(choice_number) + ") " + topic)
        choice_number = choice_number + 1

    choice_number = 1

    chosen_topic = topics[int((input("\nChoice: ")))]

    print("\nPlease enter a difficulty (Type 0 for all difficulties listed):")
    for difficulty in [difficulty for difficulty in difficulties if difficulty != "ALL"]:
        print(str(choice_number) + ") " + difficulty)
        choice_number = choice_number + 1

    chosen_difficulty = difficulties[int((input("\nChoice: ")))]

    print("\n")
    load_user_info(chosen_username, chosen_difficulty, chosen_topic)


init_menu()
