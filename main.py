import sys

if len(sys.argv) != 2:
    print("Usage: python3 {} <items csv file name>\nIn the csv file, '-' are separators.".format(sys.argv[0]))
    exit(1)

items_file = sys.argv[1]
list_file = input("Output file name: ")

class Item:
    def __init__(self, name):
        self.name = name
        self.quantity = 0

items = []

with open(items_file) as file:
    items = [Item(name) for name in file.read().replace('\n', '').split(',')]

for item in items:
    # Skip separators
    if item.name == '-':
        continue

    q = input("How many of {} would you like? ".format(item.name))
    if q:
        item.quantity = int(q)

with open(list_file, "w+") as file:
    for item in items:
        # Write newlines for separators
        if item.name == '-':
            file.write('\n')
        elif item.quantity > 0:
            file.write("[ ] {} {}\n".format(item.quantity, item.name))
