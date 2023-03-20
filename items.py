a=input("Enter a number: ")  
b=a.split(',')  
for i in b:
    if int(i)%2==0:
      print("List of items",i)