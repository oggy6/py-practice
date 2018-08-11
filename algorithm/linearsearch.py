import sys
import random
#from random import shuffle

def linearsearch(l, key):
    for index, num in enumerate(l) :
        if num == key:
            return index

    return -1;

if __name__ == '__main__':
    l = list(range(15))
    random.shuffle(l)
    target = random.randrange(0, 14)
    print(l, target)
    res = linearsearch(l, target)
    print(res)
