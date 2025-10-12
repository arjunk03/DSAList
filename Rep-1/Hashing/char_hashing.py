def check_freq(a, b):
    freq_list = [0] * 26
    for val in a:
        freq_list[ord(val)-ord("a")] += 1

    for val in b:
        print("val :", val, freq_list[ord(val)-ord("a")])

from collections import defaultdict
def check_freq(a, b):
    freq_list = defaultdict(int)
    for val in a:
        freq_list[ord(val)-ord("a")] += 1

        for val in b:
            print("val :", val, freq_list[ord(val)-ord("a")])


a = "arjunistestingr"
b = ["a","r","z"]

check_freq(a, b)
