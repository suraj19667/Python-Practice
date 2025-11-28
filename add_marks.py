#Write to enter marks of 3 subjects from the user and store them in  a dictionary.STart with an empty dictionary % add one by one. Use subject name as key & marks as value.
marks={}

phy=int(input("Enter the physics :"))
marks.update({"marks":phy})

math=int(input("Enter the math:"))
marks.update({"maths":math})

eng=int(input("Enter the English Marks:"))
marks.update({"english":eng})

print(marks)