name = input("Enter a name of student: ")
marks = float(input("Enter a marks: "))
if (marks >=90):
    print ("grade A")
elif (marks >=80 and marks < 90):
    print("grade B")
elif (marks >= 70 and marks < 80):
    print("grade c")
elif (70 > marks):
    print("grade D")
else:
    print("student fail")
print("Name of student: " , name)
 