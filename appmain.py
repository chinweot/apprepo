import git 

from flask import Flask, render_template, url_for, flash, redirect, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")  # do you have home.html in templates?


@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/chinweotapp/mysite/apprepo')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

if __name__ == "__main__":
    app.run()
