# Paula rps (May 22 2025 - May 29 2025 - )
import random

print("Welcome to the game rock paper scissors")

#three varible (rock paper scissors)
r = 0
p = 0
s = 0
gyggftuydfjvghkbuiyg78ruftdguggyughjbnjyugjbu



gdhfhgfhgfgh
kgjghj
hjkhkjh


print("awww you lost! #_#n")
    elif choice == 1:
        print("the computer picked paper")
        if answer == "rock":
            r += 1
            print("Awww you lost! >_<")
        elif answer == "paper":
            p += 1
            print("We tied! Lets play again @_@")
        elif answer == "scissors":
            s += 1
            print("Yay I won! $_$")
    else:
        print("the computer picked scissors")
        if answer == "rock":
            r += 1
            print("Yay you won! #_#")
        elif answer == "paper":
            p += 1
            print("Yay! I won! &_&")
        elif answer == "scissors":
            s += 1
            print("We tied! Lets play again -_-")

    '''
    we are going to used ol, our ordered list to track of patterns in our players moves. 
    if size of ol is equal to 2, then a pattern exists in our list, and we must keep record of it for our computer.
    XD
    '''
    ol.append(answer)

    if len(ol) == 2:
        stringvar = ol[0][0] + ol[1][0]
        for combo in maya:
            if combo == stringvar:
                maya[combo] += 1
                ol.pop(0)
            
    rematch = input("would you like a rematch, type \"Y\" for yes and \"N\" for no ")
    if rematch == "N" or rematch == "n":
        playagain = False
    
