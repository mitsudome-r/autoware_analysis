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

    contributors=[]

    while len(edges) > 0:
        print(len(edges))
        for x in edges:
            if x["node"]["author"] is not None:
                contributors.append(x["node"]["author"]["login"])
            for y in x["node"]["comments"]["edges"]:
                if y["node"]["author"] is not None:
                    contributors.append(y["node"]["author"]["login"])
        cursor=edges[-1]["cursor"]

        res = subprocess.run(["bash", script, cursor, repository])
        f = open("tmp.txt", "r")

        loaded_json = json.load(f)

        edges = loaded_json["data"]["repository"][contributor_type]["edges"]
    print(len(edges))

    contributors = sorted(set(contributors))
    print(contributors)
    print(len(contributors))
    return contributors

contributors = []

## autoware

autoware_discussions = []
cursor_script="get_first_discussion.sh"
script="query_discussions.sh"
contributor_type="discussions"
repository="autoware"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_discussions += getContributors(script, cursor, contributor_type, repository)
autoware_discussions = sorted(set(autoware_discussions))
contributors += autoware_discussions

result="autoware_discussions.txt"
with open(result, 'w') as fp:
    for name in autoware_discussions:
        fp.write("%s\n" % name)
    print('Done')

autoware_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_issues += getContributors(script, cursor, contributor_type, repository)
autoware_issues = sorted(set(autoware_issues))
contributors += autoware_issues

result="autoware_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_prs += getContributors(script, cursor, contributor_type, repository)
autoware_prs = sorted(set(autoware_prs))
contributors += autoware_prs

result="autoware_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_prs:
        fp.write("%s\n" % name)
    print('Done')

## autoware_universe

universe_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware.universe"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
universe_issues += getContributors(script, cursor, contributor_type, repository)
universe_issues = sorted(set(universe_issues))
contributors += universe_issues

result="universe_issues.txt"
with open(result, 'w') as fp:
    for name in universe_issues:
        fp.write("%s\n" % name)
    print('Done')

universe_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware.universe"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
universe_prs += getContributors(script, cursor, contributor_type, repository)
universe_prs = sorted(set(universe_prs))
contributors += universe_prs

result="universe_prs.txt"
with open(result, 'w') as fp:
    for name in universe_prs:
        fp.write("%s\n" % name)
    print('Done')

## autoware_core
autoware_core_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware.core"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_core_issues += getContributors(script, cursor, contributor_type, repository)
autoware_core_issues = sorted(set(autoware_core_issues))
contributors += autoware_core_issues

result="autoware_core_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_core_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_core_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware.core"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_core_prs += getContributors(script, cursor, contributor_type, repository)
autoware_core_prs = sorted(set(autoware_core_prs))
contributors += autoware_core_prs

result="autoware_core_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_core_prs:
        fp.write("%s\n" % name)
    print('Done')

## autoware_msgs
autoware_msgs_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware_msgs"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_msgs_issues += getContributors(script, cursor, contributor_type, repository)
autoware_msgs_issues = sorted(set(autoware_msgs_issues))
contributors += autoware_msgs_issues

result="autoware_msgs_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_msgs_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_msgs_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware_msgs"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_msgs_prs += getContributors(script, cursor, contributor_type, repository)
autoware_msgs_prs = sorted(set(autoware_msgs_prs))
contributors += autoware_msgs_prs

## autoware_launch
autoware_launch_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware_launch"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_launch_issues += getContributors(script, cursor, contributor_type, repository)
autoware_launch_issues = sorted(set(autoware_launch_issues))
contributors += autoware_launch_issues

result="autoware_launch_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_launch_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_launch_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware_launch"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_launch_prs += getContributors(script, cursor, contributor_type, repository)
autoware_launch_prs = sorted(set(autoware_launch_prs))
contributors += autoware_launch_prs

result="autoware_launch_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_launch_prs:
        fp.write("%s\n" % name)
    print('Done')

## autoware_ai

autoware_ai_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware_ai"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_issues += getContributors(script, cursor, contributor_type, repository)
autoware_ai_issues = sorted(set(autoware_ai_issues))

result="autoware_ai_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_issues:
        fp.write("%s\n" % name)
    print('Done')

### ALL

print(type(contributors))
print(contributors)
print(len(contributors))
contributors = sorted(set(contributors))

result="all_contributors.txt"
with open(result, 'w') as fp:
    for name in contributors:
        fp.write("%s\n" % name)
    print('Done')
