#!/usr/bin/bash

gh api graphql -f query='
query{
  organization(login:"autowarefoundation") {
    teams(first: 100) {
      nodes{
        name
        slugteam
        members{
          totalCount
        }
      }
    }
  }
}
' > tmp.txt
