r=int(input("Enter the row of matrix:"))
c=int(input("Enter the col of matrix:"))

print("Enter the elements of first matrix:")
matrix1=[[int(input())for i in range(c)]for i in range(r)]
print("Matrix 1")
for n in matrix1:
    print(n)

print("Enter elements of second matrix:")
matrix2=[[int(input()) for i in range(c)] for i in range(r)]
print("Matrix 2")
for n in matrix2:
    print(n)

Result=[[0 for i in range(c)] for j in range(r)]
print("Result:")
for i in range(r):
    for j in range(c):
            Result[i][j]=matrix1[i][j]+matrix2[i][j]

for n in Result:
    print(n)