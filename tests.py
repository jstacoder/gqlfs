from gql import gql

def test_schema_has_query(schema):
    assert schema.Query() is not None, 'Schema does not have a Query field'

def test_hello_world_query(client):
    query = gql('''
        query HelloWorld($msg: String!) {
            hello(msg: $msg) {
                message
            }
        }
    ''')
    result = client.execute(query, variables=dict(msg='world'))
    assert 'hello' in result
    assert 'message' in result['hello']
    assert result['hello']['message'] is not None
    assert 'hello world' in result['hello']['message']


def test_hello_type_query(client):
    query = gql('''
        query HelloWorld($msg: String!) {
            hello(msg: $msg) {
                itemType
            }
        }
    ''')
    result = client.execute(query, variables=dict(msg='world'))
    assert 'hello' in result
    assert 'itemType' in result['hello']
    assert result['hello']['itemType'] is not None
    assert result['hello']['itemType'] == 'File'


def test_type_query(client):
    query = gql('''
        query ItemType($typeName: ItemTypeEnum) {
            itemType(typeName: $typeName) {
                typeName
            }
        }
    ''')
    result = client.execute(query, variables=dict(typeName='Directory'))

def test_directory_query(client):
    query = gql('''
        query Directory{
            getDirectory{
                itemType {
                    typeName
                }
            }
        }
    ''')
    result = client.execute(query)
    assert 'getDirectory' in result
    assert 'itemType' in result['getDirectory']
    