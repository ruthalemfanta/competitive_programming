class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.tail = None
        self.size = 0


    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr_index = 0
        curr_node = self.dummy.next

        while curr_index < index:
            curr_node = curr_node.next
            curr_index += 1

        return curr_node.val

        

    def addAtHead(self, val: int) -> None:
        head = self.dummy.next
        new_node = Node(val)
        self.dummy.next = new_node
        new_node.next = head

        self.size += 1
        
        #update the tail
        if not self.tail:
            self.tail = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail:
            self.dummy.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node   

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 

        if index == self.size:
            self.addAtTail(val)
        else:
            curr_index = 0
            curr_node = self.dummy

            while curr_index < index:
                curr_node = curr_node.next
                curr_index += 1

            new_node = Node(val)
            new_node.next = curr_node.next
            curr_node.next = new_node
            self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return 
        curr_index = 0
        curr_node = self.dummy

        while curr_index < index:
            curr_node = curr_node.next
            curr_index += 1

        curr_node.next = curr_node.next.next

        if not curr_node.next:
            self.tail = curr_node

        self.size -= 1 



        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)