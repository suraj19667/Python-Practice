n=4567
num=n
total=0
nod=len(str(n))
while num>0:
    digit=num%10
    total=total+digit**nod
    num=num//10
if total==n:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")