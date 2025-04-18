class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, data):
        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if not current:
            print("Node not found.")
            return
        if prev:
            prev.next = current.next
        else:
            self.head = current.next
        print(f"Deleted node with data: {data}")

ll = LinkedList()
while True:
    action = input("Enter 'insert' to add, 'delete' to remove, 'display' to show, or 'exit' to quit: ").strip().lower()
    if action == 'insert':
        value = int(input("Enter value to insert: "))
        ll.insert(value)
    elif action == 'delete':
        value = int(input("Enter value to delete: "))
        ll.delete(value)
    elif action == 'display':
        ll.display()
    elif action == 'exit':
        break
    else:
        print("Invalid input, try again.")
