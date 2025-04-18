class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue:", self.queue)

q = Queue()
while True:
    action = input("Enter 'enqueue' to add, 'dequeue' to remove, 'display' to view, or 'exit' to quit: ").strip().lower()
    if action == 'enqueue':
        item = input("Enter item to enqueue: ")
        q.enqueue(item)
    elif action == 'dequeue':
        print("Dequeued:", q.dequeue())
    elif action == 'display':
        q.display()
    elif action == 'exit':
        break
    else:
        print("Invalid input. Please try again.")
