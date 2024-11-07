#!/usr/bin/bash

gh api graphql -F team=$1 -f query='
query($team: String!){
  organization(login:"autowarefoundation") {
    team(slug: $team) {
      members(first: 100){
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
' > team_members/$1.txt
