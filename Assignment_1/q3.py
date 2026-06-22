
num=int(input("enter the num"))

def print_fibonacci(terms):
    
    a,b=0,1
    
    for in range(terms):
        print(a, end=" ")
        a,b=b,a+b
    print()

print_fibonacci(num)
