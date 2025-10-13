# linked_list.py

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def remove_from_tail(self):
        if self.is_empty():
            return None
        
        removed_data = self.tail.data
        if self.head == self.tail: # Only one node
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return removed_data

    def get_all_data(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def __str__(self):
        return " -> ".join(str(data) for data in self.get_all_data())

# --- Basic Test (Optional, for verification) ---
if __name__ == "__main__":
    ll = DoublyLinkedList()
    print("Is empty:", ll.is_empty()) # True

    ll.insert_at_head((1, 2))
    ll.insert_at_head((0, 2))
    print("After inserting (0,2), (1,2):", ll) # (0, 2) -> (1, 2)
    print("Length:", ll.length) # 2

    ll.insert_at_head((-1, 2))
    print("After inserting (-1,2):", ll) # (-1, 2) -> (0, 2) -> (1, 2)
    print("Length:", ll.length) # 3

    removed = ll.remove_from_tail()
    print("Removed from tail:", removed) # (1, 2)
    print("After removing tail:", ll) # (-1, 2) -> (0, 2)
    print("Length:", ll.length) # 2

    ll.remove_from_tail()
    ll.remove_from_tail()
    print("After removing all:", ll) # (empty string)
    print("Length:", ll.length) # 0
    print("Is empty:", ll.is_empty()) # True