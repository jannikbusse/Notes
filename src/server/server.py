import flask
from flask import abort
import db
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.


@app.route('/todo/api/v1.0/notes', methods=['POST'])
def create_task():
    if not request.json or not 'content' in request.json or not 'thread' in request.json or not 'channel' in request.json:
        abort(404)

    thread = request.json["thread"]
    channel = request.json["channel"]
    content = request.json["content"]

    db.add_note(thread, channel, content)

    return "done!"


@app.route('/todo/api/v1.0/notes/delete', methods=['POST'])
def delete():    
    if not request.json or not 'id' in request.json :
        abort(404)

    id = request.json["id"]
    db.delete_note(id)

    return "done!"

 
@app.route('/todo/api/v1.0/notes', methods=['GET'])
def get_tasks():
    if not request.json or not 'thread':
        abort(404)

    thread = request.json["thread"]
    res = db.get_notes(thread)
    print("\n")
    print(res)
    print("\n")
    return jsonify(res)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify("hello")


db.create_table()
app.run()
