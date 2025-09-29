a = [-2, 1, -3, 4, -1, 2, 1 , -5, 4]

max_sm  = float("-inf")
total = 0

for val in a:
    total += val
    if total > max_sm :
        max_sm = total
    if total < 0:
        total = 0

max_sm = max(max_sm, total)

print(max_sm)