from words import words
import random

def get_valid_words(words):

    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()

def hangman():

    print("HANGMAN")
    print("Easy")
    print("Hard")
    difficulty = input("Choose the difficulty: ").upper()

    word=get_valid_words(words)
    underscore=[]
    letters_word = set(word)
    quantity=len(word)
    
    life = 6

    for x in range(quantity):
        underscore.append("_")
    if difficulty=="EASY":
        quantityBetween2=0
        wordRandom=''
        quantityBetween2=quantity/2
        for f in range(int(quantityBetween2)):
            wordRandom=word[random.randrange(quantity)]
        for x4 in range(quantity):

            if(wordRandom in word[x4]):
                underscore[x4]=wordRandom
                letters_word=letters_word-{wordRandom}
                letters_word2=set(letters_word)
                letters_word=letters_word2
        print("Welcome to easy version, you have "+str(life)+" lives")
    else:
        print("Welcome to hard version, you have "+str(life)+" lives")
    print(underscore)
    wordList = list(word)
    print(wordList)

    while len(letters_word) !=0 and life!=0:

        input_letter = input("Choose a letter please: ").upper()

        if input_letter in letters_word:

            for x in range(len(word)):

                if(input_letter in word[x]):
                    underscore[x]=input_letter
            print(underscore)      
            letters_word=letters_word-{input_letter}
            letters_word2=set(letters_word)
            letters_word=letters_word2
        else:
            life=life-1
            print("You're very wrong, I'm going to take your life. Now you have: "+str(life))

    if len(letters_word) ==0:
        print("Ganaste :D")

hangman()