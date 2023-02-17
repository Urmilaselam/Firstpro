Number = 100

while(Number <= 200): #100<=200 T
    count = 0  #count=0
    i = 2  #i=2
    while(i <= Number//2):  #i<=100/2=50  
        if(Number % i == 0):  #n%2==0
            count = count + 1  #0=0+1
            break  #br
        i = i + 1  
    if (count == 0 and Number != 1):  #c=0 and 100!=1
        print(" %d" %Number, end = '  ')  
    Number = Number  + 1