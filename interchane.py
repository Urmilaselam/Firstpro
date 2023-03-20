def swapList(newList):
    newList[0],newList[3]= newList[3], newList[0]
    return newList
newList=[12,35,9,56,24]
print(swapList(newList))