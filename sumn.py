####Important programme
n=int(input("Enter n value: "))
tot=0
while n>0:
    dig=n%10
    tot=tot+dig
    n=n//10
print("The sum of n numbers are: ",tot)