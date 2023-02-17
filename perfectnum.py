n=int(input("Enter n val: "))#5
sum=0
for i in range(1,n):  #1,n i=2  i=3
    if(n%i==0):  #5%1==0  2%5==0
        sum=sum+i #0=0+1
if sum==n:
 print("The num is perfect")
else:
 print("Num is not perfect")

