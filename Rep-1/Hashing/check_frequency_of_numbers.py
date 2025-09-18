def check_freq(a, b):
    freq_list = [0] * len(a)
    for val in a:
        freq_list[val] += 1

    for val in b:
        if len(freq_list) < val:
            print("val :", val, 0)
        else:
            print("val :", val, freq_list[val])

from collections import defaultdict
def check_freq(a, b):
    freq_list = defaultdict(int)
    for val in a:
        freq_list[val] += 1

    for val in b:
        if len(freq_list) < val:
            print("val :", val, 0)
        else:
            print("val :", val, freq_list[val])


a = [2,3, 5,3,6,8, 9,4, 3, 1, 0, 3, 5]
b = [12, 3, 4, 8, 5, 7, 2, 9, 55, 88]

check_freq(a, b)
