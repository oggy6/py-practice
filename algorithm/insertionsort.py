import sys
from random import shuffle

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j-1] > l[j]:
            l[j-1], l[j] = l[j], l[j-1]
            j -= 1

    return l


if __name__ == '__main__':
    l = list(range(15))
    lcopy = l[:]
    shuffle(l)
    print('Unsorted')
    print(l)
    assert l != lcopy
    print('Sorted')
    print(insertion_sort(l))
    assert l == lcopy
