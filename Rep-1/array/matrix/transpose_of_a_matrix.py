
a = [ [1,2,3], [4,5,6], [7,8,9]]

rows = len(a)
cols = len(a[0])
new_a = [[0]*rows for _ in range(cols)]
for i in range(rows):
    for j in range(cols):
        new_a[j][i] = a[i][j]

print(new_a)