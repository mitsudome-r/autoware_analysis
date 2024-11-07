#!/usr/bin/bash

gh api graphql -F user_name=$1 -f query='
query($user_name: String!){
  user(login: $user_name) {
    name
    organizations(first: 100) {
      nodes {
        login
      }
    }
    company
    id
  }
}
' > users/$1.txt
