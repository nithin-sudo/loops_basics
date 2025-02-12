# multiplication table of a number n

x = int(input("Enter Number: "))

for i in range(1,11):
    result = x * i
    print(f"{x} x {i} = {result}")