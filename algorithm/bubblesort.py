import sys
from random import shuffle

def bubble_sort(l):
    last = len(l) - 1
    for i in range(last, 0, -1):
        for j in range(i):
            if (l[j] > l[j+1]):
                tmp = l[j+1]
                l[j+1] = l[j]
                l[j] = tmp

    return l

if __name__ == '__main__':
    l = list(range(15))
    lcopy = l[:]
    shuffle(l)
    print('Unsorted')
    print(l)
    assert l != lcopy
    print('Sorted')
    print(bubble_sort(l))
    assert l == lcopy
