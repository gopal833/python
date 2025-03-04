n=int(input("enter the first number:"))
m=int(input("enter the second number:"))
operator = input("enter the operator (+, -, *, /): ")
for i in range(1):
    if operator=="+":
            print(n+m,)
    elif operator=="-":
            print(n-m)
    elif operator=="*":
          print(n*m)
    elif operator=="/":
            print(n/m)
    else:
            print("invalid operation")


