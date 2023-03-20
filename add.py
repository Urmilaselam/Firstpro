list= [1,2,3,4,5,6,7,8,3,2,5]
evencount=0
oddcount=0
even=0
odd=0
for i in list:
    if(i%2==0):
    
        
        #evencount+=1
        even=even+1
    else:
        #oddcount+=1 
        odd=odd+1
print("even ", evencount,"sum=",even)
print("odd ", oddcount,"odd=",odd)