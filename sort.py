import json
from collections import OrderedDict
import pprint
import subprocess

names = []

with open("autoware_ai_contributors.txt") as file:
    names = file.read().splitlines()

names = sorted(set(names))

print(len(names))