
filename =input("Enter the filename:")
with open(filename,"w") as f1:
    print("Enter the elements:")
    f1.write(input())

with open(filename,"r") as f2:
    contents = f2.read()
    nlist=contents.split()

for i in range(0,len(nlist)):
    nlist[i]=int(nlist[i])

for i in nlist:
    flag=False
    if i==1:
        print("1 is ne")
    elif i>2:
        for j in range(2,i):
            if(i%j==0):
                flag=True
                break
            if flag==False:
                print(i)