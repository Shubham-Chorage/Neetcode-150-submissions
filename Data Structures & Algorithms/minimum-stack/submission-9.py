# Linked list behavior as stack

class Node:
    def __init__(self,val,min_val,next = None):
        self.val = val
        self.min = min_val
        self.next = next

class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if not self.head:
            self.head = Node(val,val)
        else:
            self.head = Node(val,min(val,self.head.min),self.head)

    def pop(self) -> None:
        self.head = self.head.next
        

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min
