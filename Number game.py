import random
import time
a= int(input("Emter Lower limit: ")) 
b= int(input("Enter Upper limit: "))  

d= random.randint(a,b)
print("\nYou've only ",5," chances to guess the integer!\n")

c=0
while c<5:
    c+=1
    e=int(input("Guess a number:- "))
    if d==e:  
       print("Congrats you did it in ",c, " try")
       break
    elif d>e:
       print("Dude it's small!")
    elif d<e:
       print("Dude it's high!")

if c>=5:
   print("\nThe number is ",d)
   print("\nYou are noob!")
time.sleep(4)
