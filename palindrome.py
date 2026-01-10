n=323
num=n
rev=0
while num>0:
    last_digit=num%10
    rev=rev*10+last_digit
    num=num//10
if n==rev:
    print("This numbe is a pallindrom")
else:
    print("This number is not a pallindrom")