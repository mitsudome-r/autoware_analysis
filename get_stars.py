import json
from collections import OrderedDict
import pprint
import subprocess


def getFirstCursor(script, repository):
    res = subprocess.run(["bash", script, repository])
    f = open("tmp.txt", "r")
    loaded_json = json.load(f)
    if len(loaded_json["data"]["repository"]["stargazers"]["edges"]) == 0:
        return None, None
    cursor = loaded_json["data"]["repository"]["stargazers"]["edges"][0]["cursor"]
    edges = loaded_json["data"]["repository"]["stargazers"]["edges"]
    return cursor, edges

def getStargazers(script, cursor_script, respository):
    print(repository)

    all_edges=[]
    first_cursor, all_edges=getFirstCursor(cursor_script, repository)
    if first_cursor == None:
        return all_edges
    cursor=first_cursor
    res = subprocess.run(["bash", script, cursor, repository])
    f = open("tmp.txt", "r")

    loaded_json = json.load(f)
    edges = loaded_json["data"]["repository"]["stargazers"]["edges"]

    while len(edges) > 0:
        all_edges += edges
        print(len(edges))

        cursor=edges[-1]["cursor"]
        res = subprocess.run(["bash", script, cursor, repository])
        f = open("tmp.txt", "r")
        loaded_json = json.load(f)
        edges = loaded_json["data"]["repository"]["stargazers"]["edges"]

    return all_edges

def getUsernames(stargazers):
    usernames=set()
    for edge in stargazers:
        usernames.add(edge["node"]["login"])
    return usernames

def dumpJson(json_dict, file_name):
    with open("stars/" + file_name, 'w') as fp:
        json.dump(json_dict, fp, indent=2)

def dumpUsernames(usernames, file_name):
    with open("stars/" + file_name, 'w') as fp:
        for username in usernames:
            fp.write("%s\n" % username)

repositories = [
    "autoware",
    "autoware_core",
    "autoware_common",
    "autoware_universe",
    "autoware.privately-owned-vehicles",
    "autoware_msgs",
    "autoware_launch",
    "autoware-documentation",
    "autoware_ai_perception",
    "autoware_core_universe_prototype"
]

## autoware
all_usernames=set()
for repository in repositories:
    stargazers = []
    cursor_script="get_first_star.sh"
    script="query_stars.sh"
    stargazers += getStargazers(script, cursor_script, repository)
    usernames = getUsernames(stargazers)
    all_usernames.update(usernames)
    dumpJson(stargazers, repository+"_stargazers.json")
    dumpUsernames(usernames, repository+"_usernames.txt")

dumpUsernames(all_usernames, "usernames.txt")
