a=input("Enter a line of text: ") 
b=a.split()
c={}
for i in b:
    k=i
    if k not in c:
        c1=b.count(k)
        c[k]=c1

for i in c:
    print(i," : ",c[i])
