import sys
from random import shuffle

def merge_sort(l):
    sorted_list = []
    while len(sorted_list) != len(l) :
        a, b = devide(l)

    return l


def merge_sort(l):
    if (len(l) <= 1):
        return l

    d = len(l) // 2
    a = l[:d]
    b = l[d:]
    left = merge_sort(a)
    right = merge_sort(b)

    return list(merge(left, right))


def merge(a, b):
    c = []
    print(a, b)
    while len(a) > 0 and len(b) > 0:
        if (a[0] < b[0]):
            c.append(a[0])
            a.pop(0)
        else:
            c.append(b[0])
            b.pop(0)

    if (len(a) > 0):
        c.extend(a)
    else:
        c.extend(b)

    return c


if __name__ == '__main__':
    l = list(range(7))
    lcopy = l[:]
    shuffle(l)
    print('Unsorted')
    print(l)
    assert l != lcopy
    print('Sorted')
    print(merge_sort(l))
    assert l == lcopy
