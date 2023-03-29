import json
from collections import OrderedDict
import pprint
import subprocess

names = []
tier4_engineers = []
filtered = []

with open("tier4_engineers.txt") as file:
    tier4_engineers = file.read().splitlines()

with open("autoware_code_contributors.txt") as file:
    names = file.read().splitlines()
names = sorted(set(names))

for name in names:
    if name in tier4_engineers:
        filtered.append(name)

print(len(filtered))