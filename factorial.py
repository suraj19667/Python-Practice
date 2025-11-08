num=int(input("Enter the number:"))
result=[]

for i in range(1,num+1):
    if num%i==0:
        result.append(i)

print(result)

# -------------------- Batter Solution second method -----------------------

num=int(input("Enter the number:"))
result=[]
for i in range(1,num//2+1):
    if num%i==0:
        result.append(i)
result.append(num)
print(result)

# -----------------  Optimal Solution third method.  -----------------------------

# from math import sqrt
# num=int(input("Enter the number:"))
# result=[]
# for i in range(1,int(sqrt(num)+1)):
#     if num%i==0:
#         result.append(i)
#         if num//i !=i:
#             result.append(num//i)
# result.sort()
# print(result)