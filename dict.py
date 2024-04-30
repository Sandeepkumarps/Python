mydict={}

len=int(input("Enter the size:"))

for i in range(len):
    name=str(input("Enter name:"))
    rollno=int(input("Enter the rollno:"))
    mydict[rollno]=name

print(mydict)