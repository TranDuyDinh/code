class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListAlgorithms:
    def __init__(self) -> None:
        self.head = None

    def reverse(self) -> None:
        """
        Singly Liked List - Reverse
        """
        if self.head is None:
            return
        count = target = 0
        current_node = self.head
        while current_node.next != None:
            # swap 2 nodes
            buffer_value = current_node.data
            current_node.data = current_node.next.data
            current_node.next.data = buffer_value
            current_node = current_node.next
            count = count + 1
        current_node = self.head
        target = count - 1
        count = 0
        while target != 1:
            if count == target:
                current_node = self.head
                count = 0
                target = target - 1
            # swap 2 nodes
            buffer_value = current_node.data
            current_node.data = current_node.next.data
            current_node.next.data = buffer_value
            current_node = current_node.next
            count = count + 1


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

    def prepend(self, data: str) -> None:
        """
        Singly Liked List - Prepend
        """
        new_node = Node(data)
        # check 1st node
        if self.head is None:
            self.head = new_node
            return
        # assign newly node to the header
        new_node.next = self.head
        self.head = new_node

    def length(self) -> int:
        """
        Singly Liked List - Length
        """
        current_node = self.head
        if self.head is None:
            return 0
        count = 1
        while current_node.next != None:
            count += 1
            current_node = current_node.next
        return count
    
    # def get_node_by_order(self, order: int) -> Node | None:
    def get_node_by_order(self, order: int) -> Node:
        """
        Singly Liked List - Get Node By Order
        """
        # if self.head is None:
        #     return None
        current_node = self.head
        count = 1
        while current_node.next != None:
            if count == order:
                return current_node
            count += 1
            current_node = current_node.next
        # return None
    
    def swap_node(self, order1: str, order2: str) -> None:
        """
        Singly Liked List - Swap Node
        """
        count = 1
        current_node = self.head
        while current_node.next != None:
            if count == order1:
                buf_node = current_node
            if count == order2:
                buf_data = buf_node.data
                buf_node.data = current_node.data
                current_node.data = buf_data
                return
            count = count + 1
            current_node = current_node.next

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
    
    _list.append('A')
    _list.append('B')
    _list.append('C')
    _list.append('D')
    
    _list.print_list()
    _list.reverse()
    _list.print_list()