import random
class sportMart:
    def __init__(self):
        self.main_inventory={}
        self.main_order={}
    
    def displayOrder(self):
        for i in self.main_order:
            print(self.main_order[i])
    
    def displayInventory(self):
        for i in self.main_inventory:
            print(self.main_inventory[i])
    
    def createOrder(self,store,orderID,productID,quantity,price,total):
        orderConformation=False
        if store==1:
            orderConformation=self.reduceQuantity(productID,quantity)
        elif store==0:
            sub_dict={"orderID":orderID,"productID":productID,"Quantity":quantity,"Price":price,"Total":total}
            self.main_order[orderID]=sub_dict
            return True
        if orderConformation:
            sub_dict={"orderID":orderID,"productID":productID,"Quantity":quantity,"Price":price,"Total":total}
            self.main_order[orderID]=sub_dict
            return True
        else:
            return False



    def createInventory(self,productID,Sport,ProductName,Quantity,Price):
        sub_dict={"productid":productID,"sport":Sport,"productname":ProductName,"quantity":Quantity,"price":Price}
        self.main_inventory[productID]=sub_dict

    def reduceQuantity(self,productID,quantity):
        if int(self.main_inventory[productID]["quantity"])>=quantity:
            self.main_inventory[productID]["quantity"]=int(self.main_inventory[productID]["quantity"])-quantity
            return True
        else:
            return False

    def generateOrderID(self):
        orderID="OD00"+str(random.randint(10,100))
        flag=0
        for i in self.main_order:
            if orderID==self.main_order[i]["orderID"]:
                flag=1
        if flag==1:
            self.generateOrderID()
        else:
            return orderID
    
    def returnProductID(self,product):
        for i in self.main_inventory:
            if self.main_inventory[i]["productname"]==product:
                productID=self.main_inventory[i]["productid"]
        return productID
    
    def productPrice(self,product):
        for i in self.main_inventory:
            if self.main_inventory[i]["productname"]==product:
                productPrice=self.main_inventory[i]["price"]
        return productPrice

    def appendToFile(self,odFile,inFile):
        orderFile = open(odFile,"w+")
        orderFile.write("orderID,productID,Quantity,Price,Total\n")
        for i in self.main_order:
            orderFile.write(self.main_order[i]["orderID"]+","+self.main_order[i]["productID"]+","+str(self.main_order[i]["Quantity"])+","+str(self.main_order[i]["Price"])+","+str(self.main_order[i]["Total"])+"\n")
        inventoryFile=open(inFile,"w+")
        inventoryFile.write("productID,Sport,ProductName,Quantity,Price\n")
        for i in self.main_inventory:
            inventoryFile.write(self.main_inventory[i]["productid"]+","+self.main_inventory[i]["sport"]+","+self.main_inventory[i]["productname"]+","+str(self.main_inventory[i]["quantity"])+","+str(self.main_inventory[i]["price"])+"\n")
        print("File Written Successfully!")

