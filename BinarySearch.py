#David Justice
#9-22-16
#Binary Search


def search(myItem,myList):
    
    found = False
    bottom = 0
    top = len(myList)-1
    counter = 0
    
    while bottom<=top and not found:
        middle = (bottom + top) // 2
        counter = counter + 1
        
        if myList[middle] == myItem:
            found = True
            
        elif myList[middle] < myItem:
            bottom = middle + 1
            
        else:
            top = middle - 1


    return found, counter


def start():
    
    numberList = [1,4,6,8,12,15,18,19,24,27,31,42,43,58]
    
    item = int(input("What number are you looking for?"))
    
    isItFound, counter = search(item,numberList)
    
    if isItFound == True:
        print("Your number is there!")
        print("Found after " + str(counter) + " searches.")
    else:
        print("Your number is not there.")

start()
