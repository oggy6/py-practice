import sys
from random import shuffle

def shell_sort(l):
    h = len(l) // 2
    while h > 0:
        for i in range(h, len(l)):
            j = i
            while j >= h and l[j-h] > l[j]:
                l[j-h], l[j] = l[j], l[j-h]
                j -= h
        h = h // 2

    return l

if __name__ == '__main__' :
    l = list(range(15))
    lcopy = l[:]
    shuffle(l)
    print('Unsorted')
    print(l)
    assert l != lcopy
    print('Sorted')
    print(shell_sort(l))
    assert l == lcopy
