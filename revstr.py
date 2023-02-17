str='abcd'
print("The original string is:",str) #abcd
rev_str=' ' #Empty string
count=len(str)  #count the number of letters= 4(abcd)
while count>0:  #While count(4>0) (3>0) (2>0) (1>0) (0>0 false)
    rev_str+=str[count-1]  #rev_str+=str[4-1=3d-1=2c=1b-1=0a d will print because u=index starts from 0]
    count=count-1 #4-1=3-1=2-1=1-1=0
print("The reversed string is: ",rev_str)