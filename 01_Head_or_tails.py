from random import randint
import sys
def selection_player1():
    print("Head or Tails\n1.Heads\n2.Tails\n")
    player1=int(input(""))-1
    if player1==0: return "Heads"
    elif player1==1: return "Tails"
    else: sys.exit("Wrong number")
def selection_player2():
    if randint(0,1)==0: return "Heads"
    else: return "Tails"
###################################################
x='y'
score=0
while x!='n':
    print("Score: ", score)
    player1=selection_player1()
    player2=selection_player2()
    print("You choose this: ", player1, "\nAnd this dropped: ", player2, "\n")
    if player1==player2:
        score+=1
        print("You win")
    else:
        print("You lose")
    x=input("Wanna play again(y/n): ")
