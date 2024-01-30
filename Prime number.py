n=int(input("Enter a no."))
a=0
for i in range(2, n):
    if n % i == 0:
        print("not a prime no.")
        break
else:
    print("prime no.")
