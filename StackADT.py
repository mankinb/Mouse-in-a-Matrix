class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def isEmpty(self):
        return self.length == 0
    
    def __len__(self):    
        return self.length
    
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from empty stack."
        x = self.head.data
        self.head = self.head.next
        self.length -= 1
        return x
    
    def peek(self):
        assert not self.isEmpty(), "Cannot peek from empty stack."
        return self.head.data
    
    def push(self, item):
        node = ListNode(item)
        if self.head == None:
            self.head = node
            self.length += 1
        else:
            node.next = self.head
            self.head = node
            self.length += 1

    def __str__(self):
        output = "Top\n_______\n"
        current_node = self.head

        while current_node != None:
            output += str(current_node.data) + "\n"
            current_node = current_node.next
        output += "_______\n"
        return output
