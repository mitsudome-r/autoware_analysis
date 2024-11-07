#!/usr/bin/bash

gh api graphql -F cursor=$1 -F repository=$2 -f query='
query($cursor: String!, $repository: String!) {
  repository(owner:"autowarefoundation", name:$repository) {
    pullRequests(first:100, after: $cursor) {
      totalCount
      edges {
        cursor
        node {
          author{
            login
          }
          title
          createdAt
          merged
          additions
          deletions
          comments(first:100) {
            edges {
                node {
                    author{
                        login
                    }
                    createdAt
                }
            }
          }
        }
      }
    }
  }
}
' > tmp.txt
