import json
from collections import OrderedDict
import pprint
import subprocess

import datetime

def countStars(file):
    f = open(file, "r")
    loaded_json = json.load(f)
    edges = loaded_json

    contributors=[]
    stars_per_day={}

    print(len(edges))
    for x in edges:
        d = datetime.datetime.strptime(x["starredAt"], '%Y-%m-%dT%H:%M:%SZ')
        day = datetime.date(d.year, d.month, d.day)
        if day not in stars_per_day:
            stars_per_day[day]=1
        else:
            stars_per_day[day]+=1

    return stars_per_day
def writeNamesToFile(stars, file_name):
    with open("stars/" + file_name, 'w') as fp:
        count = 0
        for key in stars.keys():
            count += stars[key]
            line = key.strftime('%Y/%m/%d') + "," + str(stars[key])+"," + str(count)
            fp.write("%s\n" % line)
    print('Done')


stars_per_day = countStars("stars/stargazers.json")
writeNamesToFile(stars_per_day, "counted_stars.csv")
