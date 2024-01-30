n=int(input("Enter the term"))
f=0
s=1
print(f,s,end=" ")
for i in range(2,n):
    ne=f+s
    print(ne,end=" ")
    f=s
    s=ne
