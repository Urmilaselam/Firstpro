#my_tuple = (1,2,3)
#new_tuple = my_tuple + (4,)+ (5,) + my_tuple[1:]
#print(new_tuple)


mytuple=(1,2,3,4)
for i in mytuple:
    evencount=0
oddcount=0
even=0
odd=0
for i in mytuple:
    if(i%2==0):
    
        
        #evencount+=1
        even=even+1
    else:
        #oddcount+=1 
        odd=odd+1
print("even ", evencount,"sum=",even)
print("odd ", oddcount,"odd=",odd)