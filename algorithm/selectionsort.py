import sys
from random import shuffle

def selectionsort(l) :
    n = len(l)
    for index in range(n-1) :
        minIndex = index
        for x in range(index+1,n) :
            if (l[minIndex] > l[x]) :
                minIndex = x
        tmp = l[minIndex]
        l[minIndex] = l[index]
        l[index] = tmp
    return l


if __name__ == '__main__' :
    l = list(range(15))
    lcopy = l[:]
    shuffle(l)
    print('Unsorted')
    print(l)
    assert l != lcopy
    print('Sorted')
    print(selectionsort(l))
    assert l == lcopy
