
import random

EMPTY_SYMBOL = '_'

def GetRandomWord():
    filepath = "words.txt"
    file = open(filepath, "r")
    words = file.read()
    file.close()
    return random.choice(words.split(' '))



word = GetRandomWord()
fill_word = list()
for i in range (0,len(word)):
    fill_word.append(EMPTY_SYMBOL)
print(fill_word)

tries = 8

while tries > 0:
    char = (str)(input("choose a symbol: "))
    if (char in word):
        for i in range (0,len(word)):
            if word[i] == char:
                fill_word[i] = char
        print(fill_word)
        if not EMPTY_SYMBOL in fill_word:
            print("You won!")
            break
    else:
        tries -= 1
        if tries == 0:
            print(f"You lose! The word was '{word}'")
        else:
            print(f"wrong choice, {tries} tries left")