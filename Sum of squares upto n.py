# 1*2 + 3*2 + 5*2 + 7*2
n=int(input("Enter the value of time"))
s=0
a=0
l=[]
for i in range(1,n+1):
   x=str(i)+"^2"
   i=i**2
   s=s+i
   l.append(x)
#print("sum of squares of number upto",n," = ",s)
print(*l,sep=" + ")
print(s)
