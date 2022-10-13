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

    # PriorityQueue class example
    print("### PriorityQueue class example ###")
    print("Add (""task1"", 1) to PriorityQueue")
    q.push("task1", 1)
    print("q.heap = %s\n" % q.heap)

    print("Remove (""task1"", 1) from PriorityQueue")
    q.pop()
    print("q.heap = %s\n" % q.heap)

    print("Add items to PriorityQueue")
    q.push("task1", 3)
    q.push("task1", 4)
    q.push("task1", 5)
    q.push("task2", 2)
    q.push("task2", 4)
    q.push("task2", 6)
    q.push("task2", 8)
    q.push("task3", 5)
    q.push("task3", 10)
    q.push("task3", 15)
    print("q.heap = %s\n" % q.heap)

    print("Update task2 priority to 3")
    q.update("task2", 3)    
    print("q.heap = %s\n" % q.heap)

    print("Update task3 priority to 4")
    q.update("task3", 4)    
    print("q.heap = %s\n" % q.heap)

    # PQSort function
    print("### PQSort function example ###")
    list = [1, 3, 5, 8, 2, 4, 4, 6, 6, 6, 9, 7]
    print("List before PQsort: %s" % list)
    PQSort(list)
    print("List after PQsort: %s" % list)