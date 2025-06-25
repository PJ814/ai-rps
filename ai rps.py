# Paula rps (May 22 2025 - May 29 2025 - )
import random

print("Welcome to the game rock paper scissors")

#three varible (rock paper scissors)
r = 0
p = 0
s = 0

maya = {
    "rr" : 0,
    "pr" : 0,
    "sr" : 0,
    "rp" : 0,
    "pp" : 0,
    "sp" : 0,
    "rs" : 0,
    "ps" : 0,
    "ss" : 0
}
#ordered list this list keeps track the order the used types in their moves
ol = []     # <-- if.utl"ks'

playagain = True

#main code
while playagain:

    # making a total
    total = r + s + p
    if total == 0:
        choice = random.randint(0,2)
    else:
        rpc = r/total 
        ppc = p/total
        spc = s/total
        if rpc >= ppc and rpc >= spc:
            choice = 1
        elif ppc >= rpc and ppc >= spc:
            choice = 2
        elif spc >= rpc and spc >= ppc:
            choice = 0


    '''
    here we will write code that will instead of picking a random number will instead make the computer make it more educated guess
    statistics def: the colection of data in order to interpert and analyze behavior in daily life through math
    '''


    #players choice
    answer = input("rock, paper, or scissors? ")
    
    if choice == 0:
        print("the computer picked rock")
        if answer == "rock":
            r += 1
            print("we tied! Lets play again! @_@")
        elif answer == "paper":
            p += 1
            print("you won! Good job ^_^")
        elif answer == "scissors":
            s += 1
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
    
