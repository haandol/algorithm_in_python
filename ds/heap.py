class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def siftup(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i//2], self.heap_list[i] = self.heap_list[i], self.heap_list[i//2]
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.size += 1
        self.siftup(self.size)

    def siftdown(self, i):
        while (i*2) <= self.size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        if i*2+1 > self.size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i*2
            else:
                return i*2+1

    def pop(self):
        v = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        self.heap_list.pop()
        self.siftdown(1)
        return v

    def build_heap(self, L):
        i = len(L) // 2
        self.size = len(L)
        self.heap_list = [0] + L
        while i > 0:
            self.siftdown(i)
            i -= 1


if '__main__' == __name__:
    heap = BinHeap()
    L = [9, 6, 5, 3, 2]
    heap.build_heap(L)
