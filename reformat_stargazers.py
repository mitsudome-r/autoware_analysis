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



repositories = [
    "autoware",
    "autoware_core",
    "autoware_common",
    "autoware_universe",
    "autoware.privately-owned-vehicles",
    # "autoware_msgs",
    # "autoware_launch",
    # "autoware-documentation",
    # "autoware_tools",
    # "autoware_cmake",
    # "autoware_utils",
    # "autoware_lanelet2_extension",
    # "autoware_rviz_plugins",
    # "autoware_adapi_msgs",
    # "autoware_internal_msgs",
    # "openadkit"
]

autoware_ai_repositories = [
    "autoware_ai",
    "autoware_ai_perception",
    "autoware_ai_planning",
    "autoware_ai_messages",
    "autoware_ai_simulation",
    "autoware_ai_visualization",
    "autoware_ai_drivers",
    "autoware_ai_utilities",
    "autoware_ai_common"
]
def getUsernames(file_name):
    usernames = set()
    with open(file_name, 'r') as fp:
        lines = fp.readlines()
    for line in lines:
        username = line.strip()
        usernames.add(username)
    return usernames

def dumpUsernames(usernames, file_name):
    with open("stars/" + file_name, 'w') as fp:
        for username in usernames:
            fp.write("%s\n" % username)

all_usernames = set()
for repository in repositories:
    usernames = getUsernames("stars/"+repository+"_usernames.txt")
    all_usernames.update(usernames)

# for repository in autoware_ai_repositories:
#     usernames = getUsernames("stars/"+repository+"_usernames.txt")
#     all_usernames.update(usernames)


stars_per_day = countStars("stars/autoware_stargazers.json")
writeNamesToFile(stars_per_day, "counted_stars.csv")

dumpUsernames(all_usernames, "all_usernames.txt")