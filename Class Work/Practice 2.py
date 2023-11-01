import os
nameList=[] #Global Variable
def storeName():
    name=input("Enter the name to be saved: ")
    name=name.strip().title() #Convert to title case (First charc is upper)
    nameList.append(name)
    return name

def listNames():
    print("*"*30)
    print("Names in the List")
    print("*"*30)
    for name in nameList:
        print(name)
    print("*"*30)

def searchName(search):
    search=search.strip().title()
    a=False
    for name in nameList:
        if name==search:
            a=True
            break
    if a:
        print("Name exist in the list")
    else:
        print("Name does not exist in the list")

print("*"*30+"\nName Management System\n"+"*"*30)
while True:
    #os.system('cls')
    print("*"*30)
    print("1.Enter a Name")
    print("2. List the Name")
    print("3. Search for a Name")
    print("4. Exit")
    print("*"*30)

    choice=input("Enter your choice?")
    print("You have entered choice: ",choice)

    if int(choice)==1:
        name=storeName()
        print("Name {} added to list successfully!".format(name))
    elif int(choice)==2:
        listNames()
    elif int(choice)==3:
        name=input("Enter a name to be searched")
        searchName(name)
    elif int(choice)==4:
        exit() #Stop the program execution
    else:
        print("Invalid Option")