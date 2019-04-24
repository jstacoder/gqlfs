from flask import Flask, render_template
from flask_graphql import GraphQLView
from graphqlfs.schema import schema


app = Flask(__name__, static_folder='dist')

@app.route('/')
def index():
    return render_template('index.html')

class MyGraphqlView(GraphQLView):
    schema = schema
    graphiql = True

app.add_url_rule('/graphiql', view_func=MyGraphqlView.as_view(name='giql'))

if __name__ == '__main__':
    app.run()
