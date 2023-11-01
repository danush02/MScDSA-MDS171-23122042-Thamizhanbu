class student:
    def __init__(self,name,phone): #Initialize Data Members for the class
        self.name = name
        self.phone = phone
    def printStudent(self):
        print(self.name,self.phone)