#!/usr/bin/bash

gh api graphql -F repository=$1 -f query='
query($repository: String!) {
  repository(owner:"autowarefoundation", name:$repository) {
    pullRequests(first:2) {
      totalCount
      edges {
        cursor
        node {
          author{
            login
          }
          title
          comments(first:1) {
            edges {
                node {
                    author{
                        login
                    }
                }
            }
          }
        }
      }
    }
  }
}
' > tmp.txt
