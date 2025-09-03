#!/usr/bin/bash

gh api graphql -F organization=$1 -F team=$2 -f query='
query($organization: String!, $team: String!){
  organization(login:$organization) {
    team(slug:$team) {
      members(first: 2){
        nodes{
          login
        }
        edges{
         cursor
        }
      }
    }
  }
}
' > tmp.txt
