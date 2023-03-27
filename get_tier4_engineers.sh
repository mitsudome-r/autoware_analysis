#!/usr/bin/bash

gh api graphql -f query='
query{
  organization(login:"tier4") {
    discussions(first:100, after: $cursor) {
      totalCount
      edges {
        cursor
        node {
          author{
            login
          }
          title
          createdAt
          comments(first:100) {
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
