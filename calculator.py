# calculator in python

x=int(input("Enter the first number:"))
y=int(input("Enter the secodn number:"))
add=int(input("Plese Select : 1 for addition , 2 for substraction, 3 for multiplication , 4 for division:"))

if (add==1):
    print("addition ",x+y)
elif(add==2):
    print("Substraction",x-y)
elif(add==3):
    print("Multiplication",x*y)
elif(add==4):
    print("Division",x/y)
else:
    print("Please enter valid input")