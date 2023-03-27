import json
from collections import OrderedDict
import pprint
import subprocess


def getFirstCursor(script, contributor_type, repository):
    res = subprocess.run(["bash", script, repository])
    f = open("tmp.txt", "r")
    loaded_json = json.load(f)
    return loaded_json["data"]["repository"][contributor_type]["edges"][0]["cursor"]

def getContributors(script, first_cursor, contributor_type, respository):
    print(contributor_type, repository)
    cursor=first_cursor
    res = subprocess.run(["bash", script, cursor, repository])
    f = open("tmp.txt", "r")

    loaded_json = json.load(f)

    edges = loaded_json["data"]["repository"][contributor_type]["edges"]
    all_edges=[]

    while len(edges) > 0:
        all_edges += edges
        print(len(edges))

        cursor=edges[-1]["cursor"]
        res = subprocess.run(["bash", script, cursor, repository])
        f = open("tmp.txt", "r")
        loaded_json = json.load(f)
        edges = loaded_json["data"]["repository"][contributor_type]["edges"]

    return all_edges

contributors = []

## autoware

autoware_discussions = []
cursor_script="get_first_discussion.sh"
script="query_discussions.sh"
contributor_type="discussions"
repository="autoware"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_discussions += getContributors(script, cursor, contributor_type, repository)
contributors += autoware_discussions

result="autoware_discussions.json"
with open(result, 'w') as fp:
    json.dump(autoware_discussions, fp, indent=2)

autoware_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_issues += getContributors(script, cursor, contributor_type, repository)
contributors += autoware_issues

result="autoware_issues.json"
with open(result, 'w') as fp:
    json.dump(autoware_issues, fp, indent=2)

autoware_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_prs += getContributors(script, cursor, contributor_type, repository)
contributors += autoware_prs

result="autoware_prs.json"
with open(result, 'w') as fp:
    json.dump(autoware_prs, fp, indent=2)

## autoware_universe

universe_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware.universe"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
universe_issues += getContributors(script, cursor, contributor_type, repository)
contributors += universe_issues

result="universe_issues.json"
with open(result, 'w') as fp:
    json.dump(universe_issues, fp, indent=2)

universe_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware.universe"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
universe_prs += getContributors(script, cursor, contributor_type, repository)
contributors += universe_prs

result="universe_prs.json"
with open(result, 'w') as fp:
    json.dump(universe_prs, fp, indent=2)

## autoware_core
autoware_core_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware.core"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_core_issues += getContributors(script, cursor, contributor_type, repository)
contributors += autoware_core_issues

result="autoware_core_issues.json"
with open(result, 'w') as fp:
    json.dump(autoware_core_issues, fp, indent=2)

autoware_core_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware.core"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_core_prs += getContributors(script, cursor, contributor_type, repository)
contributors += autoware_core_prs

result="autoware_core_prs.json"
with open(result, 'w') as fp:
    json.dump(autoware_core_prs, fp, indent=2)

## autoware_msgs
autoware_msgs_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware_msgs"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_msgs_issues += getContributors(script, cursor, contributor_type, repository)
contributors += autoware_msgs_issues

result="autoware_msgs_issues.json"
with open(result, 'w') as fp:
    json.dump(autoware_msgs_issues, fp, indent=2)

autoware_msgs_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware_msgs"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_msgs_prs += getContributors(script, cursor, contributor_type, repository)
contributors += autoware_msgs_prs

result="get_first_pr.json"
with open(result, 'w') as fp:
    json.dump(autoware_msgs_prs, fp, indent=2)

## autoware_launch
autoware_launch_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware_launch"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_launch_issues += getContributors(script, cursor, contributor_type, repository)
contributors += autoware_launch_issues

result="autoware_launch_issues.json"
with open(result, 'w') as fp:
    json.dump(autoware_launch_issues, fp, indent=2)

autoware_launch_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware_launch"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_launch_prs += getContributors(script, cursor, contributor_type, repository)
contributors += autoware_launch_prs

result="autoware_launch_prs.json"
with open(result, 'w') as fp:
    json.dump(autoware_launch_prs, fp, indent=2)

## autoware_ai

autoware_ai_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware_ai"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_issues += getContributors(script, cursor, contributor_type, repository)

result="autoware_ai_issues.json"
with open(result, 'w') as fp:
    json.dump(autoware_ai_issues, fp, indent=2)
