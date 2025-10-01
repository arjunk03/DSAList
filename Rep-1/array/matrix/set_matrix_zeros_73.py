a = [[1,1,1],[1,0,1],[1,1,1]]
a = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]


print(a)
# brute force
rows = len(a)
cols = len(a[0])
for i in range(rows):
    for j in range(cols):
        if a[i][j] == 0:
            tmp_i = 0
            while tmp_i < rows:
                if a[tmp_i][j] != 0:
                    a[tmp_i][j] = float("inf")
                tmp_i += 1

            tmp_j = 0
            while tmp_j < cols:
                if a[i][tmp_j] != 0:
                    a[i][tmp_j] = float("inf")
                tmp_j += 1
    
for i in range(rows):
    for j in range(cols):
        if a[i][j] == float("inf"):
            a[i][j] = 0

print(a)


# Optimal

a = [[1,1,1],[1,0,1],[1,1,1]]
a = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]


print(a)
rows = len(a)
cols = len(a[0])

row_track = [0]*rows
col_track = [0]* cols
for i in range(rows):
    for j in range(cols):
        if a[i][j] == 0:
            row_track[i] = -1
            col_track[j] = -1

for i in range(rows):
    for j in range(cols):
        if row_track[i] == -1 or col_track[j] == -1:
            a[i][j] = 0

print(a)