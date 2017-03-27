from random import randint
import sys
def player1():
    print("Choose\n1.Rock\n2.Paper\n3.Scissors\n4.Lizard\n5.Spock\n")
    choice=int(input(""))
    if choice not in [1,2,3,4,5]: sys.exit("wrong number")
    return choice
def player2():
    return randint(0,4)+1
def print_selection(choice):
    if choice==1:return "Rock"
    elif choice==2:return "Paper"
    elif choice==3:return "Scissors"
    elif choice==4:return "Lizard"
    elif choice==5: return "Spock"
    else: sys.exit("wrong number")
    return
def fight(p1,p2):
    if (p1==1 and (p2==3 or p2==4)) or 	(p1==2 and (p2==1 or p2==5)) or (p1==3 and (p2==2 or p2==4)) or (p1==4 and (p2==2 or p2==5)) or 	(p1==5 and (p2==1 or p2==3)): return True
    else: return False
def result_of_fight(p1,p2):
    result=fight(p1,p2)
    if fight(p1,p2)==True: return "You win"
    elif fight(p2,p1)==True: return "You lose"
    else: return "Dead-heat"
#####################################
p1=player1()
p2=player2()
print("Player1: ",print_selection(p1),"\n")
print("Player2: ",print_selection(p2),"\n")
print(result_of_fight(p1,p2))