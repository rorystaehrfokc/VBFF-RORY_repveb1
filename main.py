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
    language = request.cookies.get("lange", "")
    text = 0

    first_write = False
    language = "en"
    #first line
    with open(f'../translated/home_{language}.txt', 'r') as f:
        text = f.readline(2)

    with open(f'../translated/home_{language}.txt', 'r') as f:
        text = f.readline(3)

    with open(f'../translated/home_{language}.txt', 'r') as f:
        text = f.readline(4)

    return render_template('home.html',
                           title="Home")
    

#About
@app.route('/about')
def about():
    language = request.cookies.get("lange", "")
    text = 0

    first_write = False
    language = "en"
    #first line
    with open(f'../translated/home_{language}.txt', 'r') as f:
        text = f.readline(2)

    with open(f'../translated/home_{language}.txt', 'r') as f:
        text = f.readline(3)

    with open(f'../translated/home_{language}.txt', 'r') as f:
        text = f.readline(4)
    return  render_template('about.html',
                            title="About")


@app.route('/querystring')
def quertstring():
    language = request.cookies.get("lange", "")
    text = 0

    first_write = False
    language = "en"
    #first line
    with open(f'../translated/home_{language}.txt', 'r') as f:
        text = f.readline(2)

    with open(f'../translated/home_{language}.txt', 'r') as f:
        text = f.readline(3)

    with open(f'../translated/home_{language}.txt', 'r') as f:
        text = f.readline(4)
    name = request.args.get("name")
    age = request.args.get("age")
    nationality = request.args.get("nationality")
    cookie_name = request.args.get("cookie_name")

    if cookie_name == "Save":
        set_cookie("name", name)
        pass
    else:
        pass
    name = request.cookies.get("name", "")
    return  render_template('querystring.html',
                            title="Querystring",
                            name=name,
                            age=age,
                            nationality=nationality)
    
    

@app.route('/messages')
def messeges():
    language = request.cookies.get("lange", "")
    text = 0

    first_write = False
    language = "en"
    #first line
    with open(f'../translated/home_{language}.txt', 'r') as f:
        text = f.readline(2)

    with open(f'../translated/home_{language}.txt', 'r') as f:
        text = f.readline(3)

    with open(f'../translated/home_{language}.txt', 'r') as f:
        text = f.readline(4)
    return  render_template('messages.html',
                            title="Messages",
                            messages = messages)

@app.route("/messages/write", methods=["GET", "POST"])
def write():
    language = request.cookies.get("lange", "")
    text = 0

    first_write = False
    language = "en"
    #first line
    with open(f'../translated/home_{language}.txt', 'r') as f:
        text = f.readline(2)

    with open(f'../translated/home_{language}.txt', 'r') as f:
        text = f.readline(3)

    with open(f'../translated/home_{language}.txt', 'r') as f:
        text = f.readline(4)
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        
        # Validate inputs
        if not name or not message:
            return "Name and message cannot be empty!", 400
        
        # Get current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Save message
        messages[timestamp] = {"name": name, "message": message}
        
        # Save to disk
        with open(MESSAGES_FILE, "w") as file:
            json.dump(messages, file, indent=4)
        
        # Store name in cookie
        resp = make_response(redirect("/messeges"))
        resp.set_cookie("name", name)
        return resp
    
    # Pre-fill name from cookie if available
    name = request.cookies.get("name", "")
    return render_template("write.html", name=name)

@app.route("/set_cookie")
def set_cookie():
    response = make_response("Cookie set")
    response.set_cookie("name", "cookie_value")
    return response

@app.route("/get_cookie")
def get_cookie():
    cookie_value = request.cookies.get("name")
    return cookie_value

@app.route("/delete_cookie")
def delete_cookie():
    response = make_response("Cookie Deleted")
    response.delete_cookie("name")
    return response

if __name__ == '__main__':
        app.run(debug=True, port=8080)