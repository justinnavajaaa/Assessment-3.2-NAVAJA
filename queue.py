
from collections import deque

print("================================")
print("          QUEUE PROGRAM")
print("================================")

last_name = input("Enter your last name: ").upper()

queue = deque()

print("\nADDING LETTERS TO QUEUE")

for letter in last_name:
    queue.append(letter)
    print("Enqueue:", letter)
    print("Queue:", list(queue))

print("\nREMOVING LETTERS FROM QUEUE")

while len(queue) > 0:
    removed = queue.popleft()
    print("Dequeue:", removed)
    print("Queue:", list(queue))

print("\nThe queue is now EMPTY!")
print("Program completed.")
