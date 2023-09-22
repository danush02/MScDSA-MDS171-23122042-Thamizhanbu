#Date:22/09/23
#Lab 09 - Program to read and write data from and to csv file. Calculate total from the data.

class expenseTracker: #Class Declaration
    def __init__(self): #Object Initiation
        self.transactionDetails={"details":[]} #Dictionary to save data

#Function to retrieve data from csv and save in dictionary
    def retrieveTransactions(self):
        for i in open("E:\Python Programming\GitHub\MScDSA-MDS171-23122042-Thamizhanbu\Lab 09\Expense_Income_Tracker.csv","r+").readlines():
            line=i.split(",")
            if line[1]!="Expense Category":
                transaction={"type":line[0],"category":line[1],"amount":line[2],"description":line[3],"date":line[4]}
                self.transactionDetails["details"].append(transaction)

#Function to Caluclate Total from Dictionary file
    def calculateTotal(self):
        totalIncome=0
        totalExpense=0
        for i in self.transactionDetails["details"]:
            if i["type"]=="Income":
                totalIncome+=int(i["amount"])
            else:
                totalExpense+=int(i["amount"])
        return totalIncome,totalExpense
    
    #Function to add new transaction to dictionary
    def addTransaction(self,type,category,amount,description,date):
        transaction={"type":type,"category":category,"amount":amount,"description":description,"date":date}
        self.transactionDetails["details"].append(transaction)
    
    #Function to write data from dictionary to csv
    def writeTransactions(self):
        file=open("E:\Python Programming\GitHub\MScDSA-MDS171-23122042-Thamizhanbu\Lab 09\Expense_Income_Tracker.csv","w+")
        file.write("Type,Expense Category,Amount,Description,Date\n")
        for i in self.transactionDetails["details"]:
            date=str(i["date"]).strip()
            file.write(i["type"]+","+i["category"]+","+i["amount"]+","+i["description"]+","+date+"\n")
        file.close()

#Object declaration
order=expenseTracker()
order.retrieveTransactions()
while True:
    print("1.Add New Transaction\n2.Calculate Total Income and Expense\n3.Exit")
    choice=int(input("Select your action:"))
    if choice==1:
        type=input("Enter the type of transaction (Income/Expense):")
        category=input("Enter the category:")
        amount=input("Enter the amount:")
        description=input("Enter the description of transaction:")
        date=input("Enter the date mm/dd/yyyy:")
        order.addTransaction(type,category,amount,description,date)
    elif choice==2:
        totalIncome,totalExpense=order.calculateTotal()
        print("Total Income=",totalIncome,"\nTotal Expense=",totalExpense)
        order.writeTransactions()
    elif choice==3:
        order.writeTransactions()
        exit()
    