def fibonocci(n):
    first=0
    second=1
    next=0
    print(first)
    print(second)
    while next<n:
        next=first+second
        first=second
        second=next
        print(next)

n=int(input("Enter the limit"))
fibonocci(n)
