from flask import Flask, render_template, send_from_directory, jsonify, request, Response
from flask import url_for
import json

app = Flask(__name__, static_url_path='/atlassian-connect', static_folder='static')

@app.route("/")
def status():
    return "I am very much alive!"

@app.route("/helloworld.html")
def action():
    return send_from_directory(app.static_folder, 'jiraCat.html')

@app.route("/atlassian-connect")
def descriptor():
    return render_template('atlassian-connect.json')
    #return url_for('static', filename='atlassian-connect.json')

@app.route("/atlassian-connect/installed", methods=['POST'])
def installed():
    print("Installed hook received.")
    data = request.data
    print(data)
    return json.dumps({'success': True}), 200, {'Content-Type': 'application/json'} 

@app.route("/atlassian-connect/uninstalled", methods=['POST'])
def uninstalled():
    print("Uninstalled hook received.")
    data = request.data
    print(data)
    return json.dumps({'success': True}), 200, {'Content-Type': 'application/json'} 

@app.route("/atlassian-connect/enabled", methods=['POST'])
def enabled():
    print("Enabled hook received.")
    data = request.data
    print(data)
    return json.dumps({'success': True}), 200, {'Content-Type': 'application/json'} 

@app.route("/atlassian-connect/disabled", methods=['POST'])
def disabled():
    print("Disabled hook received.")
    data = request.data
    print(data)
    return json.dumps({'success': True}), 200, {'Content-Type': 'application/json'} 

if __name__ == "__main__":
    app.run(debug=True)

