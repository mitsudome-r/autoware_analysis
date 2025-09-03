import json
from collections import OrderedDict
import pprint
import subprocess


def getFirstCursor(script, organization, team):
    res = subprocess.run(["bash", script, organization, team])
    f = open("tmp.txt", "r")
    loaded_json = json.load(f)
    if len(loaded_json["data"]["organization"]["team"]["members"]["edges"]) == 0:
        return None
    return loaded_json["data"]["organization"]["team"]["members"]["edges"][0]["cursor"]

def getContributors(script, organization, team, first_cursor):
    all_members=[]

    if first_cursor == None:
        return all_edges

    cursor=first_cursor
    res = subprocess.run(["bash", script, organization, team, cursor])
    f = open("tmp.txt", "r")

    loaded_json = json.load(f)

    nodes = loaded_json["data"]["organization"]["team"]["members"]["nodes"]

    while len(nodes) > 0:
        for node in nodes:
            all_members.append(node["login"])

        cursor=loaded_json["data"]["organization"]["team"]["members"]["edges"][-1]["cursor"]
        res = subprocess.run(["bash", script, organization, team, cursor])
        f = open("tmp.txt", "r")
        loaded_json = json.load(f)
        nodes = loaded_json["data"]["organization"]["team"]["members"]["nodes"]

    return all_members

## autoware

tier4_engineers = []
cursor_script="get_first_tier4_engineer.sh"
script="get_tier4_engineers.sh"
cursor=getFirstCursor(cursor_script, "tier4", "full-time-employee")
tier4_engineers += getContributors(script, "tier4", "full-time-employee", cursor)

result="tier4_engineers/tier4_engineers.txt"
with open(result, 'w') as fp:
    for name in tier4_engineers:
        fp.write("%s\n" % name)
    print('Done')

tier4_engineers = []
cursor_script="get_first_tier4_engineer.sh"
script="get_tier4_engineers.sh"
cursor=getFirstCursor(cursor_script, "autowarefoundation", "autoware-developers-tier4")
tier4_engineers += getContributors(script, "autowarefoundation", "autoware-developers-tier4", cursor)

result="tier4_engineers/autoware_developers_tier4.txt"
with open(result, 'w') as fp:
    for name in tier4_engineers:
        fp.write("%s\n" % name)
    print('Done')


tier4_engineers = []
cursor_script="get_first_tier4_engineer.sh"
script="get_tier4_engineers.sh"
cursor=getFirstCursor(cursor_script, "autowarefoundation", "autoware-developers-leodrive")
tier4_engineers += getContributors(script, "autowarefoundation", "autoware-developers-leodrive", cursor)

result="tier4_engineers/autoware_developers_leodrive.txt"
with open(result, 'w') as fp:
    for name in tier4_engineers:
        fp.write("%s\n" % name)
    print('Done')

tier4_engineers = []
cursor_script="get_first_tier4_engineer.sh"
script="get_tier4_engineers.sh"
cursor=getFirstCursor(cursor_script, "autowarefoundation", "autoware-developers-autocore")
tier4_engineers += getContributors(script, "autowarefoundation", "autoware-developers-autocore", cursor)

result="tier4_engineers/autoware_developers_autocore.txt"
with open(result, 'w') as fp:
    for name in tier4_engineers:
        fp.write("%s\n" % name)
    print('Done')