#!/usr/bin/bash

gh api graphql -F organization=$1 -F team=$2 -F cursor=$3 -f query='
query($organization: String!, $team: String!, $cursor: String!){
  organization(login:$organization) {
    team(slug:$team) {
      members(first: 100 after: $cursor){
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
