
from guizero import App, Window, Text, PushButton, TextBox

def maingame():
    from random import shuffle
    words = ["guess", "the", "bloody", "word"]  # list of possible words
    shuffle(words)  # reorder the words randomly
    chosenword = words[1]  # chose a word from the set
    losepoints = 0  # letters you got wrong
    actuallose = 0  # just to measure if you actually lost and terminate when reaches 1

    def checklose(losepoints, actuallose, chosenguesses, guess, chosenword):  # checks lose conditions

        if losepoints > 5:
            actuallose = 1

        if guess in chosenword:
            print("correct")
            print("Your choice is present in the word. Choice=" + guess)
            print("you already got")
            for i in range(0,len(chosenguesses)):
                print(chosenguesses[i])
            print(chosenguesses)
            if actuallose == 1:
                print("haha loser")

        elif guess not in chosenword:
            a = 'wrong'
            losepoints+=1
            print(a)
            return a



    while actuallose < 1:  # should interrupt when 5 wrong tries are exeded
        guess = str(input("what is your guess"))
        chosenguesses = []
        chosenguesses.append(guess)
        checklose(losepoints, actuallose, chosenguesses, guess, chosenword)
        if chosenguesses==chosenword:
            print("you won!")
            break
        if losepoints > 5:
            actuallose = 1
        elif actuallose == 1:
            print("haha you lost you idiot")
        elif guess not in chosenword:
            losepoints+=1

def startgame():
    startwindow.hide()
    gamemenu.show()
maingame()
# basic prototype GUI setup
gamemenu=App(title="")
wordtext=Text(gamemenu,text="Try to guess")
wordtext2=Text(gamemenu,text="you got nothing wrong")
insertguesses=TextBox(gamemenu)
tryagainbutton=PushButton(gamemenu, text="Update")
#setup of the intro screen
startwindow=Window(gamemenu)
introText=Text(startwindow, text="Welcome to this hangman game", size=20)
startbutton=PushButton(startwindow, text="Start", command=startgame )

#runs the GUI
gamemenu.display()
gamemenu.hide()
startwindow.show()
maingame()
