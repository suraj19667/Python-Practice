#Calculate the grade accordin to marks
marks=int(input("Enter the marks:"))
if (marks>=90):
    print("Grade A")
elif(marks>=80 and marks<90):
    print("Grade B")
elif(marks>=70 and marks<80):
    print("Grade C")
else:
    print("Grade D")

#Eligible For Vote or Not

age=int(input("Enter The Age:"))
if (age>=18):
    print("Eligible for vote")
else:
    print("Not eligible for vote !")