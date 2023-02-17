import os as osi
source=("C:\\Users\\PC\\Desktop\\Filesnotes\\dataa1.txt", "w")
dest=open("C:\\:\\Users\\PC\\Desktop\\Filesnotes\data.txt","r")
content=source.read()
dest.write(content)
print("Success")
