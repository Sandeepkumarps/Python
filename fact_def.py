def factorial(n):
    i=1
    fact=1
    while i<n+1:
        fact=fact*i
        i+=1
    return fact

n=int(input("Enter a number:"))
print(factorial(n))