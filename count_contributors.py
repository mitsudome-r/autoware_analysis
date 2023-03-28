import json
from collections import OrderedDict
import pprint
import subprocess

import datetime

def getContributors(file, contributor_type, use_filter = False, count_ai = True):
    f = open(file, "r")
    loaded_json = json.load(f)
    edges = loaded_json

    contributors=[]

    print(len(edges))
    for x in edges:
        d = datetime.datetime.strptime(x["node"]["createdAt"], '%Y-%m-%dT%H:%M:%SZ')
        date_filter = datetime.datetime(2022, 1, 1)
        # date_filter = datetime.datetime(2022, 12, 1)
        if use_filter:
            if d > date_filter and count_ai:
                continue
            if d < date_filter and count_ai == False:
                continue

        print(d) 
        if x["node"]["author"] is not None:
            contributors.append(x["node"]["author"]["login"])
        for y in x["node"]["comments"]["edges"]:
            if y["node"]["author"] is not None:
                contributors.append(y["node"]["author"]["login"])

    contributors = sorted(set(contributors))
    print(contributors)
    print(len(contributors))
    return contributors

contributors = []

## autoware

autoware_discussions = []
contributor_type="discussions"
json_file="autoware_discussions.json"
autoware_discussions += getContributors(json_file, contributor_type)
contributors += autoware_discussions

result="autoware_discussions.txt"
with open(result, 'w') as fp:
    for name in autoware_discussions:
        fp.write("%s\n" % name)
    print('Done')

autoware_issues = []
contributor_type="issues"
json_file="autoware_issues.json"
autoware_issues += getContributors(json_file, contributor_type)
contributors += autoware_issues

result="autoware_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_prs = []
contributor_type="pullRequests"
json_file="autoware_prs.json"
autoware_prs += getContributors(json_file, contributor_type, True, False)
contributors += autoware_prs

result="autoware_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_prs:
        fp.write("%s\n" % name)
    print('Done')

autoware_prs = []
contributor_type="pullRequests"
json_file="autoware_prs.json"
autoware_prs += getContributors(json_file, contributor_type, False, True)
# contributors += autoware_prs

result="autoware_ai_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_prs:
        fp.write("%s\n" % name)
    print('Done')

## autoware_universe

universe_issues = []
contributor_type="issues"
json_file="universe_issues.json"
universe_issues += getContributors(json_file, contributor_type)
contributors += universe_issues

result="universe_issues.txt"
with open(result, 'w') as fp:
    for name in universe_issues:
        fp.write("%s\n" % name)
    print('Done')

universe_prs = []
contributor_type="pullRequests"
json_file="universe_prs.json"
universe_prs += getContributors(json_file, contributor_type)
contributors += universe_prs

result="universe_prs.txt"
with open(result, 'w') as fp:
    for name in universe_prs:
        fp.write("%s\n" % name)
    print('Done')

## autoware_core
autoware_core_issues = []
contributor_type="issues"
json_file="autoware_core_issues.json"
autoware_core_issues += getContributors(json_file, contributor_type)
contributors += autoware_core_issues

result="autoware_core_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_core_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_core_prs = []
contributor_type="pullRequests"
json_file="autoware_core_prs.json"
autoware_core_prs += getContributors(json_file, contributor_type)
contributors += autoware_core_prs

result="autoware_core_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_core_prs:
        fp.write("%s\n" % name)
    print('Done')

## autoware_common
autoware_common_issues = []
contributor_type="issues"
json_file="autoware_common_issues.json"
autoware_common_issues += getContributors(json_file, contributor_type)
contributors += autoware_common_issues

result="autoware_common_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_common_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_common_prs = []
contributor_type="pullRequests"
json_file="autoware_common_prs.json"
autoware_common_prs += getContributors(json_file, contributor_type)
contributors += autoware_common_prs

result="autoware_common_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_common_prs:
        fp.write("%s\n" % name)
    print('Done')

## autoware_msgs
autoware_msgs_issues = []
contributor_type="issues"
json_file="autoware_msgs_issues.json"
autoware_msgs_issues += getContributors(json_file, contributor_type)
contributors += autoware_msgs_issues

result="autoware_msgs_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_msgs_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_msgs_prs = []
contributor_type="pullRequests"
json_file="autoware_msgs_prs.json"
autoware_msgs_prs += getContributors(json_file, contributor_type)
contributors += autoware_msgs_prs

result="autoware_msgs_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_msgs_prs:
        fp.write("%s\n" % name)
    print('Done')

## autoware_launch
autoware_launch_issues = []
contributor_type="issues"
json_file="autoware_launch_issues.json"
autoware_launch_issues += getContributors(json_file, contributor_type)
contributors += autoware_launch_issues

result="autoware_launch_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_launch_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_launch_prs = []
contributor_type="pullRequests"
json_file="autoware_launch_prs.json"
autoware_launch_prs += getContributors(json_file, contributor_type)
contributors += autoware_launch_prs

result="autoware_launch_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_launch_prs:
        fp.write("%s\n" % name)
    print('Done')

## autoware_documentation
autoware_documentation_issues = []
contributor_type="issues"
json_file="autoware_documentation_issues.json"
autoware_documentation_issues += getContributors(json_file, contributor_type)
contributors += autoware_documentation_issues

result="autoware_documentation_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_documentation_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_documentation_prs = []
contributor_type="pullRequests"
json_file="autoware_documentation_prs.json"
autoware_documentation_prs += getContributors(json_file, contributor_type)
contributors += autoware_documentation_prs

result="autoware_documentation_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_documentation_prs:
        fp.write("%s\n" % name)
    print('Done')

## autoware_ai

autoware_ai_issues = []
contributor_type="issues"
json_file="autoware_ai_issues.json"
autoware_ai_issues += getContributors(json_file, contributor_type)

result="autoware_ai_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_issues:
        fp.write("%s\n" % name)
    print('Done')

## autoware_ai_planning
autoware_ai_planning_issues = []
contributor_type="issues"
json_file="autoware_ai_planning_issues.json"
autoware_ai_planning_issues += getContributors(json_file, contributor_type)

result="autoware_ai_planning_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_planning_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_ai_planning_prs = []
contributor_type="pullRequests"
json_file="autoware_ai_planning_prs.json"
autoware_ai_planning_prs += getContributors(json_file, contributor_type)

result="autoware_ai_planning_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_planning_prs:
        fp.write("%s\n" % name)
    print('Done')

## autoware_ai_perception
autoware_ai_perception_issues = []
contributor_type="issues"
json_file="autoware_ai_perception_issues.json"
autoware_ai_perception_issues += getContributors(json_file, contributor_type)

result="autoware_ai_perception_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_perception_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_ai_perception_prs = []
contributor_type="pullRequests"
json_file="autoware_ai_perception_prs.json"
autoware_ai_perception_prs += getContributors(json_file, contributor_type)

result="autoware_ai_perception_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_perception_prs:
        fp.write("%s\n" % name)
    print('Done')

## autoware_ai_messages
autoware_ai_messages_issues = []
contributor_type="issues"
json_file="autoware_ai_messages_issues.json"
autoware_ai_messages_issues += getContributors(json_file, contributor_type)

result="autoware_ai_messages_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_messages_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_ai_messages_prs = []
contributor_type="pullRequests"
json_file="autoware_ai_messages_prs.json"
autoware_ai_messages_prs += getContributors(json_file, contributor_type)

result="autoware_ai_messages_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_messages_prs:
        fp.write("%s\n" % name)
    print('Done')

## autoware_ai_simulation
autoware_ai_simulation_issues = []
contributor_type="issues"
json_file="autoware_ai_simulation_issues.json"
autoware_ai_simulation_issues += getContributors(json_file, contributor_type)

result="autoware_ai_simulation_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_simulation_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_ai_simulation_prs = []
contributor_type="pullRequests"
json_file="autoware_ai_simulation_prs.json"
autoware_ai_simulation_prs += getContributors(json_file, contributor_type)

result="autoware_ai_simulation_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_simulation_prs:
        fp.write("%s\n" % name)
    print('Done')

## autoware_ai_visualization
autoware_ai_visualization_issues = []
contributor_type="issues"
json_file="autoware_ai_visualization_issues.json"
autoware_ai_visualization_issues += getContributors(json_file, contributor_type)

result="autoware_ai_visualization_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_visualization_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_ai_visualization_prs = []
contributor_type="pullRequests"
json_file="autoware_ai_visualization_prs.json"
autoware_ai_visualization_prs += getContributors(json_file, contributor_type)

result="autoware_ai_visualization_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_visualization_prs:
        fp.write("%s\n" % name)
    print('Done')

## autoware_ai_drivers
autoware_ai_drivers_issues = []
contributor_type="issues"
json_file="autoware_ai_drivers_issues.json"
autoware_ai_drivers_issues += getContributors(json_file, contributor_type)

result="autoware_ai_drivers_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_drivers_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_ai_drivers_prs = []
contributor_type="pullRequests"
json_file="autoware_ai_drivers_prs.json"
autoware_ai_drivers_prs += getContributors(json_file, contributor_type)

result="autoware_ai_drivers_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_drivers_prs:
        fp.write("%s\n" % name)
    print('Done')


## autoware_ai_utilities
autoware_ai_utilities_issues = []
contributor_type="issues"
json_file="autoware_ai_utilities_issues.json"
autoware_ai_utilities_issues += getContributors(json_file, contributor_type)

result="autoware_ai_utilities_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_utilities_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_ai_utilities_prs = []
contributor_type="pullRequests"
json_file="autoware_ai_utilities_prs.json"
autoware_ai_utilities_prs += getContributors(json_file, contributor_type)

result="autoware_ai_utilities_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_utilities_prs:
        fp.write("%s\n" % name)
    print('Done')

## autoware_ai_common
autoware_ai_common_issues = []
contributor_type="issues"
json_file="autoware_ai_common_issues.json"
autoware_ai_common_issues += getContributors(json_file, contributor_type)

result="autoware_ai_common_issues.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_common_issues:
        fp.write("%s\n" % name)
    print('Done')

autoware_ai_common_prs = []
contributor_type="pullRequests"
json_file="autoware_ai_common_prs.json"
autoware_ai_common_prs += getContributors(json_file, contributor_type)

result="autoware_ai_common_prs.txt"
with open(result, 'w') as fp:
    for name in autoware_ai_common_prs:
        fp.write("%s\n" % name)
    print('Done')
### ALL

print(type(contributors))
print(contributors)
print(len(contributors))
contributors = sorted(set(contributors))

result="all.txt"
with open(result, 'w') as fp:
    for name in contributors:
        fp.write("%s\n" % name)
    print('Done')

