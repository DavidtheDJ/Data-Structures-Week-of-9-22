#David Justice
#9-22-16
#List Search

def listSearch(theList,theItem):
    found = False
    positison = 0

    while positison < len(theList) and not found:
        if theList[positison] == theItem:
            found = True
        positison = positison +1
    return found

def start():
    shopping = ["apples","bananas","beans","candy"]
    item = input("What item do you want to find?")
    
    returned =listSearch(shopping, item)
    
    if returned:
        print("Your item is in the list!")
    else:
        print("Your item is not in the list.")

start()
