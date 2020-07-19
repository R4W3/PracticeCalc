import time
import random
from colorama import init, Fore, Back, Style
init()


con = []
de = ["Hi! Ich bin Rene und wer bist du?", "Gib deinen Name ein: ", "Schön dich kennenzulernen", "Schwierigkeitsgrad", "Leicht", "Mittel", "Schwer", "Wähle deinen Schwierigkeitsgrad: ", "Addition bis 10", "Subtraktion bis 10", 10, "Wähle dein Thema: ", "Aufgabe", "Richtig", "Falsch", "Punkte", "Fertig", "Subtraktion bis 10", "Sekunden", "Addition bis 100",20, "Subtraktion bis 100", "Kleines Einmaleins", "Gleichungen mit einer Unbekannten", "Lösung für X: ", "Bestzeit: ", "Aufgaben", "Highscores"]
en = ["Hi! My Name is Rene and who are you?", "Enter your Name: ", "Nice to meet you", "Difficulty", "Easy", "Medium", "Hard", "Choose a difficulty: ", "Addition up to 10", "Subtraction up to 10", 10, "Choose your topic: ", "Excercise", "Correct", "Wrong", "Points", "Done", "Subtraction up to 10", "Seconds", "Addition up to 100",20, "Substraction up to 100", "Multiplication up to 100", "Equations with one unknown", "Solve for X: ", "Best Time: ", "Tasks", "Leaderboard"]
times_easy_add = []
numbers_easy_add = list(range(1, 6))
numbers_easy_subtract = list(range(1, 11))
numbers_moderate_add = list(range(1, 51))
numbers_moderate_subtract = list(range(1, 101))
numbers_moderate_multiply = list(range(1, 11))
numbers_hard = list(range(1, 51))



def mod_easy():
    print("\n")
    print(con[3],":", con[4])
    mod_easy_menu()

def mod_easy_menu():
    print("\n")
    print(Fore.GREEN + "1. ",con[8])
    print("2. ",con[9])
    print("d. ",con[3] )
    print(Style.RESET_ALL)
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
        times_easy_add.append(totaltime)
        times_easy_add.sort()
        print(con[25],times_easy_add[0])
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
    print(Fore.LIGHTBLUE_EX + "1. ",con[19])
    print("2. ",con[21])
    print("3. ",con[22])
    print("d. ",con[3] )
    print(Style.RESET_ALL)
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

def mod_hard():
    print("\n")
    print(con[3],":", con[6])
    mod_hard_menu()

def mod_hard_menu():
    print("\n")
    print(Fore.RED + "1. ",con[23])
    print("d. ",con[3] )
    print(Style.RESET_ALL)
    mod_hard_menu_input()

def mod_hard_menu_input():
    print("\n")
    hard_top = input(con[11])
    if hard_top == "1":
        mod_hard_equation()
    elif hard_top == "d":
        difficulty()
    else:
        mod_hard_menu_input()

def mod_hard_equation():
    print("\n")
    print(con[23])
    print("\n")
    excercise = 1
    score = 0
    start = time.time()
    while excercise <= 10:
        print(con[12], excercise, "/ 10")
        a = random.choice(numbers_hard)
        b = random.choice(numbers_hard)
        c = random.choice(numbers_hard)
        result = a * b + c
        print(a, "x", b, "+ X =", result)
        userresult = input(con[24])
        if int(userresult) == c:
            score += 1
            excercise += 1
            print(con[13])
            print(score, "/ 10")
            print("\n")
        if int(userresult) != c:
            excercise +=1
            print(con[14])
            print(c, "= X")
            print(score, "/ 10", con[15])
            print("\n")

    else:
        print(con[16])
        end = time.time()
        totaltime = end - start
        print(totaltime, con[18])
        print(score, "/ 10")
        print("\n")
        mod_hard()

def leaderboard():
    print("1.___")
    print("2.___")
    print("3.___")
    main_menu()


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
    main_menu()

def main_menu_input():
    print("\n")
    menu_select = input(con[11])
    if menu_select == "1":
        difficulty()
    if menu_select == "2":
        leaderboard()

def main_menu():
    print("\n")
    print("1.", con[26])
    print("2.", con[27])
    main_menu_input()

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
    print(Fore.GREEN + "1. ", con[4])
    print(Fore.LIGHTBLUE_EX + "2. ", con[5])
    print(Fore.RED + "3. ", con[6])
    print(Style.RESET_ALL)
    difficulty_input()







print(Fore.RED + "Pre-Release 0.1.1")
print(Fore.RED + "You may encounter bugs!")
print(Style.RESET_ALL)
print("\n")
language_chooser()