import sys
import random

def binary_search(l, key):
    low = 0
    high = len(l) - 1
    while(low <= high):
        mid = (low + high) // 2
        if (key == l[mid]):
            print('find!')
            return True
        elif (key < l[mid]):
            high = mid - 1
        elif (key > l[mid]):
            low = mid + 1

    print('not find')
    return False

if __name__ == '__main__':
    l = list(range(15))
    target = random.choice(l)
    print(binary_search(l, target))
    print(target)
