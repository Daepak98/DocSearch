import flask
from flask import Flask
from os import path
import doc_manager as dm

app = Flask(__name__)


@app.route("/")
def home_page():
    return "Home?"


@ app.route("/<doc_name>", methods=["GET"])
def get_doc(doc_name: str):
    response = dm.match_term_to_doc(doc_name)
    if response:
        return response
    else:
        return f"Doc `{doc_name}` not found", 404


if __name__ == "__main__":
    app.run(
        host="localhost",
        port=5000,
        debug=True
    )
