L = []

while len(L) < 3:
    new_name = input("Add new name: ").strip().capitalize()
    L.append(new_name)

print("List full")
print(L)