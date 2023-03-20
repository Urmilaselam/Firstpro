list=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
countleap=count=0
for i in list:
    if i%4==0:
        #print("Leap year")
        countleap+=1
    else:
        #print("Not leap year")
        count+=1
print("The count of leap years from list are: ",countleap)
print("The count of regular years are: ", count)
 


