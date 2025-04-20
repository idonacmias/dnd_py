from collections import namedtuple
import csv

Skill = namedtuple('Skill', ['name', 'atribute'])
all_skills = []
with open("data/skills.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        all_skills.append(Skill._make(row))
