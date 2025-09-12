n=153
nol=len(str(n))
ans=0
while n>0:
    digit=n%10
    ans=digit+n**nol
if ans==n:
    print("armstrong")
else:
    print("not armstrong")