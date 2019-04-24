from collections import namedtuple
import pytest
import mock
from gql import Client, gql



from graphqlfs.schema import schema as gql_schema

@pytest.fixture
def schema():
    return gql_schema

@pytest.fixture
def client(schema):
    return Client(schema=schema)
    
