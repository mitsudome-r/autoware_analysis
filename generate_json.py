import json
from collections import OrderedDict
import pprint
import subprocess


def getFirstCursor(script, contributor_type, repository):
    res = subprocess.run(["bash", script, repository])
    f = open("tmp.txt", "r")
    loaded_json = json.load(f)
    if len(loaded_json["data"]["repository"][contributor_type]["edges"]) == 0:
        return None
    return loaded_json["data"]["repository"][contributor_type]["edges"][0]["cursor"]

def getContributors(script, cursor_script, contributor_type, respository):
    all_edges=[]

    first_cursor=getFirstCursor(cursor_script, contributor_type, repository)
    if first_cursor == None:
        return all_edges

    print(contributor_type, repository)
    cursor=first_cursor
    res = subprocess.run(["bash", script, cursor, repository])
    f = open("tmp.txt", "r")

    loaded_json = json.load(f)

    edges = loaded_json["data"]["repository"][contributor_type]["edges"]

    while len(edges) > 0:
        all_edges += edges
        print(len(edges))

        cursor=edges[-1]["cursor"]
        res = subprocess.run(["bash", script, cursor, repository])
        f = open("tmp.txt", "r")
        loaded_json = json.load(f)
        edges = loaded_json["data"]["repository"][contributor_type]["edges"]

    return all_edges

def dumpJson(json_dict, file_name):
    with open("generated_json/" +file_name, 'w') as fp:
        json.dump(json_dict, fp, indent=2)

## autoware
repositories = [
    "autoware",
    "autoware_core",
    "autoware_universe",
    "autoware_common",
    "autoware_msgs",
    "autoware_adapi_msgs",
    "autoware_internal_msgs",
    "autoware_cmake",
    "autoware_utils",
    "autoware_lanelet2_extension",
    "autoware_rviz_plugins",
    "autoware_launch",
    "autoware-documentation",
    "autoware_tools",
    "autoware.privately-owned-vehicles",
    "openadkit",
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

autoware_discussions = []
cursor_script="get_first_discussion.sh"
script="query_discussions.sh"
contributor_type="discussions"
repository="autoware"
autoware_discussions += getContributors(script, cursor_script, contributor_type, repository)
dumpJson(autoware_discussions, "autoware_discussions.json")

for repository in repositories:
    issues = []
    cursor_script="get_first_issue.sh"
    script="query_issues.sh"
    contributor_type="issues"
    issues += getContributors(script, cursor_script, contributor_type, repository)
    dumpJson(issues, repository+"_issues.json")

    pull_requests = []
    cursor_script="get_first_pr.sh"
    script="query_prs.sh"
    contributor_type="pullRequests"
    pull_requests += getContributors(script, cursor_script, contributor_type, repository)
    dumpJson(pull_requests, repository+"_prs.json")
