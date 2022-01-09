people = [
    {"name":"moorthy", "house":"a"},
    {"name":"netra", "house":"b"},
    {"name":"neha", "house":"c"}
]

def f(person):
    return person["name"]

people.sort(key=f)

print(people)

#lamda represenattion
people.sort(key=lambda person:person["name"])
print(people)
