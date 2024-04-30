def area(r,h):
    print("surface area of cylinder:",(2*3.14*r*r)+(2*3.14*r*h))
    print("Volume of cylinder:",(3.14*r*r*h))

r=int(input("Enter the radius:"))
h=int(input("Enter the height:"))
area(r,h)