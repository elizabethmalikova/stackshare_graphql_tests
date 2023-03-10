from graphql_tests.helper import base_url
import requests
from test_contactBySlug import test_contactBySlug

query = """
query userStacksUsing($id: ID!, $after: String, $first: Int) {
  tool(id: $id) {
    userStacksUsing(first: $first, after: $after) {
      count
      pageInfo {
        hasNextPage
        endCursor
        __typename
      }
      edges {
        node {
          name
          imageUrl
          thumbUrl
          thumbRetinaUrl
          identifier
          id
          __typename
        }
        __typename
      }
      __typename
    }
    id
    __typename
  }
}
"""


def test_userStacksUsing():
    tool_id = test_contactBySlug()
    variables = {
        "id": tool_id,
        "first": 9
    }
    response = requests.post(base_url, json={"query": query, "variables": variables})
    response.raise_for_status()
    assert response.json()['data']['tool']['userStacksUsing']['count'] > 0
