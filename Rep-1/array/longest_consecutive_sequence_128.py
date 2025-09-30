a = [1, 99, 101, 98, 2, 5, 3, 100]

a = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1, 1, 102]

# a = [1,0,1,2]
# a = [0]

# better solution
a.sort()
count = max_cnt = 0
print(a)
i = 0
# while i < len(a):
#     if i and a[i] - a[i-1] == 1:
#         count += 1
#     elif i and a[i] - a[i-1] == 0:
#         i += 1
#         continue
#     else:
#         count = 1
#     max_cnt = max(max_cnt, count)
    
#     i += 1

# print(max_cnt)


# optimal
new = set()
for val in a:
    new.add(val)

count = max_cnt = 0
for val in new:
    val_c = val
    if val - 1 in new:
        continue

    count = 1
    while val_c + 1 in new:
        count += 1
        val_c += 1
        
    max_cnt = max(max_cnt, count)

print(max_cnt)
