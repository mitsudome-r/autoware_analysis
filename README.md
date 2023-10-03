# Contributors Script

Contains scripts to count Autoware contributors

## How to use
Run the following to create json files and the list of contributors for each repository.

```
python generate_json.py
python count_contributors.py

python get_contributor_history.py
python get_tier4_engineers.py
python remove_tier4_engineers.py
python get_stars.py
python reformat_stargazers.py
```

Run the following to count contributors
`
wc -l autoware_contributors.txt #autoware_code_contributors.txt , autoware_community_contributors.txt
`

