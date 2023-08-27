import random
options=("stone","paper","pencil","scissor")
cont=True
while cont:
    m=random.choice(options)
    print("enter your choice :(stone,paper,pencil,scissor)")
    n=input()
    if m==n:
        print("Tie up")
    elif(m=="scissor" and n=="stone"):
        print("computer generated ",m,"hence")
        print("You win")
    elif(m=="stone"and n=="paper"):
        print("Computer generated",m,"hence")
        print("You win")

    elif(m=="pencil" and n=="stone"):
        print("Computer generated",m,"hence")
        print("You win")
    elif(m=="pencil"  and n=="scissor"):
        print("Computer generated",m,"hence")
        print("You win")
    elif(m=="paper" and n=="pencil"):
        print("Computer generated ",m,"hence")
        print("You win")
    else:
        print("Computer generated",m,"hence")
        print("You lose")
    s=input("Do yo want to play again.(y/n)").lower()
    if s=="y":
        cont=True
    elif s=="n":
        cont=False
    else:
         print("Oop ! you entered something wrong ")









