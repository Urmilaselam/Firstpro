list=[1,2,3,4,5,6]
counteven=0
countodd=0
for i in list:
    if i%2==0:
         counteven +=1
    else:
        countodd +=1
print("Count of even numbers: ", counteven)
print("Count of odd numbers: ", countodd)