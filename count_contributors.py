import json
from collections import OrderedDict
import pprint
import subprocess

import datetime

def getContributors(file, use_filter = False):
    print("counting contributors for", file)

    f = open(file, "r")
    loaded_json = json.load(f)
    edges = loaded_json

    contributors=[]

    date_filter = datetime.datetime(2022, 1, 1)

    for x in edges:
        # skip if before 2022-01-01 (before Core / Universe transition)
        d = datetime.datetime.strptime(x["node"]["createdAt"], '%Y-%m-%dT%H:%M:%SZ')
        if use_filter and d < date_filter:
            continue

        if x["node"]["author"] is not None:
            contributors.append(x["node"]["author"]["login"])
        for y in x["node"]["comments"]["edges"]:
            if y["node"]["author"] is not None:
                contributors.append(y["node"]["author"]["login"])

    contributors = sorted(set(contributors))
    print("total contributors:", len(contributors))
    return contributors

def writeNamesToFile(names, file_name):
    with open("contributor_names/"+file_name, 'w') as fp:
        for name in names:
            fp.write("%s\n" % name)
    print('written to', file_name)

contributors = []
autoware_code_contributors = []
autoware_community_contributors = []
autoware_contributors = []

## special case for autoware_discussions
autoware_discussions = []
json_file="generated_json/autoware_discussions.json"
autoware_discussions += getContributors(json_file, True)
contributors += autoware_discussions
writeNamesToFile(autoware_discussions, "autoware_discussions.txt")

# autoware repositories
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
    "autoware_tools",
    "autoware.privately-owned-vehicles",
    "autoware-documentation",
    "openadkit"
]

for repository in repositories:
    issues = []
    json_file="generated_json/"+repository+"_issues.json"
    issues += getContributors(json_file, True)
    autoware_community_contributors += issues
    writeNamesToFile(issues, repository+"_issues.txt")

    pull_requests = []
    json_file="generated_json/"+repository+"_prs.json"
    pull_requests += getContributors(json_file, True)
    autoware_code_contributors += pull_requests
    writeNamesToFile(pull_requests, repository+"_prs.txt")


# autoware_ai repositories
count_ai_repositories = False

if count_ai_repositories:
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

    for repository in autoware_ai_repositories:
        issues = []
        contributor_type="issues"
        json_file="generated_json/"+repository+"_issues.json"
        issues += getContributors(json_file, False)
        autoware_community_contributors += issues
        writeNamesToFile(issues, repository+"_issues.txt")

        pull_requests = []
        contributor_type="pullRequests"
        json_file="generated_json/"+repository+"_prs.json"
        pull_requests += getContributors(json_file, False)
        autoware_code_contributors += pull_requests
        writeNamesToFile(pull_requests, repository+"_prs.txt")

### ALL
print("autoware_code_contributors:", len(autoware_code_contributors))
print("autoware_community_contributors:", len(autoware_community_contributors))
print("autoware_contributors:", len(autoware_contributors))

autoware_contributors = autoware_code_contributors + autoware_community_contributors

# count only unique contributors
autoware_code_contributors = sorted(set(autoware_code_contributors))
autoware_community_contributors = sorted(set(autoware_community_contributors))
autoware_contributors = sorted(set(autoware_contributors))

writeNamesToFile(autoware_code_contributors, "autoware_code_contributors.txt")
writeNamesToFile(autoware_community_contributors, "autoware_community_contributors.txt")
writeNamesToFile(autoware_contributors, "autoware_contributors.txt")
