i,temp=0,0
n = int(input("please give a number : "))
count=0
for i in range(2,n//2):
    if n%i == 0:
        temp=1
        break
    count+=1
if temp == 1:
    print("given number is not prime")
else:
    print("given number is prime","count of prime=",count)
