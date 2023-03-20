print("Enter decimal num: ")  #9
dnum=int(input())  #9
bnum=0
mul=1
while dnum>0:               #6>0      3>0         1>0
    rem=dnum%2            #6%2=0      3%2=1       1%1=0
    bnum=bnum+(rem*mul)  #0=0+0*1=0   0=0+1*10=10  10+0*100=10
    mul=mul*10           #1*10=10     10*10=100     
    dnum=int(dnum/2)      #6/2=3      3/2=1
print("equivalent binary number: ",bnum)  #0