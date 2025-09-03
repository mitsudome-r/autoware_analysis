#!/usr/bin/bash

gh api graphql -f query='
query{
  organization(login:"autowarefoundation") {
    team(slug: "autoware-developers"){
      childTeams(first: 100){
        nodes{
          name
        }
      }
    }
  }
}
' > tmp.txt
