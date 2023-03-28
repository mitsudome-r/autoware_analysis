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

def getContributors(script, first_cursor, contributor_type, respository):
    all_edges=[]

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

## autoware_common
autoware_common_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware_common"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_common_issues += getContributors(script, cursor, contributor_type, repository)
contributors += autoware_common_issues

result="autoware_common_issues.json"
with open(result, 'w') as fp:
    json.dump(autoware_common_issues, fp, indent=2)

autoware_common_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware_common"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_common_prs += getContributors(script, cursor, contributor_type, repository)
contributors += autoware_common_prs

result="autoware_common_prs.json"
with open(result, 'w') as fp:
    json.dump(autoware_common_prs, fp, indent=2)

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

result="autoware_msgs_prs.json"
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

## autoware_documentation
autoware_documentation_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware-documentation"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_documentation_issues += getContributors(script, cursor, contributor_type, repository)
contributors += autoware_documentation_issues

result="autoware_documentation_issues.json"
with open(result, 'w') as fp:
    json.dump(autoware_documentation_issues, fp, indent=2)

autoware_documentation_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware-documentation"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_documentation_prs += getContributors(script, cursor, contributor_type, repository)
contributors += autoware_documentation_prs

result="autoware_documentation_prs.json"
with open(result, 'w') as fp:
    json.dump(autoware_documentation_prs, fp, indent=2)

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

## autoware_ai_perception
autoware_ai_perception_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware_ai_perception"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_perception_issues += getContributors(script, cursor, contributor_type, repository)

result="autoware_ai_perception_issues.json"
with open(result, 'w') as fp:
    json.dump(autoware_ai_perception_issues, fp, indent=2)

autoware_ai_perception_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware_ai_perception"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_perception_prs += getContributors(script, cursor, contributor_type, repository)

result="autoware_ai_perception_prs.json"
with open(result, 'w') as fp:
    json.dump(autoware_ai_perception_prs, fp, indent=2)

## autoware_ai_planning
autoware_ai_planning_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware_ai_planning"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_planning_issues += getContributors(script, cursor, contributor_type, repository)

result="autoware_ai_planning_issues.json"
with open(result, 'w') as fp:
    json.dump(autoware_ai_planning_issues, fp, indent=2)

autoware_ai_planning_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware_ai_planning"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_planning_prs += getContributors(script, cursor, contributor_type, repository)

result="autoware_ai_planning_prs.json"
with open(result, 'w') as fp:
    json.dump(autoware_ai_planning_prs, fp, indent=2)

## autoware_ai_messages
autoware_ai_messages_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware_ai_messages"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_messages_issues += getContributors(script, cursor, contributor_type, repository)

result="autoware_ai_messages_issues.json"
with open(result, 'w') as fp:
    json.dump(autoware_ai_messages_issues, fp, indent=2)

autoware_ai_messages_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware_ai_messages"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_messages_prs += getContributors(script, cursor, contributor_type, repository)

result="autoware_ai_messages_prs.json"
with open(result, 'w') as fp:
    json.dump(autoware_ai_messages_prs, fp, indent=2)

## autoware_ai_simulation
autoware_ai_simulation_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware_ai_simulation"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_simulation_issues += getContributors(script, cursor, contributor_type, repository)

result="autoware_ai_simulation_issues.json"
with open(result, 'w') as fp:
    json.dump(autoware_ai_simulation_issues, fp, indent=2)

autoware_ai_simulation_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware_ai_simulation"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_simulation_prs += getContributors(script, cursor, contributor_type, repository)

result="autoware_ai_simulation_prs.json"
with open(result, 'w') as fp:
    json.dump(autoware_ai_simulation_prs, fp, indent=2)

## autoware_ai_visualization
autoware_ai_visualization_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware_ai_visualization"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_visualization_issues += getContributors(script, cursor, contributor_type, repository)

result="autoware_ai_visualization_issues.json"
with open(result, 'w') as fp:
    json.dump(autoware_ai_visualization_issues, fp, indent=2)

autoware_ai_visualization_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware_ai_visualization"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_visualization_prs += getContributors(script, cursor, contributor_type, repository)

result="autoware_ai_visualization_prs.json"
with open(result, 'w') as fp:
    json.dump(autoware_ai_visualization_prs, fp, indent=2)

## autoware_ai_drivers
autoware_ai_drivers_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware_ai_drivers"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_drivers_issues += getContributors(script, cursor, contributor_type, repository)

result="autoware_ai_drivers_issues.json"
with open(result, 'w') as fp:
    json.dump(autoware_ai_drivers_issues, fp, indent=2)

autoware_ai_drivers_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware_ai_drivers"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_drivers_prs += getContributors(script, cursor, contributor_type, repository)

result="autoware_ai_drivers_prs.json"
with open(result, 'w') as fp:
    json.dump(autoware_ai_drivers_prs, fp, indent=2)

## autoware_ai_utilities
autoware_ai_utilities_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware_ai_utilities"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_utilities_issues += getContributors(script, cursor, contributor_type, repository)

result="autoware_ai_utilities_issues.json"
with open(result, 'w') as fp:
    json.dump(autoware_ai_utilities_issues, fp, indent=2)

autoware_ai_utilities_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware_ai_utilities"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_utilities_prs += getContributors(script, cursor, contributor_type, repository)

result="autoware_ai_utilities_prs.json"
with open(result, 'w') as fp:
    json.dump(autoware_ai_utilities_prs, fp, indent=2)

## autoware_ai_common
autoware_ai_common_issues = []
cursor_script="get_first_issue.sh"
script="query_issues.sh"
contributor_type="issues"
repository="autoware_ai_common"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_common_issues += getContributors(script, cursor, contributor_type, repository)

result="autoware_ai_common_issues.json"
with open(result, 'w') as fp:
    json.dump(autoware_ai_common_issues, fp, indent=2)

autoware_ai_common_prs = []
cursor_script="get_first_pr.sh"
script="query_prs.sh"
contributor_type="pullRequests"
repository="autoware_ai_common"
cursor=getFirstCursor(cursor_script, contributor_type, repository)
autoware_ai_common_prs += getContributors(script, cursor, contributor_type, repository)

result="autoware_ai_common_prs.json"
with open(result, 'w') as fp:
    json.dump(autoware_ai_common_prs, fp, indent=2)

