from Node import Node


class LinkedQueue:
    def __init__(self, limit=10):
        self.head_node = None
        self.tail_node = None
        self.limit = limit
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        return self.size < self.limit

    def front(self):
        if not self.is_empty():
            return self.head_node.get_value()

    def rear(self):
        if not self.is_empty():
            return self.tail_node.get_value()

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            if self.size == 0:
                self.head_node = item_to_add
                self.tail_node = item_to_add
            else:
                self.tail_node.set_link_node(item_to_add)
                self.tail_node = item_to_add
            self.size += 1
        else:
            print('This queue is full. Please wait.')

    def dequeue(self):
        if not self.is_empty():
            if self.size == 1:
                self.head_node = None
                self.tail_node = None
            elif self.size == 2:
                self.head_node = self.tail_node
            else:
                self.head_node = self.head_node.get_link_node()
            self.size -= 1
        else:
            print('Nothing to remove out of the queue.')


q = LinkedQueue()
print('---ENQUEUE---\n\n')
for i in range(11):
    q.enqueue(i)
    print('Front: {0} Rear: {1}\n'.format(str(q.front()), str(q.rear())))
print('---DEQUEUE---\n\n')
for i in range(11):
    print('Front: {0} Rear: {1}\n'.format(str(q.front()), str(q.rear())))
    q.dequeue()
