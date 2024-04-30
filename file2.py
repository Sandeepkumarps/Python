filename=input("Enterr the filename:")

with open(filename,"w") as f1:
    print("Enter the elements:")
    f1.write(input())
    f1.close()

with open(filename,"r") as f2:
    contents=f2.read()
    nlist=contents.split()

    uppercount=0
    lowercount=0
    digitcount=0

    for ch in contents:
        if ch.isupper():
            uppercount+=1
        if ch.islower():
            lowercount+=1
        if ch.isdigit():
            digitcount+=1

print(uppercount)
print(lowercount)
print(digitcount)
print(len(nlist))
