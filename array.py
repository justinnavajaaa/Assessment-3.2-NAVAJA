
print("================================")
print("       ARRAY PROGRAM")
print("================================")

last_name = input("Enter your last name: ").upper()

array = []

print("\nADDING LETTERS TO ARRAY")

for letter in last_name:
    array.append(letter)
    print("Added:", letter)
    print("Array:", array)

print("\nREMOVING LETTERS FROM ARRAY")

while len(array) > 0:
    removed = array.pop()
    print("Removed:", removed)
    print("Array:", array)

print("\nThe array is now EMPTY!")
print("Program completed.")
