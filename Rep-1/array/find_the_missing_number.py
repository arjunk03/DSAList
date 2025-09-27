a = [1,2,3,4,5,0,7,8,9]

dct = {}
for i in range(0, len(a)+1):
    dct[i] = 0

for val in a:
    dct[val] = 1

print([key for key, val in dct.items() if not val ])
     
# optimal solution
a = [1,2,3,4,5,0,7,8,9]
sm = sum(a)
tot_n = (len(a) * (len(a)+1))/2
diff = tot_n - sm
print(diff)