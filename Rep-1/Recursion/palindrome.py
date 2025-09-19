# iteration
def pal(s):
    l, r = 0, len(s) -1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -=1

    return True


a = "malayalam"
print(pal(a))


# ercursion
def pal(s, l , r):
    if l >= r:
        return True

    if s[l] != s[r]:
        return False
    
    return pal(s, l+1, r-1)


a = "malayalam"
print(pal(a, 0, len(a) -1))
