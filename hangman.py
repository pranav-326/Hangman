import random
import wordList
import stages
randChoice=random.choice(wordList.word_list)
# print(randChoice)
blankLetters="_"*len(randChoice)
print(blankLetters)
lives=6
correctLetters=[]
wrongLetters=[]
displayTemp=blankLetters
while True:
    display=""
    userInput=input('Enter a letter:').lower()
    if userInput in correctLetters:
        print("You have already guessed this letter and it was right")
    if userInput in wrongLetters:
        print("You have guessed this letter already and it was wrong")
    for letter in randChoice:
        if userInput==letter:
            display+=userInput
            correctLetters.append(letter)
        elif letter in correctLetters:
            display+=letter
        else:
            display+="_"
    print(display)
    if userInput not in randChoice:
        print("Wrong guess!")
        wrongLetters.append(userInput)
        lives -= 1
    else:
        correctLetters.append(userInput)
        print("Correct guess!")
    print(f"Lives remaining: {lives}/6")
    print(stages.stages[lives])
    if lives==0:
        print("Exceeded the number of guesses")
        break
    print(lives)
    displayTemp=display
    if "_" not in display:
        print("Game won!")
        break
input("Press Enter to exit")