import myModule as md
student1=md.student("Anbu",95005592)
student1.name="Thamizh"
student1.printStudent()
student2=md.student("Sankar",895677)
student2.printStudent()
student1.name=student2.name
student1.printStudent()
studentObj=[]
for i in range(0,4):
    studentObj.append(md.student(input("Enter Name"),input("Enter Number")))
for i in range(0,len(studentObj)):
    studentObj[i].printStudent()