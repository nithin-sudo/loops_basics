# print 1 to 10 even numbers using while

print("Even number from 1 to 10")
i = 1

while (i <= 10):
    if(i % 2 == 0):
        print(i)
        i += 1
        continue
    i +=1


# print 1 to 10 odd number
print("Odd numbers from 1 to 10")
i = 1

while (i <= 10):
    if(i % 2 != 0):
        print(i)
        i += 1
        continue
    i += 1
