# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# in-memory task store (like your CLI to_do list)
to_do = []

@app.route("/")
def index():
    # render the HTML page and pass current tasks
    return render_template("index.html", tasks=to_do)

@app.route("/add", methods=["POST"])
def add():
    # get the value of the form field named "task"
    task = request.form.get("task", "").strip()
    if task:                # ignore empty submissions
        to_do.append(task)  # add to the list
    # Redirect back to the index page (POST -> Redirect -> GET pattern)
    return redirect(url_for("index"))

@app.route("/remove/<int:index>")
def remove(index):
    # index is 0-based (we'll show 1-based numbers in the UI)
    if 0 <= index < len(to_do):
        del to_do[index]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
