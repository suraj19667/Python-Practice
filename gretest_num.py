num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number:"))

if(num1>=num2 and num1>=num3):
    print("first numer is largest")
elif(num2>=num3):
    print("second numbr is largest")
else:
    print("third number is largest")