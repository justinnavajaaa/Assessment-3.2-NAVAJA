
print("================================")
print("          STACK PROGRAM")
print("================================")

last_name = input("Enter your last name: ").upper()

stack = []

print("\nPUSHING LETTERS INTO STACK")

for letter in last_name:
    stack.append(letter)
    print("Push:", letter)
    print("Stack:", stack)

print("\nPOPPING LETTERS FROM STACK")

while len(stack) > 0:
    removed = stack.pop()
    print("Pop:", removed)
    print("Stack:", stack)

print("\nThe stack is now EMPTY!")
print("Program completed.")
