a = [3,5,7,8,6,4,9,2,1]
target = 22

dct = {}
for val in a:
    if target - val in dct:
        print("Found")
        break
    else:
        dct[val] = 0

else:
    print("Not found")

