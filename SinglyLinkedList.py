from Node import Node


class SinglyLinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def get_head_node(self):
        return self.head_node

    def insert_node(self, node_data):
        new_node = Node(node_data)
        new_node.set_link_node(self.get_head_node())
        self.head_node = new_node

    def print_nodes(self):
        current_node = self.get_head_node()
        while current_node:
            print(current_node.get_value())
            current_node = current_node.get_link_node()

    def delete_node(self, node_value):
        current_node = self.get_head_node()
        if current_node.get_value() == node_value:
            self.head_node = current_node.get_link_node()
        else:
            while current_node:
                next_node = current_node.get_link_node()
                if next_node.get_value() == node_value:
                    current_node.set_link_node(next_node.get_link_node())
                    current_node = None
                else:
                    current_node = current_node.get_link_node()
        print("list after deletion")
        self.print_nodes()


ll = SinglyLinkedList()
n1 = 34
n2 = 45
n3 = 69
node_arr = [n1, n2, n3]
for i in range(len(node_arr)):
    ll.insert_node(node_arr[i])

ll.print_nodes()
ll.delete_node(45)
ll.delete_node(69)
ll.delete_node(34)
