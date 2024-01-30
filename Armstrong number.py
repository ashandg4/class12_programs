# Armstrong number
print("An Armstrong number is a number such that the sum of its digits raised to the third power is equal to the number itself")
n=int(input("Enter a number: "))
s=0
a=n
while a>0:
    digit=a%10
    s+=digit**3
    a//=10
if n==s:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")
