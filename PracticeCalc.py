import time
import random

con = []
de = ["Hi! Ich bin Rene und wer bist du?", "Gib deinen Name ein: ", "Schön dich kennenzulernen", "Schwierigkeitsgrad", "Leicht", "Mittel", "Schwer", "Wähle deinen Schwierigkeitsgrad: ", "Addition bis 10", "Subtraktion bis 10", 10, "Wähle dein Thema: ", "Aufgabe", "Richtig", "Falsch", "Punkte", "Fertig", "Subtraktion bis 10", "Sekunden", "Addition bis 100",20, "Subtraktion bis 100", "Kleines Einmaleins"]
en = ["Hi! My Name is Rene and who are you?", "Enter your Name: ", "Nice to meet you", "Difficulty", "Easy", "Medium", "Hard", "Choose a difficulty: ", "Addition up to 10", "Subtraction up to 10", 10, "Choose your topic: ", "Excercise", "Correct", "Wrong", "Points", "Done", "Subtraction up to 10", "Seconds", "Addition up to 100",20, "Substraction up to 100", "Multiplication up to 100"]
numbers_easy_add = list(range(1, 6))
numbers_easy_subtract = list(range(1, 11))
numbers_moderate_add = list(range(1, 51))
numbers_moderate_subtract = list(range(1, 101))
numbers_moderate_multiply = list(range(1, 11))



def mod_easy():
    print("\n")
    print(con[3],":", con[4])
    mod_easy_menu()

def mod_easy_menu():
    print("\n")
    print("1. ",con[8])
    print("2. ",con[9])
    print("d. ",con[3] )
    mod_easy_menu_input()

def mod_easy_menu_input():
    print("\n")
    easy_top = input(con[11])
    if easy_top == "1":
        mod_easy_add()
    elif easy_top == "2":
        mod_easy_subtract()
    elif easy_top == "d":
        difficulty()
    else:
        mod_easy_menu_input()

def mod_easy_add():
    print("\n")
    print(con[8])
    print("\n")
    excercise = 1
    score = 0
    start = time.time()
    while excercise <= 10:
        print(con[12], excercise, "/ 10")
        a = random.choice(numbers_easy_add)
        b = random.choice(numbers_easy_add)
        result = a + b
        print(a, "+", b, "= ")
        userresult = input()
        if int(userresult) == result:
            score += 1
            excercise += 1
            print(con[13])
            print(score, "/ 10")
            print("\n")
        if int(userresult) != result:
            excercise +=1
            print(con[14])
            print(a, "+", b, "=", result)
            print(score, "/ 10", con[15])
            print("\n")

    else:
        print(con[16])
        end = time.time()
        totaltime = end - start
        print(totaltime, con[18])
        print(score, "/ 10")
        print("\n")
        mod_easy()

def mod_easy_subtract():
    print("\n")
    print(con[8])
    print("\n")
    excercise = 1
    score = 0
    start = time.time()
    while excercise <= 10:
        print(con[12], excercise, "/ 10")
        a = random.choice(numbers_easy_subtract)
        b = random.choice(numbers_easy_subtract)
        result = max(a,b) - min(a,b)
        print(max(a,b), "-", min(a,b,), "= ")
        userresult = input()
        if int(userresult) == result:
            score += 1
            excercise += 1
            print(con[13])
            print(score, "/ 10")
            print("\n")
        if int(userresult) != result:
            excercise +=1
            print(con[14])
            print(max(a,b), "-", min(a,b,), "=", result)
            print(score, "/ 10", con[15])
            print("\n")

    else:
        print(con[16])
        end = time.time()
        totaltime = end - start
        print(totaltime, con[18])
        print(score, "/ 10")
        print("\n")
        mod_easy()

def mod_moderate():
    print("\n")
    print(con[3],":", con[5])
    mod_moderate_menu()

def mod_moderate_menu():
    print("\n")
    print("1. ",con[19])
    print("2. ",con[21])
    print("3. ",con[22])
    print("d. ",con[3] )
    mod_moderate_menu_input()

def mod_moderate_menu_input():
    print("\n")
    moderate_top = input(con[11])
    if moderate_top == "1":
        mod_moderate_add()
    elif moderate_top == "2":
        mod_moderate_subtract()
    elif moderate_top == "3":
        mod_moderate_multiply()
    elif moderate_top == "d":
        difficulty()
    else:
        mod_moderate_menu_input()

def mod_moderate_add():
    print("\n")
    print(con[19])
    print("\n")
    excercise = 1
    score = 0
    start = time.time()
    while excercise <= 10:
        print(con[12], excercise, "/ 10")
        a = random.choice(numbers_moderate_add)
        b = random.choice(numbers_moderate_add)
        result = a + b
        print(a, "+", b, "= ")
        userresult = input()
        if int(userresult) == result:
            score += 1
            excercise += 1
            print(con[13])
            print(score, "/ 10")
            print("\n")
        if int(userresult) != result:
            excercise +=1
            print(con[14])
            print(a, "+", b, "=", result)
            print(score, "/ 10", con[15])
            print("\n")

    else:
        print(con[16])
        end = time.time()
        totaltime = end - start
        print(totaltime, con[18])
        print(score, "/ 10")
        print("\n")
        mod_moderate()

def mod_moderate_subtract():
    print("\n")
    print(con[21])
    print("\n")
    excercise = 1
    score = 0
    start = time.time()
    while excercise <= 10:
        print(con[12], excercise, "/ 10")
        a = random.choice(numbers_moderate_subtract)
        b = random.choice(numbers_moderate_subtract)
        result = max(a,b) - min(a,b)
        print(max(a,b), "-", min(a,b,), "= ")
        userresult = input()
        if int(userresult) == result:
            score += 1
            excercise += 1
            print(con[13])
            print(score, "/ 10")
            print("\n")
        if int(userresult) != result:
            excercise +=1
            print(con[14])
            print(max(a,b), "-", min(a,b,), "=", result)
            print(score, "/ 10", con[15])
            print("\n")

    else:
        print(con[16])
        end = time.time()
        totaltime = end - start
        print(totaltime, con[18])
        print(score, "/ 10")
        print("\n")
        mod_moderate()

def mod_moderate_multiply():
    print("\n")
    print(con[22])
    print("\n")
    excercise = 1
    score = 0
    start = time.time()
    while excercise <= 10:
        print(con[12], excercise, "/ 10")
        a = random.choice(numbers_moderate_multiply)
        b = random.choice(numbers_moderate_multiply)
        result = a * b
        print(a, "x", b, "=")
        userresult = input()
        if int(userresult) == result:
            score += 1
            excercise += 1
            print(con[13])
            print(score, "/ 10")
            print("\n")
        if int(userresult) != result:
            excercise +=1
            print(con[14])
            print(max(a,b), "-", min(a,b,), "=", result)
            print(score, "/ 10", con[15])
            print("\n")

    else:
        print(con[16])
        end = time.time()
        totaltime = end - start
        print(totaltime, con[18])
        print(score, "/ 10")
        print("\n")
        mod_moderate()


def language_chooser():
    print("Choose your language")
    print("1. English")
    print("2. Deutsch")
    print("\n")
    lan = input("Enter a number and press enter: ")
    print("\n")
    if lan == "1":
        con.extend(en)
        user_info()
    elif lan == "2":
        con.extend(de)
        user_info()
    else:
        print("Invalid!")
        language_chooser()

def user_info():
    print(con[0])
    user_name = input(con[1])
    print("\n")
    print(con[2], user_name, "!")
    print("\n")
    difficulty()

def difficulty_input():
    print("\n")
    diff = input(con[7])
    if diff == "1":
        mod_easy()
    elif diff == "2":
        mod_moderate()
    elif diff == "3":
        mod_hard()
    else:
        difficulty_input()

def difficulty():
    print(con[3])
    print("1. ", con[4])
    print("2. ", con[5])
    print("3. ", con[6])
    difficulty_input()







print("Pre-Release 0.0.4")
print("Not all functions work!")
print("\n")
language_chooser()