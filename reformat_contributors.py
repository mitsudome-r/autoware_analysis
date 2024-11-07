import json
from collections import OrderedDict
import pprint
import subprocess
import os
import datetime

# name , date
code_contributors = {}
community_contributors = {}
autoware_contributors = {}

# day , countup
code_contributors_per_day = {}
community_contributors_per_day = {}
autoware_contributors_per_day = {}


def get_awf_team(username):
    with open("team_members/autoware-developers-adastec.txt") as f:
      if username in f:
        return "adastec"
    with open("team_members/autoware-developers-adlink.txt") as f:
      if username in f:
        return "adlink"
    with open("team_members/autoware-developers-arm.txt") as f:
      if username in f:
        return "arm"
    with open("team_members/autoware-developers-autocore.txt") as f:
      if username in f:
        return "autocore"
    with open("team_members/autoware-developers-bogazici.txt") as f:
      if username in f:
        return "bogazici"
    with open("team_members/autoware-developers-driveblocks.txt") as f:
      if username in f:
        return "driveblocks"
    with open("team_members/autoware-developers-edutech.txt") as f:
      if username in f:
        return "edutech"
    with open("team_members/autoware-developers-esol.txt") as f:
      if username in f:
        return "esol"
    with open("team_members/autoware-developers-fixposition.txt") as f:
      if username in f:
        return "fixposition"
    with open("team_members/autoware-developers-foxconn.txt") as f:
      if username in f:
        return "foxconn"
    with open("team_members/autoware-developers-interplai.txt") as f:
      if username in f:
        return "interplai"
    with open("team_members/autoware-developers-itri.txt") as f:
      if username in f:
        return "itri"
    with open("team_members/autoware-developers-jdlogistics.txt") as f:
      if username in f:
        return "jdlogistics"
    with open("team_members/autoware-developers-leodrive.txt") as f:
      if username in f:
        return "leodrive"
    with open("team_members/autoware-developers-macnica.txt") as f:
      if username in f:
        return "macnica"
    with open("team_members/autoware-developers-map4.txt") as f:
      if username in f:
        return "map4"
    with open("team_members/autoware-developers-nagoya.txt") as f:
      if username in f:
        return "nagoya"
    with open("team_members/autoware-developers-pixmoving.txt") as f:
      if username in f:
        return "pixmoving"
    with open("team_members/autoware-developers-reka.txt") as f:
      if username in f:
        return "reka"
    with open("team_members/autoware-developers-robotec.txt") as f:
      if username in f:
        return "robotec"
    with open("team_members/autoware-developers-robotiz3d.txt") as f:
      if username in f:
        return "robotiz3d"
    with open("team_members/autoware-developers-springcloud.txt") as f:
      if username in f:
        return "springcloud"
    with open("team_members/autoware-developers-tum.txt") as f:
      if username in f:
        return "tum"
    with open("team_members/autoware-developers-udel.txt") as f:
      if username in f:
        return "udel"
    with open("team_members/autoware-developers-upenn.txt") as f:
      if username in f:
        return "upenn"
    with open("team_members/autoware-developers-wsu.txt") as f:
      if username in f:
        return "wsu"
    with open("tier4_engineers/tier4_engineers.txt") as f:
      if username in f:
        return "tier4"
    return ""


def get_user_info(username):
    print(username)
    file_name = "users/" + username + ".txt"
    if not os.path.exists(file_name):
      return None
    f = open(file_name, "r")
    loaded_json = json.load(f)

    orgs = []

    for org in loaded_json["data"]["user"]["organizations"]["nodes"]:
        orgs.append(org["login"])
    company = loaded_json["data"]["user"]["company"]
    user_info = {}
    user_info["name"] = username
    user_info["orgs"] = orgs
    user_info["company"] = company
    user_info["team"] = get_awf_team(username)

    return user_info


def create_table(file, pull_requests_table):
    f = open(file, "r")
    loaded_json = json.load(f)
    edges = loaded_json

    for x in edges:
        d = datetime.datetime.strptime(x["node"]["createdAt"], '%Y-%m-%dT%H:%M:%SZ')

        if x["node"]["author"] is not None:
            author = x["node"]["author"]["login"]
            if author not in contributors:
                contributors[author] = d
            elif contributors[author] > d:
                contributors[author] = d

        for y in x["node"]["comments"]["edges"]:
            if y["node"]["author"] is not None:
                d = datetime.datetime.strptime(y["node"]["createdAt"], '%Y-%m-%dT%H:%M:%SZ')
                author = y["node"]["author"]["login"]
                if author not in contributors:
                    contributors[author] = d
                elif contributors[author] > d:
                    contributors[author] = d


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

# writeToFile(sorted_pull_requests_table, "pull_requests.csv")
