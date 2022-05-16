#pip installations: pip install random-word ; pip install pyyaml

from random_word import RandomWords

def word_generator():
    word = ''
    word_len=8
    while(word_len>=8):
        r=RandomWords()
        word=r.get_random_word()
        word=word.lower()
        word_len=len(word)
    return word

def hangman():
    str1=word_generator()
    str2=''
    #print(str1)
    for letter in str1:
        str2 = str2 + '_'

    errors=10
    while errors > 0:
        if '_' in str2:
            input_value=input("Enter a letter ")
            control=str2
            str2 = check_match(input_value, str1, str2)
            print(str2)
            if control == str2:
                errors=errors-1
            print("remaining errors: ", errors)
            print("************************************")

        else:
            print('*******WIN word completed WIN*******')
            break
    else:
        print("Game over")

def check_match(input,str1,str2):
    indexes = index_finder(input, str1)
    for index in indexes:
        if len(input) > 0:
            str2 = str2[:index] + input + str2[index + 1:]
    return str2

def index_finder(input, word):
    indexes=[]
    i = 0
    for letter in word:
        if letter == input:
            indexes.append(i)
        i = i + 1
    return indexes


hangman()


