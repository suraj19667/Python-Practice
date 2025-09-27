n=153
nol=len(str(n))
ans=0
while n>0:
    digit=n%10
    ans=digit+n**nol
if ans==n:
    print("This is a armstrong number")
else:
    print("This is not a armstrong number")