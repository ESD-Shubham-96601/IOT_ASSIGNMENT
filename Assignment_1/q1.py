#Write a program to accept two numbers and display division of the two numbers. 
# Check divide by zero error. If divider is zero then display appropriate error message.

dividend = int(input("enter dividend : "))
divisor = int(input("enter divisor : "))

if divisor==0 :
    print(f"cannot divide by zero")
else :
    quo = dividend / divisor
    print(f"quotient = {quo}")