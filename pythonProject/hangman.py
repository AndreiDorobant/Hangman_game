import requests
import csv
import random
HANGMAN_STEPS = [
"""
------
| |
|
|
|
|
|
|___
""",
"""
------
| |
| O
|
|
|
|
|___
""",
"""
------
| |
| O
| |
|
|
|
|___
""",
"""
------
| |
| O
| /|
|
|
|
|___
""",
"""
------
| |
| O
| /|\\
|
|
|
|___
""",
"""
------
| |
| O
| /|\\
| /
|
|
|___
""",
"""
------
| |
| O
| /|\\
| / \\
|
|
|___
"""
]

mode = input("Play in online mode?[Y/N]:")
if mode == 'y' or mode == 'Y':
    response = requests.get('https://random-word-form.herokuapp.com/random/noun')
    # the status code on the given API returned 404 and a gave json() errors so I had to use a different API
    word_list = (response.json())
    word = word_list[0]
else:
    spamReader = csv.reader(open('words.csv', 'r'))

    data = sum([i for i in spamReader], [])
    word = random.choice(data)
step = 0;
ok=0;
win = 0
cheat = input("enable CHEAT mode? [Y/N]:")
if cheat == 'Y' or cheat == 'y':
    print("word is : " ,word)
guesslist = []
while step < 7 :
    print(HANGMAN_STEPS[step])
    unknown = 0;
    guess = input("Guess a letter or the word:")
    if len(guess) > 1:
        if guess == word:
            print("Correct! You win")
            win = 1
            if cheat == 'y' or cheat == 'Y':
                print("but you cheated")
            break
        else :
            print("wrong word!")
            step = step+1
            continue
    else:
        if guess in guesslist:
            print("letter already guessed")
            continue
        guesslist.append(guess)
        for i in range(0,len(word)):
            if word[i] in guesslist:
                print(word[i] , end='')
            else:
                print('_' , end='')
                unknown = 1
        print(' ')
        if guess in word:
            print("letter is in the word")
        else:
            step = step +1
            print("letter is not in the word")
    if unknown == 0:
        print("All letters guessed ! You win !")
        win = 1
        if cheat == 'y' or cheat == 'Y':
            print("but you cheated")
        break
if win == 0:
    print("Time ran out . You lose!")
    if cheat == 'y' or cheat == 'Y':
        print("Must have been on purpose")