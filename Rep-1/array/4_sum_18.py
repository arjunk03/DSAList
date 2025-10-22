a = [1,0,-1,0,-2,2]

tgt = 0

# a = [2,2,2,2,2]
# tgt = 8
# optimal
a.sort()

res = set()

for i in range(len(a)):
    for j in range(i+1, len(a)-2):
        k , l = j+1, len(a)-1
        while k < l:
            tmp = a[i] + a[j] + a[k] + a[l]
            if tmp > tgt:
                l -= 1
            elif tmp <  tgt:
                k += 1
            else:
                tmp_res = [a[i] , a[j] , a[k] , a[l]]
                tmp_res.sort()
                res.add(tuple(tmp_res))
                k += 1
                l -= 1

print(res)

# best solution
def findNsum(arr, tgt, N, tmp_res, final_res):
    if len(arr) < N or N < 2:
        return
    
    if N == 2:
        l , r = 0 , len(arr) - 1

        while l < r:
            tmp = arr[l] + arr[r]
            if tmp == tgt:
                final_res.add(tuple(tmp_res + [arr[l], arr[r]]))
                l += 1
                r -= 1

            elif tmp > tgt:
                r -= 1
            else:
                l += 1
    else:
        for i in range(0, len(arr)-N + 1):
            if tgt < arr[i] * N or tgt > arr[-1] * N:
                continue

            findNsum(arr[i+1:], tgt-arr[i], N-1, tmp_res+[arr[i]], final_res)

a.sort()

res = set()
findNsum(a, tgt, 4, [], res)

print(res)