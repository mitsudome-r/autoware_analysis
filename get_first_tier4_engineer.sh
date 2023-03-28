#!/usr/bin/bash

gh api graphql -f query='
query{
  organization(login:"tier4") {
    team(slug:"full-time-employee") {
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
