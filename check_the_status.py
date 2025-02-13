def check_status(a,b):
    flag=True
    if(a<0 or b<0):
        flag=False
        print(flag)
    else:
        flag=True
        print(flag)

a=int(input("Enter the first number : "))
b=int(input("Enter the secons number : "))   

check_status(a,b)
     
            