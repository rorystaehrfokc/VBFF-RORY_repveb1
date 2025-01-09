# import table
from flask import Flask, request, redirect, render_template, make_response, url_for
from datetime import datetime
import json, os

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

#redirects to home en
@app.route('/')
def sendtohome():
    return(redirect('/en/home'))

#redirets to the page in en
@app.route('/<page>')
def sendtopage(page):
    if page == 'en' or 'da' or 'jp':
        return(redirect(f'/{page}/home'))
    return(redirect(f'/en/{page}'))

#redirects to en if language is none
def ifnone(lang, page):
    if lang == "none":
        return redirect(f'/en/{page}')

#lodes the language file
def getpagelang(lang, page):
    language_file = f"translated/{page}_{lang}.json"
    if os.path.exists(language_file):
        with open(language_file, "r") as fp:
           langu = json.load(fp)
    else:
        langu = {}
        with open(language_file, "w") as fp:
           json.dump(langu, fp)
        pass
    return (langu)

#Home
@app.route('/<language>/home')
def home(language):
    page = "home"
    langu = getpagelang(language, page)
    return render_template('home.html',
                           title="Home",
                           language=language,
                           langu=langu) 

#About
@app.route('/<language>/about')
def about(language):
    page = "about"
    getpagelang(language, page)
    return  render_template('about.html',
                            title="About",
                            language=language)
    
#Messages
@app.route('/<language>/messages')
def msg(language):
    page = "messages"
    getpagelang(language, page)
    return  render_template('messages.html',
                            title="Messages",
                            messages = messages,
                            language=language)

#Write
@app.route("/<language>/messages/write", methods=["GET", "POST"])
def write(language):
    page = "write"
    getpagelang(language, page)
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
    return render_template("write.html",
                           name=name,
                           language=language)       

@app.route('/howdidyougetthislink/set_cookie')
def set_cookie():
    response = make_response("Cookie set")
    response.set_cookie("name",)
    return response

@app.route("/howdidyougetthislink/get_cookie")
def get_cookie():
    cookie_value = request.cookies.get("name", "", "age", "", "language", "")
    return cookie_value

@app.route("/howdidyougetthislink/delete_cookie")
def delete_cookie():
    response = make_response("Cookie Deleted")
    response.delete_cookie("name", "age", "language")
    return response

if __name__ == '__main__':
        app.run(debug=True, port=8080)
