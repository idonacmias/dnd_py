from collections import namedtuple
import csv

Skill = namedtuple('Skill', ['name', 'atribute', 'pro_level'])
all_skills = []
with open("data/skills.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        row.append(0)
        all_skills.append(Skill._make(row))
