import math
"""
Binary min heap implementation using a Python list, indexed from 0 to n-1

This stores tuples that represent (key, value) pairs, where the key can be any floating point number.

Node i has children at indices 2i+1 and 2i+2, and parent at index floor((i-1)/2).

for discussion on sift up/down - basically, siftDown swaps from the root to the leaves, 
siftUp swaps from the leaves to the root.


Insert uses sift up (place in the next open position in the bottom layer, and then move upwards).
This is necessary since the heap is already sorted at this point, and it makes more sense to add an item 
at the end. The invariant is that everything before the current index is a heap. 

When building a heap from an unsorted array, it turns out that it's faster to sift down, starting from the end.
Here the invariant is that everything after the current index is a heap. This allows heap construction in O(n)
vs O(nlogn).

https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity
"""


class BinHeap():

    def __init__(self):
        self.heap = []
        self.len, self.next_index = 0, 0
    
    def find_min(self):
        if (self.len == 0):
            raise Error
        return self.heap[0][1]

    def insert(self, key, value):
        self.heap.append((key, value))
        self.sift_up(self.next_index)
        self.next_index += 1
        self.len += 1
        print(f"inserted: {(key, value)}")

    def sift_up(self, curr):
        "Sift the element at index curr upwards until the heap property is satisfied for all elements above curr."
        parent = get_parent(curr)
        while parent != -1 and curr > 0 and self.heap[curr][0] < self.heap[parent][0]:
            self.heap[curr], self.heap[parent] = self.heap[parent], self.heap[curr_curr]
            curr, parent = parent, get_parent(parent)

    def sift_down(self, curr):
        "Sift the element at index curr downwards until the heap property is satisfied for all elements below curr."
        min_child = self.get_min_child(curr)
        while min_child != -1 and curr < self.len and self.heap[curr][0] > self.heap[min_child][0]:
            self.heap[curr], self.heap[min_child] = self.heap[min_child], self.heap[curr]
            curr, min_child = min_child, get_min_child(min_child)

    def get_min_child(self, curr):
        # TODO test if this works?
        left, right = 2 * curr + 1, 2 * curr + 2
        if (left >= self.len):
            return -1
        return left if right >= self.len or self.heap[left][0] <= self.heap[right][0] else right

    def get_parent(self, curr):
        if curr == 0:
            return -1
        return math.floor((curr - 1) / 2)
        
    def __str__(self):
        res = ""
        for idx, pair in enumerate(self.heap):
            res += str(pair[0]) + " | "
            if (idx + 2) & (idx + 1) == 0:
                res += "\n"
        return res
    
    

    
if __name__ == "__main__":
    h = BinHeap()
    h.insert(5, "A")
    h.insert(2, "B")
    h.insert(3, "B")
    h.insert(4, "c")
    h.insert(10, "awd")
    h.insert(11, "awd")
    h.insert(2, "awd")
    h.insert(1, "awd")
    h.insert(3, "awd")



    print(h)
    
