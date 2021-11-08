#for my second integration project, I made a true or false quiz show
#makes all questions random
import random

inFile = open("QuizScore.txt", 'a')
def getTofstatements():

    statements = []
    statements.append(["Ladybugs can only be red with black spots","F"])
    statements.append(["Leonardo Dicaprio won his first Oscar for best actor in 2016", "T"])
    statements.append(["a hyena's 'laughter' is a form of communication used to convey frustration or fear", "T"])
    statements.append(["The Konami Code is activated when the player inputs '↓ ↘ → + B'", "F"])
    statements.append(["The Beatles debut album 'Please Please Me' was released on August 5, 1966", "F"])
    statements.append(["Though being the the main antagonist of the 'Friday the 13th' series, Jason Voorhees did not make an appearance until the second movie", "T"])
    statements.append(["The arcade game 'Donkey Kong' was originally planned to be a 'Popeye' game", "T"])
    statements.append(["Like bees, wasps make honey", "F"])
    statements.append(["Nobody expects the Spanish Inquisition!", "T"])
    statements.append(["In Marvel Comics, the superhero Thor's alter ego was originally Donald Blake", "T"])
    statements.append(["The Teenage Mutant Ninja Turtles did not have a live musical tour at the height of their fame.", "F"])


    return statements

def playTofgame():

    #get true or false statements
    tofStatements = getTofstatements()

    #Randomize tof statements
    random.shuffle(tofStatements)

    #set player score to 0
    score = 0
    inFile = open("QuizScore.txt", 'a')
    #Show tof statements using a loop
    for s in tofStatements:


        #present statement
        print("True or False: " + s[0])

        #user enters guess
        guess = input("Enter T or F: ")
        #check if guess is correct
        if guess == s[1]:
            print("Good job! That was correct!")
            #update score
            score = score + 1
        else:
            print("Sorry! That was wrong!")
    #show final score
    print("Congratulations! You scored a total of " + str(score) + " points.")
    if score == 10:
        print("You looked at your phone, didn't you?")
    elif score <= 9 and score >= 7:
        print("Hey! You did pretty good!")
    elif score <= 6 and score >= 5:
        print("Not a bad score, but not a good one either...")
    elif score <= 4 and score >= 2:
        print("Looks like someone needs to study a bit more!")
    else:
        print("Okay, boomer")
    #return to main menu
    return mainMenu()

def mainMenu():
    print("+------------------------------+")
    print("|Welcome to Ethan's quiz show! |")
    print("|Please select an option:      |")
    print("|1. Play                       |")
    print("|0. Quit                       |")
    print("+------------------------------+")
    #player chooses to play or quit
    choice = input("Enter here: ")
    if choice == "1":
        playTofgame()
    elif choice == "0":
        print("Thanks for playing!")
        quit()
mainMenu()