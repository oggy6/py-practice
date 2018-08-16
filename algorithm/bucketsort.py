import sys
from random import shuffle

def bucket_sort(l):
    bucket = [0 for i in range(len(l))]

    for i in range(0, len(l)):
        bucket[l[i]] = 1

    res = []
    for j in range(len(bucket)):
        if bucket[j] == 1:
            res.append(j)

    return res


if __name__ == '__main__':
    l = list(range(15))
    lcopy = l[:]
    shuffle(l)
    print('Unsorted')
    print(l)
    assert l != lcopy
    print('Sorted')
    l = bucket_sort(l)
    print(l)
    assert l == lcopy
