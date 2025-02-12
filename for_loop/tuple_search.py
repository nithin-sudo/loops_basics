nums = (1,4,9,16,25,36,49,64,81,100,49)

x = 49
index = 0
for num in nums:
    if (num == x):
        print("FOUND at index: ",index)
        break
    index += 1
