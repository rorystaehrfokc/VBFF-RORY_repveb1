from flask import Flask, render_template, request
import io, random


app = Flask(__name__,
            static_folder="static",
            static_url_path="/")

@app.route('/')
def home():
    return render_template('home.html',
                           title="Home")

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

@app.route('/msg')
def msg():
    messeges = [
        
    ]
    return  render_template('msg.html',
                            title="Msg")


if __name__ == '__main__':
    app.run(debug=True, port=8080)

