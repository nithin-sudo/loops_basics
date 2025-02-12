# find the factorial of n natural numbers

number = int(input("Enter a number: "))

factorial = 1
for i in range(1,number + 1):
    factorial = factorial * i

print(f"factorial of the number: {number} is : ",factorial)