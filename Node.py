class Node:
    def __init__(self, data, link_node=None):
        self.data = data
        self.link_node = link_node

    def get_value(self):
        return self.data

    def get_link_node(self):
        return self.link_node

    def set_link_node(self, link_node):
        self.link_node = link_node
