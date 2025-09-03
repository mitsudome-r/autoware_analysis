#!/usr/bin/bash

gh api graphql -F username=$1 -f query='
query($username: String!){
  user(login:$username) {
    login
    name
    company
    id
    organizations(first: 100){
      nodes{
        login
        name
      }
    }
  }
}
' > users/$1.txt
