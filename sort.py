import json
from collections import OrderedDict
import pprint
import subprocess

names = []

with open("full.txt") as file:
    names = file.read().splitlines()

names = sorted(set(names))

print(len(names))