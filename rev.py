n=313
t=n
r=0
i=1
while n!=0:
    d=n%10
    r=r*10+d
    n=n//10
print(r)
if(t==r):
    print("Palindrome")
else:
    print("not palindrome")
