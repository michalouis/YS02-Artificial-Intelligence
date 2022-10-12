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

    def removeDuplicates(self):
        foundOnce = False
        templist = []
        for pqItem in self.heap:
            if pqItem not in templist:
                templist.append(pqItem)
            else:
                self.count -= 1
            
        heapify(templist)
        return templist

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

if __name__ == '__main__':
    q = PriorityQueue()