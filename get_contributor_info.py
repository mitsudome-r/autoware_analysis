import json
from collections import OrderedDict
import pprint
import subprocess

import os

def list_files_in_directory(directory_path):
    """
    List all files in the specified directory.

    Args:
        directory_path (str): Path to the directory to list files from

    Returns:
        list: A list of filenames in the directory
    """
    try:
        # Get all files in the directory
        files = os.listdir(directory_path)
        return files
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found")
        return []
    except PermissionError:
        print(f"Error: Permission denied to access directory '{directory_path}'")
        return []

def exists_in_a_file(file_path, search_text):
    """
    Check if a specific text exists in a file.

    Args:
        file_path (str): Path to the file to search in
        search_text (str): Text to search for

    Returns:
        bool: True if the text is found, False otherwise
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return search_text in content
    except Exception as e:
        print(f"Error occurred while reading file: {e}")
        return False


def parse_user_info(file_path):
    user = None
    with open(file_path, "r") as f:
        data = json.load(f)
        print(file_path)
        if data["data"]["user"] != None:
            user = {}
            user["name"] = data["data"]["user"]["login"]
            user["company"] = data["data"]["user"]["company"]
            if user["company"] == None:
                user["company"] = "none"
            user["organizations"] = []
            for organization in data["data"]["user"]["organizations"]["nodes"]:
                user["organizations"].append(organization["login"])
            user["team"] = "none"
            if exists_in_a_file("tier4_engineers/autoware_developers_leodrive.txt", user["name"]):
                user["team"] = "leodrive"
            elif exists_in_a_file("tier4_engineers/autoware_developers_autocore.txt", user["name"]):
                user["team"] = "autocore"
            elif exists_in_a_file("tier4_engineers/autoware_developers_tier4.txt", user["name"]):
                user["team"] = "tier4"
            elif exists_in_a_file("tier4_engineers/tier4_engineers.txt", user["name"]):
                user["team"] = "tier4"

            if "autocore" in user["company"]:
                user["team"] = "autocore"
            elif "Leo Drive" in user["company"]:
                user["team"] = "leodrive"
            # elif "TIER IV" in user["company"]:
            #     user["team"] = "tier4"
        else:
            user = {}
            user["name"] = file_path.split("/")[-1].split(".")[0]
            user["company"] = "none"
            user["organizations"] = []
            user["team"] = "none"
    return user

file_list = list_files_in_directory("users")


users = []
for file in file_list:
    user = parse_user_info(f"users/{file}")
    if user != None:
        users.append(user)

print(users)

with open("contributor_names/user_info.txt", "w") as f:
    for user in users:
        print (user["name"])
        f.write(f"{user['name']}:{user['company']}:{user['organizations']}:{user['team']}\n")
