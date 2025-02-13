# grading system in python

marks=int(input("Enter your marks :"))
if(marks>=80 and marks<=100):
    print("Comgratulations , You got A+")
elif(marks>=70 and marks<80):
    print("GPA: A")
elif(marks>=60 and marks<70):
    print("GPA: A-")
elif(marks>=50 and marks<60):
    print("GPA: B")
elif(marks>=40 and marks<=50):
    print("GPA:  C")
elif(marks>=33 and marks<40):
    print("GPA : D")
else:
    print("Failed")
    
    
#checking even an odd
number=int(input("ENter a number to check is it even or odd: "))
if(number%2==0):
    print(number," is even")
else:
    print(number ," is odd")