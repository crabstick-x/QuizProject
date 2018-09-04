from database import *
from random import shuffle


def start_quiz(topics, difficulties):
    username = str(input("\nPlease enter your username: "))
    if check_if_username_exists(username) == False:
        if str(input("Username not found. Would you like to create an account? (Y/N): ")).upper() == "Y":
            username = register_user()
        else:
            username = ""
    if not username == "":
        choice_number = 1
        print("\nPlease enter a topic:")
        for topic in [topic for topic in topics if topic != "ALL"]:
            print(str(choice_number) + ") " + topic)
            choice_number = choice_number + 1

        choice_number = 1

        chosen_topic = topics[int((input("\nChoice: ")))]

        print("\nPlease enter a difficulty:")
        for difficulty in [difficulty for difficulty in difficulties if difficulty != "ALL"]:
            print(str(choice_number) + ") " + difficulty)
            choice_number = choice_number + 1

        chosen_difficulty = difficulties[int((input("\nChoice: ")))]

        answers = []
        questions = []
        correct_answers = []

        questions, answers, correct_answers = load_quiz(chosen_topic, chosen_difficulty)

        correct_total, total_questions, percentage = run_quiz(questions, answers, correct_answers)

        calculated_grade = calculate_grade(percentage)

        print("Correct Answers: " + str(correct_total))
        print("Total Questions: " + str(total_questions))
        print("Percentage: " + str(percentage) + "%")
        print("Grade: " + calculated_grade)

        save_quiz(username, correct_total, total_questions, calculated_grade, chosen_topic, chosen_difficulty)


def run_quiz(questions, answers, correct_answers):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
    question_id = 0

    correct_answers_total = 0

    for question in questions:
        print("\n=========== QUESTION " + str(question_id + 1) + " ===========\n" + question)
        current_qustion_answers = answers[question_id]
        shuffle(current_qustion_answers)
        answer_id = 0
        for answer in current_qustion_answers:
            print(alphabet[answer_id] + ") " + answer)
            answer_id = answer_id + 1

        chosen_answer = input("\nYour Answer (a, b, c...): ")
        chosen_id = alphabet.index(chosen_answer.lower())

        if current_qustion_answers[chosen_id].upper() == correct_answers[question_id].upper():
            print("\nCORRECT ANSWER!! :)")
            correct_answers_total = correct_answers_total + 1
        else:
            print("\nINCORRECT ANSWER :(")
            print("'" + correct_answers[question_id] + "' was the correct answer.")

        question_id = question_id + 1

    print("\n=========== QUIZ OVER =========== ")

    percentage = 100 * correct_answers_total / question_id

    return correct_answers_total, question_id, percentage


def calculate_grade(perc):
    grade = ""
    if perc >= 0 and perc <= 25:
        grade = "D"
    elif perc >= 25 and perc <= 50:
        grade = "C"
    elif perc >= 50 and perc <= 75:
        grade = "B"
    elif perc >= 75 and perc <= 100:
        grade = "A"
    return grade
