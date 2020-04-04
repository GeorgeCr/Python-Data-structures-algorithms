from Node import Node


class LinkedStack:
    def __init__(self, limit=10):
        self.head_node = None
        self.size = 0
        self.limit = limit

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        return self.size < self.limit

    def peek(self):
        if not self.is_empty():
            return self.head_node.get_value()
        print('Nothing to see here!')

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.head_node
            self.head_node = item_to_remove.get_link_node()
            self.size -= 1
            return item_to_remove
        print('No items to remove!')

    def push(self, value):
        if self.has_space():
            item_to_add = Node(value)
            item_to_add.set_link_node(self.head_node)
            self.head_node = item_to_add
            self.size += 1
        else:
            print('The stack is full!')


s = LinkedStack()
for i in range(11):
    print('Attempting to add {0}'.format(i))
    s.push(i)
for i in range(11):
    print('Attempting to remove {0}'.format(i))
    s.pop()
