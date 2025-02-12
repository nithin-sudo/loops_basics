# print the multiplication table of a number n
n = int(input("Enter number:"))
i = 1
while i <= 10:
    result = n * i
    #the below statement has f string which simply means we can write our expression
    print(f"{n} * {i} = {result}")
    i += 1
print("Loop ended")