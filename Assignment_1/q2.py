#2. Write a program to accept 5 digit number and check whether it is a numeric palindrome. 
# (if reversed number is same as entered number it is called as palindrome)

num = int(input("enter 5 digit number : "))

temp = num
rev = 0
while(temp > 0) :
    mod = temp % 10
    rev = rev * 10 + mod
    temp = temp //10

print(f"reverse number : {rev}")

if num == rev :
    print(f" {num} is palindrome number ")
else :
    print(f"{num} is not palindrome")


