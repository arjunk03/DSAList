a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

n = len(a)
LEFT = TOP = 0
BOTTOM , RIGHT = n - 1, len(a[0]) - 1

res = []

while LEFT <= RIGHT and TOP <= BOTTOM:
    # LEFT to RIGHT
    for i in range(LEFT, RIGHT+1):
        res.append(a[TOP][i])
    
    TOP += 1

    #RIGHT to BOTTOM
    for i in range(TOP, BOTTOM+1):
        res.append(a[i][RIGHT])
    
    RIGHT -= 1

    if TOP <= BOTTOM:
        #RIGHT to LEFT
        for i in range(RIGHT,LEFT-1, -1):
            res.append(a[BOTTOM][i])
        
        BOTTOM -= 1

    if LEFT <= RIGHT:
        #BOTTOM to TOP
        for i in range(BOTTOM, TOP-1, -1):
            res.append(a[i][LEFT])
        
        LEFT += 1

print(res)