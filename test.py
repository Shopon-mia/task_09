# begining functio 5 tiems code
def append_at_begining(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

def append_at_begining(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

def append_at_begining(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

def append_at_begining(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

def append_at_begining(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

# end function 5 time code
def append_at_end(self, data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data, None) 

def append_at_end(self, data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data, None)

def append_at_end(self, data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data, None)

def append_at_end(self, data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data, None)

def append_at_end(self, data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data, None)

# insert function 5 time code
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