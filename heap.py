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

    def __init__(self, input_list = [], sift_down = True):
        "Assume that input_list is a list of (key, value) tuples. "
        self.len, self.next_index = len(input_list), len(input_list)
        self.build_heap(input_list, sift_down)

    def build_heap(self, input_list, sift_down = True):
        "Build the heap from an unsorted list."
        self.heap = input_list[:]
        if sift_down:
            for i in reversed(range(0, self.len)):
                self._sift_down(i)
        else:
            for i in range(0, self.len):
                self._sift_up(i)

    def insert(self, key, value):
        self.heap.append((key, value))
        self._sift_up(self.next_index)
        self.next_index += 1
        self.len += 1

    def _sift_up(self, curr):
        "Sift the element at index curr upwards until the heap property is satisfied for all elements above curr."
        parent = math.floor((curr - 1)/2)
        while curr > 0 and self.heap[curr][0] < self.heap[parent][0]:
            self.heap[curr], self.heap[parent] = self.heap[parent], self.heap[curr]
            curr, parent = parent, math.floor((parent - 1)/2)

    def _sift_down(self, curr):
        "Sift the element at index curr downwards until the heap property is satisfied for all elements below curr."
        child = 2*curr + 1
        while child < self.len:
            right = child + 1
            if right < self.len and self.heap[child][0] > self.heap[right][0]:
                child = right
            if self.heap[curr][0] < self.heap[child][0]:
                break
            self.heap[curr], self.heap[child] = self.heap[child], self.heap[curr]
            curr, child = child, 2*child + 1
    
    def del_min(self):
        self.next_index -= 1
        self.len -= 1
        self.heap[0], self.heap[self.next_index] = self.heap[self.next_index], self.heap[0]
        self.heap.pop()
        self._sift_down(0)
        
    def __str__(self):
        res = ""
        for idx, pair in enumerate(self.heap):
            res += str(pair[0]) + " | "
            if (idx + 2) & (idx + 1) == 0:
                res += "\n"
        return res
        
    def __len__(self):
        return self.len
    
    def print_arr(self):
        print(self.heap)
    

    
if __name__ == "__main__":
    h = BinHeap([(5,"a"), (2, "B"), (3, "C"), (4, "d")])
    print(h)
    
