a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

n = len(a)
LEFT = TOP = 0
BOTTOM = RIGHT = n - 1

res = []
# LEFT to RIGHT
for i in range(RIGHT+1):
    res