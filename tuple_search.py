# search for a number in tuple

nums = (1,4,9,16,25,36,12,11,13,17)
number = 16
i = 0
while (i < len(nums)):
    if(number == nums[i]):
        print("FOUND AT INDEX: ",i)
    # can use break here instead of else so it stops the exec    
    else:
        print("Finding")
    i+=1
print("Loop ended")