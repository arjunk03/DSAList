a = [3,23,4,56,5,3,4,6]

larg = float("-inf")
s_larg = float("-inf")
for val in a:
    if val > larg:
        s_larg = larg
        larg = val
    elif val > s_larg and val < larg:
        s_larg = val

print("large:", larg)
print("s_larg :", s_larg)