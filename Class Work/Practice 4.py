my_contact={"name","number"}
def addContact():
    name=input("Enter the contact name: ")
    name=name.strip().title()
    my_contact["name"].append(name)
    num=input("Enter the number: ")
    my_contact["number"].append(num)

def editContact(name,nameedit,numedit):
    name=name.strip().title()
    index=my_contact["name"].index(name)
    my_contact["name"][index]=nameedit
    my_contact["number"][index]=numedit
    return True

print("Contact Management")
print("-"*30)
while True:
    print("-"*30)
    print("Available action\n")
    print("1. Add\n2. Edit\n3. Delete\n4. Search\n5. close")
    action=int(input("Enter your required action number: "))
    if action==1:
        addContact()
    elif action==2:
        name=input("Enter the name to be edited: ")
        nameedit=input("Enter the new name: ")
        numedit=input("Enter the updated contact number: ")
        if editContact(name,nameedit,numedit):
            print("Contact Updated Successfuly")
    elif action==3:
        exit()
