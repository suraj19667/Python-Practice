n=345678
num=n
while n>0:
    last_digit=n%10
    print(last_digit,end="")
    n=n//10
print("\nThe reverse of",num,"is above :")