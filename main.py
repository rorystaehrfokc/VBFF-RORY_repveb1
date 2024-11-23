# import table
from flask import Flask, request, redirect, render_template, make_response
import io, json, os
from datetime import datetime

# Flask initialaize
app = Flask(__name__,
            static_folder="static",
            static_url_path="/")

# File to store messages
MESSAGES_FILE = "messages.json"

# Load messages from disk or initialize
if os.path.exists(MESSAGES_FILE):
    with open(MESSAGES_FILE, "r") as file:
        messages = json.load(file)
else:
    messages = {}


# Home
@app.route('/')
def home():
    return render_template('home.html',
                           title="Home")

#About
@app.route('/about')
def about():
    return  render_template('about.html',
                            title="About")


@app.route('/querystring')
def quertstring():
    name = request.args.get("name")
    age = request.args.get("age")
    nationality = request.args.get("nationality")
    return  render_template('querystring.html',
                            title="Querystring",
                            name=name,
                            age=age,
                            nationality=nationality)

@app.route('/messeges')
def messeges():
    return  render_template('messeges.html',
                            title="Messeges")


@app.route("/set_cookie")
def set_cookie():
    response = make_response("Cookie set")
    response.set_cookie("cookie_name", "cookie_value")
    return response

@app.route("/get_cookie")
def get_cookie():
    cookie_value = request.cookies.get("cookie_name")
    return cookie_value

@app.route("/delete_cookie")
def delete_cookie():
    response = make_response("Cookie Deleted")
    response.delete_cookie("cookie_name")
    return response



if __name__ == '__main__':
    app.run(debug=True, port=8080)

