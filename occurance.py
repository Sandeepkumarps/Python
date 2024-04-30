n=int(input("Enter the number of elements:"))
num=[]

print("Enter the elements to the matrix:")

for i in range(n):
    num.append(int(input()))

delete=int(input("Enter the element to be removed "))

while delete in num:
    num.remove(delete)
    print(num)
