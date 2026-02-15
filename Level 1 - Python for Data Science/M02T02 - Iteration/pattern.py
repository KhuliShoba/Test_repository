# Arrow pattern
for x in range (1,6):
    print("* " * x)
    if x >= 5: 
        for y in range (1,4):
            k = x - y
            print("* " * k) 
            