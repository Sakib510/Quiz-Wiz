# Quiz Using Python
import time
import pyttsx3
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

print('\n--------------------------------------------------------------------')
talk('\nHello participants! Welcome to this quiz!\n')
print ('\nHello participants! Welcome to this quiz!\n')
talk('What is your name?')
name =  str(input('What is your name?\n'))
print('Hi '+ name +'! Get Ready For the quiz..\n')
talk('Hi '+ name +'! Get Ready For the quiz..')
talk('What is your id?')
id =  str(input('What is your id? \n'))
print('You are eligible for the quiz.\n')
talk('You are eligible for the quiz')
print('--------------------------------------------------------------------\n')
print('Instruction :\n\nYou will be tested on 5 questions and for each question you get two/three choices.\n\nYou select which is the correct answer.\n\nFor every correct answer you get 1 mark and For wrong answer you loose 0.5 mark.\n')
talk('Instruction :\n\nYou will be tested on 5 questions and for each question you get two/three choices.\n\nYou select which is the correct answer.\n\nFor every correct answer you get 1 mark and For wrong answer you loose 0.5 mark.\n')
print('\n--------------------------------------------------------------------\n\n')
print('--------------------------------------------------------------------')
print('\t\t\t\tQuestion')
talk('\t\t\t\tQuestion')
print('--------------------------------------------------------------------\n')

# This is the score

score = 0


def ques_1():
    global score
    time.sleep(0.5)
    print('1.\nPython is a high level programming language?\n')
    talk('Python is a high level programming language?')
    print('a. True')
    print('b. False')
    print('')
    talk("What's the right answer:")
    ans = str(input("What's the right answer: "))
   
    if ans == "a":    
        print("well done, that's correct!")
        talk("well done, that's correct!")
        score += 1

    else:
        print("Sorry, that was the wrong answer!")
        talk("Sorry, that was the wrong answer!")
        score -= 1 / 2

    print('\n--------------------------------------------------------------------\n')
    ques_2()


def ques_2():
    global score
    time.sleep(0.5)
    print('2.\nWhat does the print function do?\n')
    talk('What does the print function do?')
    print('a. Prints string')
    print('b. Prints integers')
    print('c. Prints both')
    print('')
    talk("What's the right answer:")
    ans = str(input("What's the right answer: "))

    if ans == "c":
        print("well done, that's correct!")
        talk("well done, that's correct!")
        score += 1
    else:
        print("Sorry, that was the wrong answer!")
        talk("Sorry, that was the wrong answer!")
        score -= 1 / 2

    print('\n--------------------------------------------------------------------\n')
    ques_3()


def ques_3():
    global score
    time.sleep(0.5)
    print('3.\nWhich one of the following is the correct extension of the Python file?\n')
    talk('Which one of the following is the correct extension of the Python file?')
    print('a. .python')
    print('b. .py')
    print('c. None of these')
    print('')
    talk("What's the right answer:")
    ans = str(input("What's the right answer: "))

    if ans == "b":
        print("well done, that's correct!")
        talk("well done, that's correct!")
        score += 1
    else:
        print("Sorry, that was the wrong answer!")
        talk("Sorry, that was the wrong answer!")
        score -= 1 / 2
    print('\n--------------------------------------------------------------------\n')
    ques_4()


def ques_4():
    global score
    time.sleep(0.5)
    print('4.\nWhich character is used in Python to make a single line comment?\n')
    talk('Which character is used in Python to make a single line comment?')
    print('a. #')
    print('b. /')
    print('c. //')
    print('')
    talk("What's the right answer:")
    ans = str(input("What's the right answer: "))

    if ans == "a":
        print("well done, that's correct!")
        talk("well done, that's correct!")
        score += 1
    else:
        print("Sorry, that was the wrong answer!")
        talk("Sorry, that was the wrong answer!")
        score -= 1 / 2
    print('\n--------------------------------------------------------------------\n')
    ques_5()


def ques_5():
    global score
    time.sleep(0.5)
    print('5.\nThe output to execute string.ascii_letters can also be obtained from:?\n')
    talk('The output to execute string.ascii_letters can also be obtained from')
    print('a. ascii_lowercase_string.digits')
    print('b. lowercase_string.upercase')
    print('c. ascii_lowercase+string.ascii_upercase')
    print('')
    talk("What's the right answer:")
    ans = str(input("What's the right answer: "))

    if ans == "c":
        print("well done, that's correct!")
        talk("well done, that's correct!")
        score += 1
    else:
        print("Sorry, that was the wrong answer!")
        talk("Sorry, that was the wrong answer!")
        score -= 1 / 2
    print('\n--------------------------------------------------------------------\n')
    ques_6()


def ques_6():
    global score
    time.sleep(0.5)
    print('6.\nWhich module is used in python to create Graphics?\n')
    talk('Which module is used in python to create Graphics?')
    print('a. Turtle')
    print('b. Canvas')
    print('c. Tkinter')
    print('')
    talk("What's the right answer:")
    ans = str(input("What's the right answer: "))

    if ans == "a":
        print("well done, that's correct!")
        talk("well done, that's correct!")
        score += 1
    else:
        print("Sorry, that was the wrong answer!")
        talk("Sorry, that was the wrong answer!")
        score -= 1 / 2
    print('\n--------------------------------------------------------------------\n')


    print('Dashboard : \n')
    talk('Dashboard : \n')
    print('Well done.You finished the quiz!')
    talk('Well done.You finished the quiz!')

ques_1()
if (score >= 4):
    talk("Excellent!!!  " + name)
    print("Excellent!!!  " + name)
    print("Your scored: ", score)
elif (3 < score < 3):
    talk("Good ! " + name)
    print("Good ! " + name)
    print("Your scored: ", score)
else:
    talk("Better luck next time ! " + name)
    print("Better luck next time ! " + name)
    print("Your scored: ", score)

print('\n--------------------------------------------------------------------\n')
