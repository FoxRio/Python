import itertools
itertools.per
observations = [
    (['Harry', 'Ron', 'Neville'], [6, 10, 3]),
    (['Ginny', 'Clementine', 'Dattel', 'Luna', 'Himbeere'], [2, 1, 9, 8, 4]),
    (['Ginny', 'Luna', 'Ron', 'Himbeere', 'Johannisbeere'], [5, 8, 10, 4, 2]),
    (['Dattel', 'Luna', 'Himbeere', 'Neville', 'Johannisbeere'], [6, 4, 2, 5, 9])
]
people = {
    "Harry": [],
    "Ron": [],
    "Neville": [],
    "Ginny": [],
    "Luna": [],
    'Himbeere': [],
    "Johannisbeere": [],
    "Dattel": [],
    "Clementine": []
}

c = 0
for i in observations:
    print(c, i)
    for human in i[0]:
        for value in i[1]:
            if c == 0:
                alreadyThere = people[human]
                people[human] = []
                if value in alreadyThere:
                    people[human].append(value)
            else:
                people[human].append(value)
    c += 1

print(people.items())