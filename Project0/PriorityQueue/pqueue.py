from heapq import heappop, heappush


class pq:

    def __init__(self):
        """
    
        
        """
        self.heap = []
        self.count = 0
    
    def isItem(self, item):
        """
        
        """
        for pqItem in self:
            if pqItem == item:
                return True

        return False

    def push(self, item, priority):
        """
        
        """

        if self.isItem(self, (priority, item)):
            print("Item is already in PriorityQueue")
            return

        heappush(self, (priority, item))
        self.count += 1

    def pop(self):
        """
        
        """

        heappop(self)
        self.count -= 1

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
            heappush(self, item)
        else:
            for pqItemPriority, pqItem in self:
                if pqItem == item:
                    if pqItemPriority <= priority:
                        print("Item did not update")
                        return
                    else:
                        pqItemPriority = priority