import sys
from random import shuffle

def quick_sort(l):
    if len(l) < 1:
        return l

    pivot = l[0]
    left = []
    right = []
    for x in range(1, len(l)):
        if (l[x] < pivot):
            left.append(l[x])
        else:
            right.append(l[x])

    left = quick_sort(left)
    right = quick_sort(right)
    middle = [pivot]

    return left + middle + right


if __name__ == '__main__':
    l = list(range(15))
    lcopy = l[:]
    shuffle(l)
    print('Unsorted')
    print(l)
    assert l != lcopy
    print('Sorted')
    print(quick_sort(l))
    assert l == lcopy
