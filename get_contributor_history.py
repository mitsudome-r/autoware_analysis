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

start_date = datetime.datetime(2022, 1, 1)
end_date = datetime.datetime.today()

def date_range(start, stop, step = datetime.timedelta(1)):
    current = start
    while current < stop:
        yield current
        current += step

def getContributors(file, contributors):
    f = open(file, "r")
    loaded_json = json.load(f)
    edges = loaded_json

    for x in edges:
        d = datetime.datetime.strptime(x["node"]["createdAt"], '%Y-%m-%dT%H:%M:%SZ')
        date_filter = start_date

        if d < date_filter:
            continue
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

    return contributors

def countContributorsPerDay(contributors, contributors_per_day):
    for contributor in contributors.keys():
        date = contributors[contributor]
        day = datetime.date(date.year, date.month, date.day)
        if day not in contributors_per_day:
            contributors_per_day[day]=1
        else:
            contributors_per_day[day]+=1
    contributors_per_day = sorted(contributors_per_day.items())

def writeToFile(contributors_per_day, file_name):
    with open("contributor_history/" + file_name, 'w') as fp:
        count = 0
        for item in sorted(contributors_per_day.items()):
            count += item[1]
            line = item[0].strftime('%Y/%m/%d') + "," + str(item[1])+"," + str(count)
            fp.write("%s\n" % line)
    print('Done')

def writeToCSV(autoware_contributors_per_day, code_contributors_per_day, community_contributors_per_day, file_name):
    with open("contributor_history/" + file_name, 'w') as fp:
        fp.write("date, autoware_contributors, code_contributors, community_contributors\n")
        autoware_contributor_count = 0
        code_contributor_count = 0
        community_contributor_count = 0
        for item in sorted(autoware_contributors_per_day.items()):
            date = item[0]
            count = item[1]

        for date in date_range(start_date,end_date):
            date_format = datetime.date(date.year,date.month,date.day)
            updated = False
            if date_format in autoware_contributors_per_day:
                autoware_contributor_count += autoware_contributors_per_day[date_format]
                updated = True
            if date_format in code_contributors_per_day:
                code_contributor_count+=code_contributors_per_day[date_format]
                updated = True
            if date_format in community_contributors_per_day:
                community_contributor_count+=community_contributors_per_day[date_format]
                updated = True

            if updated:
                line = date.strftime('%Y/%m/%d') + "," + str(autoware_contributor_count)+"," + str(code_contributor_count) + "," + str(community_contributor_count)
                print(line)
                fp.write("%s\n" % line)
    print('Done')

# name , date
code_contributors = {}
community_contributors = {}
autoware_contributors = {}

# day , countup
code_contributors_per_day = {}
community_contributors_per_day = {}
autoware_contributors_per_day = {}

getContributors("generated_json/autoware_discussions.json", community_contributors)
getContributors("generated_json/autoware_issues.json", community_contributors)
getContributors("generated_json/universe_issues.json", community_contributors)
getContributors("generated_json/autoware_core_issues.json", community_contributors)
getContributors("generated_json/autoware_common_issues.json", community_contributors)
getContributors("generated_json/autoware_msgs_issues.json", community_contributors)
getContributors("generated_json/autoware_launch_issues.json", community_contributors)
getContributors("generated_json/autoware_documentation_issues.json", community_contributors)
getContributors("generated_json/autoware_ai_issues.json", community_contributors)
getContributors("generated_json/autoware_ai_perception_issues.json", community_contributors)
getContributors("generated_json/autoware_ai_planning_issues.json", community_contributors)
getContributors("generated_json/autoware_ai_messages_issues.json", community_contributors)
getContributors("generated_json/autoware_ai_simulation_issues.json", community_contributors)
getContributors("generated_json/autoware_ai_visualization_issues.json", community_contributors)
getContributors("generated_json/autoware_ai_drivers_issues.json", community_contributors)
getContributors("generated_json/autoware_ai_utilities_issues.json", community_contributors)
getContributors("generated_json/autoware_ai_common_issues.json", community_contributors)
getContributors("generated_json/autoware_ai_issues.json", community_contributors)

getContributors("generated_json/autoware_prs.json", code_contributors)
getContributors("generated_json/universe_prs.json", code_contributors)
getContributors("generated_json/autoware_core_prs.json", code_contributors)
getContributors("generated_json/autoware_common_prs.json", code_contributors)
getContributors("generated_json/autoware_msgs_prs.json", code_contributors)
getContributors("generated_json/autoware_launch_prs.json", code_contributors)
getContributors("generated_json/autoware_documentation_prs.json", code_contributors)
# getContributors("generated_json/autoware_ai_prs.json", code_contributors)
getContributors("generated_json/autoware_ai_perception_prs.json", code_contributors)
getContributors("generated_json/autoware_ai_planning_prs.json", code_contributors)
getContributors("generated_json/autoware_ai_messages_prs.json", code_contributors)
getContributors("generated_json/autoware_ai_simulation_prs.json", code_contributors)
getContributors("generated_json/autoware_ai_visualization_prs.json", code_contributors)
getContributors("generated_json/autoware_ai_drivers_prs.json", code_contributors)
getContributors("generated_json/autoware_ai_utilities_prs.json", code_contributors)
getContributors("generated_json/autoware_ai_common_prs.json", code_contributors)


def get_awf_team(username):
    with open("team_members/autoware-developers-adastec.txt", 'r') as f:
      for line in f:
        if username in line:
          return "adastec"
    with open("team_members/autoware-developers-adlink.txt", 'r') as f:
      for line in f:
        if username in line:
          return "adlink"
    with open("team_members/autoware-developers-arm.txt", 'r') as f:
      for line in f:
        if username in line:
          return "arm"
    with open("team_members/autoware-developers-autocore.txt", 'r') as f:
      for line in f:
        if username in line:
          return "autocore"
    with open("team_members/autoware-developers-bogazici.txt", 'r') as f:
      for line in f:
        if username in line:
          return "bogazici"
    with open("team_members/autoware-developers-driveblocks.txt", 'r') as f:
      for line in f:
        if username in line:
          return "driveblocks"
    with open("team_members/autoware-developers-edutech.txt", 'r') as f:
      for line in f:
        if username in line:
          return "edutech"
    with open("team_members/autoware-developers-esol.txt", 'r') as f:
      for line in f:
        if username in line:
          return "esol"
    with open("team_members/autoware-developers-fixposition.txt", 'r') as f:
      for line in f:
        if username in line:
          return "fixposition"
    with open("team_members/autoware-developers-foxconn.txt", 'r') as f:
      for line in f:
        if username in line:
          return "foxconn"
    with open("team_members/autoware-developers-interplai.txt", 'r') as f:
      for line in f:
        if username in line:
          return "interplai"
    with open("team_members/autoware-developers-itri.txt", 'r') as f:
      for line in f:
        if username in line:
          return "itri"
    with open("team_members/autoware-developers-jdlogistics.txt", 'r') as f:
      for line in f:
        if username in line:
          return "jdlogistics"
    with open("team_members/autoware-developers-leodrive.txt", 'r') as f:
      for line in f:
        if username in line:
          return "leodrive"
    with open("team_members/autoware-developers-macnica.txt", 'r') as f:
      for line in f:
        if username in line:
          return "macnica"
    with open("team_members/autoware-developers-map4.txt", 'r') as f:
      for line in f:
        if username in line:
          return "map4"
    with open("team_members/autoware-developers-nagoya.txt", 'r') as f:
      for line in f:
        if username in line:
          return "nagoya"
    with open("team_members/autoware-developers-pixmoving.txt", 'r') as f:
      for line in f:
        if username in line:
          return "pixmoving"
    with open("team_members/autoware-developers-reka.txt", 'r') as f:
      for line in f:
        if username in line:
          return "reka"
    with open("team_members/autoware-developers-robotec.txt", 'r') as f:
      for line in f:
        if username in line:
          return "robotec"
    with open("team_members/autoware-developers-robotiz3d.txt", 'r') as f:
      for line in f:
        if username in line:
          return "robotiz3d"
    with open("team_members/autoware-developers-springcloud.txt", 'r') as f:
      for line in f:
        if username in line:
          return "springcloud"
    with open("team_members/autoware-developers-tum.txt", 'r') as f:
      for line in f:
        if username in line:
          return "tum"
    with open("team_members/autoware-developers-udel.txt", 'r') as f:
      for line in f:
        if username in line:
          return "udel"
    with open("team_members/autoware-developers-upenn.txt", 'r') as f:
      for line in f:
        if username in line:
          return "upenn"
    with open("team_members/autoware-developers-wsu.txt", 'r') as f:
      for line in f:
        if username in line:
          return "wsu"
    with open("tier4_engineers/tier4_engineers.txt", 'r') as f:
      for line in f:
        if username in line:
          return "tier4"
    return "None"

def get_user_info(username):
    print(username)
    user_info = {}
    user_info["name"] = "None"
    user_info["orgs"] = []
    user_info["company"] = "None"
    user_info["team"] = "None"
    file_name = "users/" + username + ".txt"
    if not os.path.exists(file_name):
      return user_info
    f = open(file_name, "r")
    loaded_json = json.load(f)

    orgs = []
    if "data" not in loaded_json:
      return user_info
    for org in loaded_json["data"]["user"]["organizations"]["nodes"]:
        orgs.append(org["login"])
    company = loaded_json["data"]["user"]["company"]
    user_info["name"] = username
    if len(orgs) > 0:
      user_info["orgs"] = orgs
    if company is not None:
      user_info["company"] = company
    if company == "":
      user_info["company"] = "None"

    user_info["team"] = get_awf_team(username)

    return user_info

def writeContributorToCSV(contributors, file_name):
    sorted_items_by_value = sorted(contributors.items(), key=lambda x: x[1])
    sorted_dict_by_value = {k: v for k, v in sorted_items_by_value}
    with open("contributor_history/" + file_name, 'w') as fp:
        fp.write("name;first date of contribution;company;org;awf-team\n")
        for key in sorted_dict_by_value.keys():
            user_info = get_user_info(key)
            org_string = ", ".join(user_info["orgs"])
            print(type(user_info["company"]))
            print(type(user_info["team"]))
            if org_string == "":
                org_string = "None"
            line = key + ";" + contributors[key].strftime('%Y/%m/%d') + ";" + user_info["company"] + ";" + org_string + ";" + user_info["team"]
            fp.write("%s\n" % line)
    print('Done')

writeContributorToCSV(community_contributors, "community_contributors.csv")
writeContributorToCSV(code_contributors, "code_contributors.csv")

## merge two dict
autoware_contributors = community_contributors.copy()
for author in code_contributors.keys():
    if author not in autoware_contributors:
        autoware_contributors[author] = code_contributors[author]
    elif autoware_contributors[author] > code_contributors[author]:
        autoware_contributors[author] = code_contributors[author]


## count per day
countContributorsPerDay(code_contributors, code_contributors_per_day)
countContributorsPerDay(community_contributors, community_contributors_per_day)
countContributorsPerDay(autoware_contributors, autoware_contributors_per_day)

writeToFile(code_contributors_per_day, "code_contributors_per_day.txt")
writeToFile(community_contributors_per_day, "community_contributors_per_day.txt")
writeToFile(autoware_contributors_per_day, "autoware_contributors_per_day.txt")

writeToCSV(autoware_contributors_per_day, code_contributors_per_day, community_contributors_per_day, "contributors_count.csv")

## TIER IV
def countTIERIVContributorsPerDay(contributors, contributors_per_day, engineer_filter):
    for contributor in contributors.keys():
        if contributor not in engineer_filter:
            continue
        date = contributors[contributor]
        day = datetime.date(date.year, date.month, date.day)
        if day not in contributors_per_day:
            contributors_per_day[day]=1
        else:
            contributors_per_day[day]+=1
    contributors_per_day = sorted(contributors_per_day.items())
def writeToCSV_TIERIV(autoware_contributors_per_day, code_contributors_per_day, community_contributors_per_day, tier4_autoware_contributors_per_day, tier4_code_contributors_per_day, tier4_community_contributors_per_day, file_name):
    with open("contributor_history/" + file_name, 'w') as fp:
        fp.write("date, autoware_contributors, code_contributors, community_contributors, tier4_autoware_contributors_per_day, tier4_code_contributors_per_day, tier4_community_contributors_per_day\n")
        autoware_contributor_count = 0
        code_contributor_count = 0
        community_contributor_count = 0

        tier4_autoware_contributor_count = 0
        tier4_code_contributor_count = 0
        tier4_community_contributor_count = 0

        for item in sorted(autoware_contributors_per_day.items()):
            date = item[0]
            count = item[1]

        for date in date_range(start_date,end_date):
            date_format = datetime.date(date.year,date.month,date.day)
            updated = False
            if date_format in autoware_contributors_per_day:
                autoware_contributor_count += autoware_contributors_per_day[date_format]
                updated = True
            if date_format in code_contributors_per_day:
                code_contributor_count+=code_contributors_per_day[date_format]
                updated = True
            if date_format in community_contributors_per_day:
                community_contributor_count+=community_contributors_per_day[date_format]
                updated = True
            if date_format in tier4_autoware_contributors_per_day:
                tier4_autoware_contributor_count += tier4_autoware_contributors_per_day[date_format]
                updated = True
            if date_format in tier4_code_contributors_per_day:
                tier4_code_contributor_count+=tier4_code_contributors_per_day[date_format]
                updated = True
            if date_format in tier4_community_contributors_per_day:
                tier4_community_contributor_count+=tier4_community_contributors_per_day[date_format]
                updated = True

            if updated:
                line = date.strftime('%Y/%m/%d') + "," + str(autoware_contributor_count)+"," + str(code_contributor_count) + "," + str(community_contributor_count) + "," + str(tier4_autoware_contributor_count)+"," + str(tier4_code_contributor_count) + "," + str(tier4_community_contributor_count)
                print(line)
                fp.write("%s\n" % line)
    print('Done')




tier4_engineers = []
with open("tier4_engineers/tier4_engineers.txt") as file:
    tier4_engineers = file.read().splitlines()

tier4_code_contributors_per_day = {}
tier4_community_contributors_per_day = {}
tier4_autoware_contributors_per_day = {}

countTIERIVContributorsPerDay(code_contributors, tier4_code_contributors_per_day, tier4_engineers)
countTIERIVContributorsPerDay(community_contributors, tier4_community_contributors_per_day, tier4_engineers)
countTIERIVContributorsPerDay(autoware_contributors, tier4_autoware_contributors_per_day, tier4_engineers)

writeToCSV_TIERIV(autoware_contributors_per_day, code_contributors_per_day, community_contributors_per_day, tier4_autoware_contributors_per_day, tier4_code_contributors_per_day, tier4_community_contributors_per_day, "tieriv_contributors_count.csv")
