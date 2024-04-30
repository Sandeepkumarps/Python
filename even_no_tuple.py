n=int(input("Enter the number of elements:"))
nums=tuple()
print("Enter the numbers:")
for i in range(n):
    nums+=(int(input()),)

print("Tuple:")
print(nums)

print("even numbers:")

for i in nums:
    if i%2==0:
        print(i)