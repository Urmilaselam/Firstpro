n=int(input("Enter n value: "))
tot=0
temp=n
while n>0:
    d=n%10
    tot=tot+d
    n=n//10
print("sum of numbers are:",tot)
if(temp==tot):
    print("Palindrome !")
else:
    print("Not palindrome !")
