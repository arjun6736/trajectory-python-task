while True:
    num1 = float(input("Enter first number: "))
    opr = input("choose one /,*,-,+ : ")
    num2 = float(input("Enter second number: "))

    if opr=="/":
        print(num1/num2)
    elif opr=="*":
        print(num1*num2)
    elif opr=="-":
        print(num1-num2)
    elif opr=="+":
        print(num1+num2)
    else:
        print("Somthing rong tryagin")