# Priority Queue in Python
# https://www.geeksforgeeks.org/priority-queue-in-python/


class BinaryHeap:
    def __init__(self):
        self.d = 2
        self.heap = []

    def __str__(self):
        return ' '.join([str(i) for i in self.heap])

    def isEmpty(self):
        return len(self.heap) == 0

    def parent(self, i):
        return int((i - 1) / self.d)

    def kthChild(self, i, k):
        return self.d * i + k

    def maxChild(self, i):
        leftChild = self.kthChild(i, 1)
        rightChild = self.kthChild(i, 2)
        if rightChild >= len(self.heap):
            return leftChild
        return leftChild if self.heap[leftChild] > self.heap[rightChild] else rightChild

    def findMax(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def insert(self, data):
        self.heap.append(data)
        index = len(self.heap) - 1
        while (index > 0 and self.heap[index] > self.heap[self.parent(index)]):
            self.heap[index] = self.heap[self.parent(index)]
            index = self.parent(index)
        self.heap[index] = data

    def deleteMax(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap[0]

        maxElement = self.heap[0]
        tmp = self.heap[-1]
        self.heap[0] = tmp
        del self.heap[-1]

        index = 0
        while (self.kthChild(index, 1) < len(self.heap) and tmp < self.heap[self.maxChild(index)]):
            self.heap[index] = self.heap[self.maxChild(index)]
            index = self.maxChild(index)
        self.heap[index] = tmp
        return maxElement


bh = BinaryHeap()
bh.insert(10)
bh.insert(20)
bh.insert(19)
bh.insert(17)
print(bh)
d = bh.deleteMax()
print(d)
print(bh)
