
num1=int(input("enter first number"))
num2=int(input("enter the second number"))
opr=input("enter which operation to perform")

match opr:
    case '+' :
        print(f"the sum is {num1+num2}")
    case '-' :
        print(f"the difference is {num1-num2}")
    case '*' :
        print(f"the product is {num1*num2}")
    case '/' :
        print(f"the div is {num1/num2}")
    case _:
        print("invalid output")