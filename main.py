# import table
from flask import Flask, request, redirect, render_template, make_response, url_for
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
    if request.cookies.get("First_time", "") == "no":
        pass
    else:
        return redirect('/set_language', "home")
    if request.cookies.get("language", "") == "da" or "en" or "Jp":
        language = request.cookies.get("language", "")
    else:
        language = "en"
        set_cookie("language", language)
    language = "en"
    language_file = f"translated/about_{language}.json"
    if os.path.exists(language_file):
        with open(language_file, "r") as fp:
           lang = json.load(fp)
    else:
        lang = {}
        with open(f'./translate/about_{language}.json', 'w') as fp:
           json.dump(lang, fp)
        pass
    return render_template('home.html',
                           title="Home")
    

#About
@app.route('/about')
def about():
    if request.cookies.get("First_time", "") == "no":
        pass
    else:
        return redirect('/set_language', "about")
    if request.cookies.get("language", "") == "da" or "en" or "Jp":
        language = request.cookies.get("language", "")
    else:
        language = "en"
        set_cookie("language", language)
    language_file = "translated/home_{language}.json"
    if os.path.exists(language_file):
        with open(language_file, "r") as file:
            #Insert dictonary
            pass
    else:
        #Insert dictonary_2
        pass
    return  render_template('about.html',
                            title="About")


@app.route('/querystring')
def quertstring():
    if request.cookies.get("First_time", "") == "no":
        pass
    else:
        return redirect('/set_language', "querystring")
    if request.cookies.get("language", "") == "da" or "en" or "Jp":
        language = request.cookies.get("language", "")
    else:
        language = "en"
        set_cookie("language", language)
    language_file = "translated/home_{language}.json"
    if os.path.exists(language_file):
        with open(language_file, "r") as file:
            #Insert dictonary
            pass
    else:
        #Insert dictonary_2
        pass
    name = request.args.get("name")
    age = request.args.get("age")
    language = request.args.get("language")
    cookie_name = request.args.get("cookie_name")

    if cookie_name == "Save":
        set_cookie("name", name, "age", age)
    return  render_template('querystring.html',
                            title="Querystring",
                            name=name,
                            age=age,
                            language=language)
    
    

@app.route('/messages')
def msg():
    if request.cookies.get("First_time", "") == "no":
        pass
    else:
        return redirect('/set_language', "messages")
    if request.cookies.get("language", "") == "da" or "en" or "Jp":
        language = request.cookies.get("language", "")
    else:
        language = "en"
        set_cookie("language", language)
    language_file = "translated/home_{language}.json"
    if os.path.exists(language_file):
        with open(language_file, "r") as file:
            #Insert dictonary
            pass
    else:
        #Insert dictonary_2
        pass
    return  render_template('messages.html',
                            title="Messages",
                            messages = messages)

@app.route("/messages/write", methods=["GET", "POST"])
def write():
    if request.cookies.get("First_time", "") == "no":
        pass
    else:
        return redirect('/set_language', "messages")
    if request.cookies.get("language", "") == "da" or "en" or "Jp":
        language = request.cookies.get("language", "")
    else:
        language = "en"
        set_cookie("language", language)
    language_file = "translated/home_{language}.json"
    if os.path.exists(language_file):
        with open(language_file, "r") as file:
            #Insert dictonary
            pass
    else:
        #Insert dictonary_2
        pass
   
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
        resp = make_response(redirect("/messages"))
        resp.set_cookie("name", name)
        return resp
    
    # Pre-fill name from cookie if available
    name = request.cookies.get("name", "")
    return render_template("write.html", name=name)

@app.route("/set_language")
def set_language():
    set__language = ""
    language = request.args.get("language")
    set__language.set_cookie("language", language)
    return render_template("set_language.html",
                           language = language)
                           

@app.route("/set_cookie")
def set_cookie():
    response = make_response("Cookie set")
    response.set_cookie("name",)
    return response

@app.route("/get_cookie")
def get_cookie():
    cookie_value = request.cookies.get("name", "", "age", "", "language", "")
    return cookie_value

@app.route("/delete_cookie")
def delete_cookie():
    response = make_response("Cookie Deleted")
    response.delete_cookie("name", "age", "language")
    return response

if __name__ == '__main__':
        app.run(debug=True, port=8080)
