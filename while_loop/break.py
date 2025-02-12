# search for a number in tuple
#break
nums = (1,4,9,16,25,36,12,11,13,17)
number = 16
i = 0
while (i < len(nums)):
    if(number == nums[i]):
        print("FOUND AT INDEX: ",i)
        break
    i+=1
print("Loop ended")

