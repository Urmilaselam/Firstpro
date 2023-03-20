#year=int(input("Enter any year: "))
countleap=count=0
for i in range(2000,2020):
    if i%4==0:
        print("Leap year")
        countleap+=1
    else:
        print("not leap")
        count+=1

print("Leap years are: ",countleap)
print("Not leap years are", count)