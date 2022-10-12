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

    def update(self, item, priority):
        """
        
        """

        # if not self.isItem([priority, item]):
        #     heappush(self.heap, [priority, item])
        #     self.count += 1
        # else:
        #     for pqItemPriority, pqItem in self.heap:
        #         if pqItem == item:
        #             if pqItemPriority <= priority:
        #                 print("Item did not update")
        #                 return None
        #             else:
        #                 pqItemPriority = priority

        for pqItem in self.heap:
            if pqItem[1] == item:
                if pqItem[0] <= priority:
                    print("Item did not update")
                    return None
                else:
                    pqItem[0] = priority
                    return None

        self.count += 1
        heappush(self.heap, [priority, item])

if __name__ == '__main__':
    q = PriorityQueue()