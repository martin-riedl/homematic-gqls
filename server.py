#!/usr/bin/python3

__author__ = "Martin Riedl"
__copyright__ = "Copyright 2020"
__credits__ = [
    "coreGreenberet (https://github.com/coreGreenberet)", 
    "hahn-th (https://github.com/hahn-th/homematicip-rest-api)",
    "Seth Corker (https://blog.sethcorker.com/how-to-create-a-react-flask-graphql-project)"
]
__license__ = "GPL"
__maintainer__ = "Martin Riedl"

from flask import Flask, request, jsonify
from ariadne import graphql_sync, make_executable_schema, gql, load_schema_from_path
from ariadne.explorer import ExplorerGraphiQL

from model import query

type_defs = gql(load_schema_from_path("./schema.graphql"))
schema = make_executable_schema(type_defs, query)

explorer_html = ExplorerGraphiQL().html(None)

app = Flask(__name__)

# Switch caching off

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    """Serve GraphQL playground"""
    if 'query' in request.args:
        # serve query
        success, result = graphql_sync(
            schema,
            {
                "query" : request.args['query']
            }
        )
        status_code = 200 if success else 400
        return jsonify(result), status_code
    else:
        # only serve playground if no query argument is given ...
        return explorer_html, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    #print(data)
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8191)

