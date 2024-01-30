import random
a="┏(°.°)┛    ┗(°.°)┓    ┗(°.°)┛    ┏(°.°)┓"
b=["rock","paper","scissors"]
num=int(input("Enter how many rounds you wanna play: "))
n=0

while n>=num:
    n+=1
    x=input("rock , paper, scissors: ")
    if x not in b:
        print ("Cheater !!!!!")
        print("\n")
        continue

    pc=random.choice(b)
    
    print (("Computer picked {}: ").format(pc))
    if x==pc:
        print (("It's a draw.\n{}").format(a))

    elif x=="rock" and pc=="scissors":
        print (("You win....rock beats scissors\n{}").format(a))
        
    elif x=="paper" and pc=="rock":
        print (("You win....paper beats rock\n{}").format(a))
        
    elif x=="scissors" and pc=="paper":
        print (("You win....scissors beats paper\n{}").format(a))
        
    else:
        print (("You lose. {} beats {}\n{}").format(pc,x,a))
    print("\n")
