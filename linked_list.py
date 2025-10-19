class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def search(self,data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False
    
    def remove_beginning(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data
    
    def remove_at_end(self):
        if not self.head:
            return None
        if not self.head.next:
            removed_data = self.head.data
            self.head = None
            return removed_data
        temporary_node = self.head
        while temporary_node.next.next:
            temporary_node = temporary_node.next
        removed_data = temporary_node.next.data
        temporary_node.next = None
        return removed_data

sushi_preparation = LinkedList()
sushi_preparation.insert_at_end("prepare")
sushi_preparation.insert_at_end("roll")
sushi_preparation.insert_at_end("serve")
sushi_preparation.insert_at_beginning("assemble")
sushi_preparation.insert_at_beginning("gather ingredients")

print(sushi_preparation.search("roll"))
print(sushi_preparation.search("ate and left no crumbs"))
print(sushi_preparation.remove_beginning())
print(sushi_preparation.remove_at_end())

