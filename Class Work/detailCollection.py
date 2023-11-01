details_dict={"name":[],"regno":[],"phone":[],"email":[]}
def addDetails():
    name=input("Enter the Name: ")
    name=name.strip().title()
    regno=input("Enter the Reg No.: ")
    regno=regno.strip()
    phone=input("Enter the Phone No.: ")
    phone=phone.strip()
    email=input("Enter the MailID: ")
    email=email.strip().lower()
    return True
def searchDetails(regno):
    for no in details_dict["regno"]:
        if regno==no:
            ind=details_dict["regno"]
while True:
    print("*"*30,"\nEnter your choice\n","*"*30)
    print("1. Enter Details")
    print("2. Search Reg. No")
    print("3. Display Details")
    print("4. Exit")
    choice=input("Choice: ")
    if choice==1:
        if addDetails:
            print("Values got added successfully!")
    elif choice==2:
        regno=input("Enter the Reg No. to be searched: ")
        searchDetails(regno)


