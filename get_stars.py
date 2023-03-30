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

def dumpJson(json_dict, file_name):
    with open("stars/" + file_name, 'w') as fp:
        json.dump(json_dict, fp, indent=2)

## autoware

stargazers = []
cursor_script="get_first_star.sh"
script="query_stars.sh"
repository="autoware"
stargazers += getStargazers(script, cursor_script, repository)
dumpJson(stargazers, "stargazers.json")

