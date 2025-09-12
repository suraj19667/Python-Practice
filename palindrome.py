n=567
num=n
result=0
while num>0:
    digit=num%10
    result=result*10+digit
    num=num//10
if n==result:
    print("palindrome")
else:
    print("not a palindrome")