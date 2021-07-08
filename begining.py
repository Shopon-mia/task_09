# NODE --> Data | Next
# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next


# class LinkedList:
#     def __init__(self):
#         self.head = Node()

#     def print_linked_list(self):
#         if self.head is None:
#             print('Linked list is empty')
#             return
#         current_node = self.head
#         info_str = ''
#         while current_node:
#             info_str = info_str + str(current_node.data) + ' --> '
#             current_node = current_node.next
#         print(info_str)

#     def append_at_begining(self, data):
#         node = Node(data, self.head.next)
#         self.head.next = node


# if __name__ == '__main__':
#     ll = LinkedList()

#     # item added at begining
#     ll.append_at_begining(20)
#     ll.append_at_begining(10)
#     ll.print_linked_list()



# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next


# class LinkedList:
#     def __init__(self):
#         self.head = Node()

#     def print_linked_list(self):
#         if self.head is None:
#             print('Linked list is empty')
#             return
#         current_node = self.head
#         info_str = ''
#         while current_node:
#             info_str = info_str + str(current_node.data) + ' --> '
#             current_node = current_node.next
#         print(info_str)

#     def append_at_begining(self, data):
#         node = Node(data, self.head.next)
#         self.head.next = node


# if __name__ == '__main__':
#     ll = LinkedList()

#     # item added at begining
#     ll.append_at_begining(20)
#     ll.append_at_begining(10)
#     ll.append_at_begining(30)
#     ll.print_linked_list()


# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next


# class LinkedList:
#     def __init__(self):
#         self.head = Node()

#     def print_linked_list(self):
#         if self.head is None:
#             print('Linked list is empty')
#             return
#         current_node = self.head
#         info_str = ''
#         while current_node:
#             info_str = info_str + str(current_node.data) + ' --> '
#             current_node = current_node.next
#         print(info_str)

#     def append_at_begining(self, data):
#         node = Node(data, self.head.next)
#         self.head.next = node


# if __name__ == '__main__':
#     ll = LinkedList()

#     # item added at begining
#     ll.append_at_begining(20)
#     ll.append_at_begining(10)
#     ll.append_at_begining(30)
#     ll.append_at_begining(40)
#     ll.print_linked_list()



# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next


# class LinkedList:
#     def __init__(self):
#         self.head = Node()

#     def print_linked_list(self):
#         if self.head is None:
#             print('Linked list is empty')
#             return
#         current_node = self.head
#         info_str = ''
#         while current_node:
#             info_str = info_str + str(current_node.data) + ' --> '
#             current_node = current_node.next
#         print(info_str)

#     def append_at_begining(self, data):
#         node = Node(data, self.head.next)
#         self.head.next = node


# if __name__ == '__main__':
#     ll = LinkedList()

#     # item added at begining
#     ll.append_at_begining(20)
#     ll.append_at_begining(10)
#     ll.append_at_begining(30)
#     ll.append_at_begining(40)
#     ll.append_at_begining(50)
#     ll.print_linked_list()


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node()

    def print_linked_list(self):
        if self.head is None:
            print('Linked list is empty')
            return
        current_node = self.head
        info_str = ''
        while current_node:
            info_str = info_str + str(current_node.data) + ' --> '
            current_node = current_node.next
        print(info_str)

    def append_at_begining(self, data):
        node = Node(data, self.head.next)
        self.head.next = node


if __name__ == '__main__':
    ll = LinkedList()

    # item added at begining
    ll.append_at_begining(20)
    ll.append_at_begining(10)
    ll.append_at_begining(30)
    ll.append_at_begining(40)
    ll.append_at_begining(50)
    ll.append_at_begining(60)
    ll.print_linked_list()