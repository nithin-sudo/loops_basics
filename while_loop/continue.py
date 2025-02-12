# this is actually a tricky one, it does not work as expected currently
# because i purposely made some error. 

i = 0
while(i <= 5):
    if(i == 3):
        # here
        continue
    print(i)
    i += 1