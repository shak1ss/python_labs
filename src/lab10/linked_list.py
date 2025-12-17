class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self.size += 1

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert(self, idx, value):
        if idx < 0 or idx > self.size:
            raise IndexError("Index out of range")
        if idx == 0:
            self.prepend(value)
        elif idx == self.size:
            self.append(value)
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def remove(self, value):
        current = self.head
        if current and current.value == value:
            self.head = current.next
            if not self.head:
                self.tail = None
            self.size -= 1
            return
        prev = None
        while current:
            if current.value == value:
                prev.next = current.next
                if not current.next:
                    self.tail = prev
                self.size -= 1
                return
            prev = current
            current = current.next
        raise ValueError(f"{value} not found in list")

    def remove_at(self, idx):
        if idx < 0 or idx >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        if idx == 0:
            self.head = current.next
            if not self.head:
                self.tail = None
        else:
            prev = None
            for _ in range(idx):
                prev = current
                current = current.next
            prev.next = current.next
            if not current.next:
                self.tail = prev
        self.size -= 1

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self):
        return self.size

    def __repr__(self):
        return f"SinglyLinkedList([{', '.join(map(str, self))}])"
