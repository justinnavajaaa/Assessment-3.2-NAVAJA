
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self):
        if self.head is None:
            return None

        removed = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return removed

    def display(self):
        current = self.head

        if current is None:
            print("EMPTY")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


print("================================")
print("   SINGLY LINKED LIST PROGRAM")
print("================================")

last_name = input("Enter your last name: ").upper()

linked_list = SinglyLinkedList()

print("\nADDING NODES")

for letter in last_name:
    linked_list.add(letter)
    print("Added:", letter)
    print("Linked List:", end=" ")
    linked_list.display()

print("\nREMOVING NODES")

while linked_list.head is not None:
    removed = linked_list.remove()
    print("Removed:", removed)
    print("Linked List:", end=" ")
    linked_list.display()

print("\nThe linked list is now EMPTY!")
print("Program completed.")
