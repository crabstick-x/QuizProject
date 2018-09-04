import os.path, os, sys
import csv

database_location = "database"
# Enter a directory for where the database CSV files are located.
questions_location = "questions"
# Enter a directory for where the question CSV files are located.
# The correct answer is the first answer in the CSV file. At runtime the answers are shuffled.


def load_user_info(usr, difficulty, topic):
    if os.path.isfile(database_location + "/" + usr + ".csv") == True:

        user_file = database_location + "/" + usr + ".csv"
        fo = open(user_file, "rb")
        csv_reader = csv.reader(fo, delimiter=",")

        row_id = 0

        highest_score = 0
        average_score = 0

        print("=========== " + usr.upper() + " ===========")

        for row in csv_reader:
            if row_id== 0:
                print("Name: " + row[1])
                print("Age: " + row[2])
                print("Year Group: " + row[3])
            else:
                if (row[4].upper() == difficulty.upper() or difficulty.upper() == "ALL") \
                        and (row[0].upper() == topic.upper() or topic.upper() == "ALL"):
                    print("\nQUIZ:")
                    print("Topic: " + row[0])
                    print("Difficulty: " + row[4])
                    print("Score: " + row[1] + " / " + row[2])
                    print("Grade: " + row[3])

                    average_score = average_score + int(row[1])

                    if highest_score < int(row[1]):
                        highest_score = int(row[1])

            row_id = row_id + 1

        average_score = average_score / (row_id - 1)

        fo.close()

        print("\nHighest Score: " + str(highest_score))
        print("Average Score: " + str(average_score))
        print("End of Information")

    else:

        print("User not found!")


def get_usernames():
    user_list_location = database_location + "/usernames.txt"
    fo = open(user_list_location, "r")

    usernames_list = fo.readlines()

    usernames_list = [x.strip() for x in usernames_list]

    return usernames_list


def check_if_username_exists(usr):
    return os.path.isfile(database_location + "/" + usr + ".csv")


def load_quiz(topic, difficulty):
    quiz_file = questions_location + "/" + topic.lower() + ".csv"
    fo = open(quiz_file, "rb")
    csv_reader = csv.reader(fo, delimiter=",")

    questions = []
    answers = []
    correct_answers = []

    row_id = 0

    for row in csv_reader:
        if row[0].upper() == difficulty.upper():
            questions.append(row[1])
            correct_answers.append(row[2])
            question_answers = []
            for col in row:
                if (not col.upper() == row[0].upper()) and (not col.upper() == row[1].upper()):
                    question_answers.append(col)
            answers.append(question_answers)
        row_id = row_id + 1

    return questions, answers, correct_answers


def generate_username(name, age):
    return name[:3] + str(age)

def register_user():
    print("\n=========== REGISTER ===========")
    name = raw_input("Name: ")
    age = int(raw_input("Age: "))
    username = generate_username(name, age)
    print("Username: " + username)
    password = raw_input("Password: ")
    year_group = int(raw_input("Year Group: "))

    user_list_location = database_location + "/usernames.txt"
    fo = open(user_list_location, "a")
    fo.write(username + "\n")
    fo.close()

    user_file = database_location + "/" + username + ".csv"
    fo = open(user_file, "w")

    fo.write(password + "," + name + "," + str(age) + "," + str(year_group) + "\n")

    print("\n User Information Saved!")

    return username


def save_quiz(username, correct, questions, grade, topic, difficulty):
    user_file = database_location + "/" + username + ".csv"
    fo = open(user_file, "a")
    fo.write(topic + "," + str(correct) + "," + str(questions) + "," + grade + "," + difficulty & "\n")
    fo.close()
    print("Data Saved!")