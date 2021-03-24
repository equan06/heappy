from src.heap import binheap

input = [3, 1, 0, 2, 5, 7, 3]
def create_heap():
    return binheap(input)

def test_init():
    h = create_heap()
    assert len(h) == len(input)

def test_pop():
    h = create_heap()
    for i in sorted(input):
        assert h.pop()[0] == i

def test_insert():
    h = create_heap()
    h.insert(4, "A")
    for i in range(5):
        h.pop()
    assert h.pop()[0] == 4

    h.insert(-1, "B")
    assert h.pop()[0] == -1

def test_multiple_insert():
    h = binheap()
    for i in input:
        h.insert(i, i)
    for j in sorted(input):
        assert h.pop()[0] == j