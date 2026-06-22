
num=10

for i in range(31,-1,-1):
    bit=(num>>i)&1
    print(bit,end="")

print()

