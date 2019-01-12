class Node:
    def __init__(self, val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self): 
        self.head = None

    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node

    def deleteNode(self, value):
        while(temp!=None):
            if temp.val==value:
                if prev:
                    prev.next=temp.next
                else:
                    head = temp.next
                return
        return
        curr=head
        while(curr!=None):
            print(curr.val)
            curr=curr.next

llist = LinkedList()
llist.push(7)