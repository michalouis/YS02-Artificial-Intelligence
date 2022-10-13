from heapq import heapify, heappop, heappush


class PriorityQueue:

    def __init__(self):
        """
    
        
        """
        self.heap = []
        self.count = 0
    
    def isItem(self, item):
        """
        
        """
        for pqItem in self.heap:
            if pqItem == item:
                return True

        return False

    def push(self, item, priority):
        """
        
        """

        if self.isItem([priority, item]):
            return None

        self.count += 1
        heappush(self.heap, [priority, item])

    def pop(self):
        """
        
        """

        if self.count == 0:
            print("PriorityQueue is empty")
            return None

        self.count -= 1
        item = heappop(self.heap)
        return item[1]

    def isEmpty(self):
        """
        
        """

        if self.count != 0:
            return False
        else:
            return True

    def removeDuplicates(self):
        """

        """

        list = []
        for pqItem in self.heap:
            if pqItem not in list:
                list.append(pqItem)
            else:
                self.count -= 1
            
        return list

    def update(self, item, priority):
        """
        
        """

        updated = False
        for pqItem in self.heap:
            if pqItem[1] == item:
                if pqItem[0] > priority:
                    pqItem[0] = priority
                    updated = True

        if updated:
            self.heap = self.removeDuplicates()
            return None

        self.count += 1
        heappush(self.heap, [priority, item])

def PQSort(list):
    """
    
    """

    pq = PriorityQueue()
    for itemN in range(len(list)):
        item = list.pop()
        pq.push(item, item)

    for itemN in range(pq.count):
        list.append(pq.pop())

    return None


if __name__ == '__main__':
    q = PriorityQueue()