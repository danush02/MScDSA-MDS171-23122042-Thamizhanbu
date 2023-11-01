import sportMart as sm

trinity_store=sm.sportMart()
store=0
for i in open("E:\Practice codes\python_codes_Thamizhanbu\Module Creation\Sport Mart Class\sportMart_OrderDetails.csv","r+").readlines():
            line=i.split(",")
            if not("Quantity" in line):
                trinity_store.createOrder(store,line[0],line[1],line[2],line[3],line[4].strip())

for i in open("E:\Practice codes\python_codes_Thamizhanbu\Module Creation\Sport Mart Class\sportMart_Inventory.csv","r+").readlines():
            line=i.split(",")
            if not("Quantity" in line):
                trinity_store.createInventory(line[0],line[1],line[2],line[3],line[4].strip())

print("Welcome to the Trinity Store")

while True:
    action=int(input("Select your required action:\n1.Create Order\n2.Display Order\n3.Display Inventory\n4.Exit\n"))
    if action==1:
        print("Available Products")
        num=0
        productName=[]
        for i in trinity_store.main_inventory:
            if int(trinity_store.main_inventory[i]["quantity"])>0:
                num+=1
                print(num,".",trinity_store.main_inventory[i]["productname"])
                productName.append([num,trinity_store.main_inventory[i]["productname"]])
        product=int(input("Enter the required product number:"))
        for i in productName:
            if i[0]==product:
                pname=i[1]
                productID=trinity_store.returnProductID(pname)
        orderID=trinity_store.generateOrderID()
        quantity=int(input("Enter the quantity purchased:"))
        price=int(trinity_store.productPrice(pname))
        total=price*quantity
        store=1
        conformation=trinity_store.createOrder(store,orderID,productID,quantity,price,total)
        if conformation:
             print("Order created successfully!")
        else:
             print("Order can't be created order quantity is more than inventory quantity") 
    elif action==2:
        trinity_store.displayOrder()
    elif action==3:
        trinity_store.displayInventory()
    elif action==4:
         trinity_store.appendToFile("E:\Practice codes\python_codes_Thamizhanbu\Module Creation\Sport Mart Class\sportMart_OrderDetails.csv","E:\Practice codes\python_codes_Thamizhanbu\Module Creation\Sport Mart Class\sportMart_Inventory.csv")
         exit()


# filname="Ord.csv"
# createOrder(fileName)

#def creatordr(fileName)
#for i in open(fileName,"r+").readline()
    