
# ASSESSMENT 3.2
# DOUBLY LINKED LIST
# Last Name: NAVAJA

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove(self):
        if self.tail is None:
            return None

        removed = self.tail.data
        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        return removed

    def display(self):
        current = self.head

        if current is None:
            print("EMPTY")
            return

        while current:
            print(current.data, end="")

            if current.next is not None:
                print(" <-> ", end="")

            current = current.next

        print()


print("================================")
print("   DOUBLY LINKED LIST PROGRAM")
print("================================")

last_name = input("Enter your last name: ").upper()

dll = DoublyLinkedList()

print("\nADDING NODES")

for letter in last_name:
    dll.add(letter)
    print("Added:", letter)
    print("Doubly Linked List:", end=" ")
    dll.display()

print("\nREMOVING NODES")

while dll.tail is not None:
    removed = dll.remove()
    print("Removed:", removed)
    print("Doubly Linked List:", end=" ")
    dll.display()

print("\nThe doubly linked list is now EMPTY!")
print("Program completed.")
