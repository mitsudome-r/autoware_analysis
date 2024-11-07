import json
from collections import OrderedDict
import pprint
import subprocess

import datetime

# name , date
code_contributors = {}
community_contributors = {}
autoware_contributors = {}

# day , countup
code_contributors_per_day = {}
community_contributors_per_day = {}
autoware_contributors_per_day = {}

start_date = datetime.datetime(2022, 1, 1)
end_date = datetime.datetime.today()

def date_range(start, stop, step = datetime.timedelta(1)):
    current = start
    while current < stop:
        yield current
        current += step

def create_table(file, pull_requests_table):
    f = open(file, "r")
    loaded_json = json.load(f)
    edges = loaded_json

    for x in edges:
        d = datetime.datetime.strptime(x["node"]["createdAt"], '%Y-%m-%dT%H:%M:%SZ')
        date_filter = start_date

        # if d < date_filter:
        #     continue
        if x["node"]["merged"] == True:
            print(x["node"]["merged"])
            pull_requests_table.append([file, d, x["node"]["additions"], x["node"]["deletions"]])

    return pull_requests_table

def sort_table_by_date(pull_requests_table):
    # print(pull_requests_table)
    sorted_table = sorted(pull_requests_table, key=lambda x: x[1])

    return sorted_table


def writeToFile(pull_requests_table, file_name):
    print(pull_requests_table)
    with open("contributor_history/" + file_name, 'w') as fp:
        count = 0
        for item in pull_requests_table:
            line = item[0] + "," + item[1].strftime('%Y/%m/%d') + "," + str(item[2] ) + "," + str(item[3])
            fp.write("%s\n" % line)
    print('Done')


pull_requests_table = []
sorted_pull_requests_table = []

create_table("generated_json/autoware_prs.json", pull_requests_table)
create_table("generated_json/universe_prs.json", pull_requests_table)
create_table("generated_json/autoware_core_prs.json", pull_requests_table)
create_table("generated_json/autoware_common_prs.json", pull_requests_table)
create_table("generated_json/autoware_msgs_prs.json", pull_requests_table)
create_table("generated_json/autoware_launch_prs.json", pull_requests_table)
create_table("generated_json/autoware_documentation_prs.json", pull_requests_table)
create_table("generated_json/autoware_ai_prs.json", pull_requests_table)
create_table("generated_json/autoware_ai_perception_prs.json", pull_requests_table)
create_table("generated_json/autoware_ai_planning_prs.json", pull_requests_table)
create_table("generated_json/autoware_ai_messages_prs.json", pull_requests_table)
create_table("generated_json/autoware_ai_simulation_prs.json", pull_requests_table)
create_table("generated_json/autoware_ai_visualization_prs.json", pull_requests_table)
create_table("generated_json/autoware_ai_drivers_prs.json", pull_requests_table)
create_table("generated_json/autoware_ai_utilities_prs.json", pull_requests_table)
create_table("generated_json/autoware_ai_common_prs.json", pull_requests_table)

sorted_pull_requests_table = sort_table_by_date(pull_requests_table)

writeToFile(sorted_pull_requests_table, "pull_requests.csv")
