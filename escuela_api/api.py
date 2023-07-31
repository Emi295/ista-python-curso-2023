import flask

app = flask.Flask(__name__)

@app.route("/hola_mundo")
def hola_mundo():
    return "<h1>Hola mundo</h1>"