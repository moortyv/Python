#Empty set

s = set()

s.add(1)
s.add(2)
s.add(500)

print(s)

s.add(1)
print(s) #no duplicates

s.add("d")
print(s)

s.remove("d")
print(s)

print(f"SEt has {len(s)} elements ")
