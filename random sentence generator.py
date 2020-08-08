from random import shuffle
from guizero import App, Text, PushButton
def main():
    subjects = ["a man ", "a woman ", "a dog ", "a cat ", "a lot of people ", "a monkey ","This ","You ", "The one who created this program "]
    verbs = ["ate ", "drank ", "killed ", "enjoyed ","commited suicide using ","is getting "]
    objects = ["a man ", "a woman ", "a dog ", "a cat ", "a lot of people ", "soda", "money ", "sense ", "stupid","you","the one who created this program"]
    shuffle(subjects)
    shuffle(verbs)
    shuffle(objects)
    chosensubject=subjects[0]
    chosenverb=verbs[0]
    chosenobject=objects[0]
    sentencetext.value=chosensubject+chosenverb+chosenobject

#GUI setup
mainscreen=App("Random sentencen gemnerator")
welcometext=Text(mainscreen,text="""Welcome to this random sentence generator
Here's your sentence""")
sentencetext=Text(mainscreen,text="")
generatesentence=PushButton(mainscreen,text="Generate", command=main)

mainscreen.display()
