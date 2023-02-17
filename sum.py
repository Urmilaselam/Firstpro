n=int(input("Enter n value: "))
i=0
first=0
second=1
while i<n:
    print(first,end=" ")
    temp=first
    first=second
    second=temp+second
    i+=1
