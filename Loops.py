#While loop

# 1.print number

# i=1
# while i<10:
#     i+=1
#     print(i)

#Find the numbr in tuple
nums=(3,4,5,6,6,5,4,3,5,6,5)
x=9
i=1
while i<len(nums):
    if (nums[i]==x):
        print("found")
    else:
        print("please enter valid number")
    i+=1