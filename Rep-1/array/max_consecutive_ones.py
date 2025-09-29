a = [1,0,1,0,0,1,1,1,1,0,0,1, 1,1,1,1,1,1,1,1]

max_cnt = cnt = 0
for val in a:
    if val == 0:
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 0
    else:
        cnt += 1

else:
    if cnt > max_cnt:
        max_cnt = cnt
    
print(max_cnt)