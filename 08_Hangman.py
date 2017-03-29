import time
import sys
letters="abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPQRSTUWVXYZ"
word2=""
wrong_letters=[]
good_letters=[]
def drawing(num_er):
    if num_er==0:
        print("\n\n\n\n\n")
    elif num_er==1:
        print("\n\n\n\n\n   /")
    elif num_er==2:
        print("\n\n\n\n\n   / \\")
    elif num_er==3:
        print("\n\n\n\n    |\n   / \\")
    elif num_er==4:
        print("\n\n\n    |\n    |\n   / \\")
    elif num_er==5:
        print("\n\n    |\n    |\n    |\n   / \\")
    elif num_er==6:
        print("\n    |\n    |\n    |\n    |\n   / \\")
    elif num_er==7:
        print("  __\n    |\n    |\n    |\n    |\n   / \\")
    elif num_er==8:
        print("  __\n |  |\n    |\n    |\n    |\n   / \\")
    elif num_er==9:
        print("  __\n |  |\n o  |\n    |\n    |\n   / \\")
    elif num_er==10:
        print("  __\n |  |\n o  |\n |  |\n    |\n   / \\")
    elif num_er==11:
        print("  __\n |  |\n o  |\n/|  |\n    |\n   / \\")
    elif num_er==12:
        print("  __\n |  |\n o  |\n/|\\ |\n    |\n   / \\")
    elif num_er==13:
        print("  __\n |  |\n o  |\n/|\\ |\n/   |\n   / \\")
    elif num_er==14:
        print("  __\n |  |\n o  |\n/|\\ |\n/ \\ |\n   / \\")
    else: sys.exit("wrong number")
    return
#################################################################
def check_word(word):
    for x in range (0,len(word)):
        if word[x] not in letters: return False
    return True
#################################################################
def check_letter(letter):
    global good_letters, wrong_letters, word2
    if letter not in letters: return 0
    elif letter not in word: 
        if letter not in wrong_letters:
            wrong_letters.append(letter)
            return 1
        else: return 1
    elif letter in good_letters:
        print(2)
        return 2
    elif letter in word and letter not in word2:
        good_letters.append(letter)
        word2=""
        for x in range(0,len(word)):
        	    if word[x] in good_letters:
        	        word2+=word[x]
        	    else:
        	        word2+=' '
        print("I'm here")
        return 3
    else:
        return 4
#################################################################
word=input("Write a word: ")
if check_word(word)==False: sys.exit("wrong character in the word")
print("\n"*10)
#################################################################
num_er=0
while(True):
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    drawing(num_er)
    print("Lenght of the word", len(word))
    print("WORD: ", word2)
    print("Wrong letters: ",wrong_letters)
    print("Falses: ", num_er)
    letter=input("Write a letter: ")
    result=check_letter(letter)
    if result==0:
        print("wrong character")
        num_er+=1
    elif result==1: 
        print("wrong letter")
        num_er+=1
    elif result==2: 
        print("this letter was writen")
        num_er+=1
    elif result==3: print("good letter")
    elif result==4: sys.exit("unknow error in function")
    else: sys.exit("unknow error")
    time.sleep(0.2)
    if num_er>14: 
        print("too much false\ngame over looser")
        sys.exit("end of the game")
    elif word2==word:
         print("you win")
         sys.exit("end of the game")

'''
for i in range(1,16):
    drawing(i)
    time.sleep(0.5)
'''
