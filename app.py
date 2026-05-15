from flask import Flask, render_template

app = Flask(__name__)

showing_name = False

@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/partials/toggle")
def toggle_name():
    global showing_name

    showing_name = not showing_name

    if showing_name:
        return "<h1>Corey Krzyzanowski</h1>"
    else:
        return "Display name here"

if __name__ == "__main__":
    app.run(debug=True)
