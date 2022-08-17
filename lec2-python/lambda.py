people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]

# people.sort()

############
def f(person):
    return person["name"]


people.sort(key=f)
print(people)
###########
# lambda function
people.sort(key=lambda person: person["name"])
print(people)
