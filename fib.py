n=int(input("Enter n value"))
first=0
second=1
i=0
while i<=n:
    print(first)
    temp=first
    first=second
    second=temp+second
    i+=1
