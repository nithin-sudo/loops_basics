# find the factorial of n natural numbers

number = int(input("Enter a number: "))

factorial = 1
i = 1
while (i <= number):
    factorial = factorial * i
    i += 1

print(f"factorial of the number {number} is : ",factorial)