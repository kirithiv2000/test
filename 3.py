array = [ 1,2]
maximum = -10000
secondMax = -10000
for i in array:
    if maximum<i:
        maximum , secondMax = i , maximum
    elif secondMax<i:
        secondMax = i
print("second maximum is = ",secondMax)