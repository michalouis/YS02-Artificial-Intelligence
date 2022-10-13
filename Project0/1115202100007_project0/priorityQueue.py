from heapq import heapify, heappop, heappush


class PriorityQueue:

    def __init__(self):
        """
        Initialize priorityQueue by creating
        an empty heap and setting its counter to 0
        """
        self.heap = []
        self.count = 0
    
    def isItem(self, item):
        """
        if item is in priorityQueue return True
        else return False
        """
        for pqItem in self.heap:
            if pqItem == item:
                return True

        return False

    def push(self, item, priority):
        """
        If item isn't already in pq's heap
        insert it and increase pq's couunter by 1
        """

        if self.isItem([priority, item]):
            return

        self.count += 1
        heappush(self.heap, [priority, item])

    def pop(self):
        """
        If heap isn't empty return item and
        decrease pq's counter by 1
        """

        if self.count == 0:
            print("PriorityQueue is empty")
            return None

        self.count -= 1
        item = heappop(self.heap)
        return item[1]

    def isEmpty(self):
        """
        If pq's heap is empty return
        True else return False
        """

        if self.count != 0:
            return False
        else:
            return True

    def removeDuplicates(self):
        """
        Add to an empty list pq's items
        only once and then return list
        
        Note: items with identical content but
        different priority are different items
        """

        list = []
        for pqItem in self.heap:
            if pqItem not in list:
                list.append(pqItem)
            else:
                # if you find a duplicate decrease pq's counter
                self.count -= 1
            
        return list

    def update(self, item, priority):
        """
        Update items' priority only if
        the new priority is smaller than
        the current one, then delete duplicate items

        If no items were updated add the item to the pq
        """

        # update items
        updated = False
        for pqItem in self.heap:
            if pqItem[1] == item:
                if pqItem[0] > priority:
                    pqItem[0] = priority
                    updated = True

        # check for duplicates
        if updated:
            self.heap = self.removeDuplicates()
            return

        # if no items were updated add item to the pq 
        self.count += 1
        heappush(self.heap, [priority, item])

def PQSort(list):
    """
    Put list's items in a pq using the class we just created
    Items are now sorted from small to big inside the pq
    Transfer items from pq back to the list

    List is now sorted because pq pops items from small to big
    """

    pq = PriorityQueue()
    for itemN in range(len(list)):
        item = list.pop()
        pq.push(item, item)

    for itemN in range(pq.count):
        list.append(pq.pop())

    return


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