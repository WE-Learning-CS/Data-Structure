class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        index = len(self.data) -1 # 마지막 인덱스
        
        while index != 1:
            parentNode = index // 2
            
            if self.data[parentNode] < self.data[index]:
                self.data[parentNode], self.data[index] = self.data[index], self.data[parentNode]
                index = parentNode
            
            else:
                break

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1] 
            data = self.data.pop(-1) 

        else:
            data = None

        return data
    
    def maxHeapify(self, i):
        left     = i * 2
        right    = i * 2 + 1
        smallest = i

        if left < len(self.data) and self.data[left] > self.data[smallest]:
            smallest = left
        
        if right < len(self.data) and self.data[right] > self.data[smallest]:
            smallest = right
        
        if smallest != i:
            self.data[smallest], self.data[i] = self.data[i], self.data[smallest]
            self.maxHeapify(smallest)
        
    def heapSort(unsorted):
        H = MaxHeap()
        for item in unsorted:
            H.insert(item)

        sorted = []
        d = H.remove()

        while d:
            sorted.append(d)
            d = H.remove()

        return sorted
            