from heapq import heappop, heappush


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
            print("Item is already in PriorityQueue")
            return

        heappush(self.heap, [priority, item])
        self.count += 1

    def pop(self):
        """
        
        """

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

    def update(self, item, priority):
        """
        
        """

        if not self.isItem(self, item):
            heappush(self.heap, [priority, item])
            self.count += 1
        else:
            for pqItemPriority, pqItem in self.heap:
                if pqItem == item:
                    if pqItemPriority <= priority:
                        print("Item did not update")
                        return
                    else:
                        pqItemPriority = priority

if __name__ == '__main__':
    q = PriorityQueue()