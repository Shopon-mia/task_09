# NODE --> Data | Next

# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next


# class LinkedList:
#     def __init__(self):
#         self.head = Node()

#     def get_length(self):
#         cnt = 0
#         current_node = self.head
#         while current_node:
#             cnt += 1
#             current_node = current_node.next
#         return cnt

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

#     def insert_at(self, index, data):
#         if index < 0 or index > self.get_length():
#             print('Invalid Index')
#             return

#         if index == 0:
#             self.append_at_begining(data)
#             return

#         cnt = 0
#         current_node = self.head
#         while current_node:
#             if cnt == index - 1:
#                 node = Node(data, current_node.next)
#                 current_node.next = node
#                 break
#             current_node = current_node.next
#             cnt += 1

# if __name__ == '__main__':
#     ll = LinkedList()

#     # item added at begining
#     ll.append_at_begining(10)
#     ll.append_at_begining(20)
#     ll.append_at_begining(30)
#     ll.append_at_begining(40)
#     ll.append_at_begining(50)
#     ll.append_at_begining(60)
#     ll.append_at_begining(70)
#     ll.append_at_begining(80)
#     ll.print_linked_list()


#     # insert at specific index
#     ll.insert_at(3, 25)
#     ll.insert_at(5, 35)
#     ll.print_linked_list()


# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next


# class LinkedList:
#     def __init__(self):
#         self.head = Node()

#     def get_length(self):
#         cnt = 0
#         current_node = self.head
#         while current_node:
#             cnt += 1
#             current_node = current_node.next
#         return cnt

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

#     def insert_at(self, index, data):
#         if index < 0 or index > self.get_length():
#             print('Invalid Index')
#             return

#         if index == 0:
#             self.append_at_begining(data)
#             return

#         cnt = 0
#         current_node = self.head
#         while current_node:
#             if cnt == index - 1:
#                 node = Node(data, current_node.next)
#                 current_node.next = node
#                 break
#             current_node = current_node.next
#             cnt += 1

# if __name__ == '__main__':
#     ll = LinkedList()

#     # item added at begining
#     ll.append_at_begining(10)
#     ll.append_at_begining(20)
#     ll.append_at_begining(30)
#     ll.append_at_begining(40)
#     ll.append_at_begining(50)
#     ll.print_linked_list()


#     # insert at specific index
#     ll.insert_at(3, 25)
#     ll.insert_at(5, 35)
#     ll.print_linked_list()


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node()

    def get_length(self):
        cnt = 0
        current_node = self.head
        while current_node:
            cnt += 1
            current_node = current_node.next
        return cnt

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

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            print('Invalid Index')
            return

        if index == 0:
            self.append_at_begining(data)
            return

        cnt = 0
        current_node = self.head
        while current_node:
            if cnt == index - 1:
                node = Node(data, current_node.next)
                current_node.next = node
                break
            current_node = current_node.next
            cnt += 1

if __name__ == '__main__':
    ll = LinkedList()

    # item added at begining
    ll.append_at_begining(10)
    ll.append_at_begining(20)
    ll.append_at_begining(30)
    ll.append_at_begining(40)
    ll.append_at_begining(50)
    ll.append_at_begining(60)
    ll.print_linked_list()


    # insert at specific index
    ll.insert_at(3, 25)
    ll.insert_at(5, 35)
    ll.print_linked_list()

