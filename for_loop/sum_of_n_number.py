# find sum of n numbers

number = int(input("Enter number: "))
sum = 0

for i in range(1, number+1):
    sum = sum + i

print("total sum = ",sum)