min_age = 100
min_person = ""

people = [
    ["Stephanie", 36],
    ["John", 29],
    ["Emily", 24],
    ["Gretchen", 54],
    ["Noah", 12],
    ["Penelope", 32],
    ["Michael", 2],
    ["Jacob", 10],
]

for item in people:
    name = item[0]
    age = item[1] 

    if age < min_age:
        #minimum age is updated
        min_age = age
        #minimum person is updated
        min_person = name

print(f"\nThe youngest person is {min_person} at {min_age} years old.\n")