from src.heap import binheap
import random
import time
from collections import deque

def siftdown_siftup():
    size = 100000
    input = [(random.randint(0, size), i) for i in range(0, size)]


    start1 = time.time()
    h1 = binheap(input)
    print(f"siftdown elapsed: {time.time() - start1}")

    start2 = time.time()
    h2 = binheap(input, sift_down = False)
    print(f"siftup elapsed: {time.time() - start2}")

def add(d, elem):
    idx = 0
    if len(d) == 0:
        d.append(elem)
    else:
        next = 0
        for i in enumerate(d):
            if elem[0] > i[0]:
                next += 1
            else:
                break
        if next > len(d):
            d.append(elem)
        else:
            d.insert(next, elem)

def simulate():
    size = 1000
    input = [random.randint(0, size) for i in range(0, size)]

    s1 = time.time()
    for _ in range(1000):
        h = binheap()
        for idx, i in enumerate(input):
            if idx > size / 2:
                h.del_min()
            h.insert(i, i)
        while len(h) > 0:
            h.del_min()
    print(time.time() - s1)

    s2 = time.time()
    for _ in range(1000):
        d = deque()
        for idx, i in enumerate(input):
            if idx > size / 2:
                d.popleft()
            add(d, (i, i))
        while len(d) > 0:
            d.popleft()
    print(time.time() - s2)

if __name__ == "__main__":
    # siftdown_siftup()
    simulate()
