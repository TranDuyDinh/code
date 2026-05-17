class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListAlgorithms:
    def __init__(self) -> None:
        self.head = None

    def append(self, data : str) -> None:
        """
        Singly Liked List - Append
        """
        new_node = Node(data)
        # add 1st node
        if self.head is None:
            self.head = new_node
            return
        # assign pointer to header
        last_node = self.head
        # scan list to find the last node
        while last_node.next != None:
            last_node = last_node.next
        # add new node
        last_node.next = new_node


    def print_list(self):
        """
        Singly Liked List - Print
        """
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


if __name__ == "__main__":

    _list = LinkedListAlgorithms()
    
    _list.append('a')
    _list.append('b')
    _list.append('c')
    
    _list.print_list()