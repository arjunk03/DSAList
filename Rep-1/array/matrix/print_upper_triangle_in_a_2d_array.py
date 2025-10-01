a = [ [1,2,3], [4,5,6], [7,8,9]]

rows = len(a)
cols = len(a[0])
for i in range(rows):
    for j in range(cols):
        if j >= i:
            print(a[i][j], end=" ")
        else:
            print("*", end=" ")
    print()