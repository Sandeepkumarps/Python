def cmp(a,b,n1,n2):

    if n1==n2:

        for i in range(n1):

            if a[i]==b[i]:
                flag=1
            else:
                flag=0
    else:
        flag=0
        if(flag==1):
            print("same")
        else:
            print("Not same")


a,b=tuple(),tuple()

n1=int(input("Enter the elements of tuple:"))
print("Enter the elements:")
for i in range(n1):
    a+=(int(input()),)


n2=int(input("Enter the elements of tuple:"))
print("Enter the elements:")
for i in range(n2):
    b+=(int(input()),)



print("Maximum of first tuple",max(a))
print("Maximum of second tuple",max(b))
print("minimum of first tuple",min(a))
print("minimum of second tuple",min(b))
compare=cmp(a,b,n1,n2)
