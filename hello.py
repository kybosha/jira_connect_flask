from flask import Flask, render_template, send_from_directory
from flask import url_for

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

if __name__ == "__main__":
    app.run(debug=True)
