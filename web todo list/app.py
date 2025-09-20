# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


to_do = []

@app.route("/")
def index():

    return render_template("index.html", tasks=to_do)

@app.route("/add", methods=["POST"])
def add():
  
    task = request.form.get("task", "").strip()
    if task:
        to_do.append(task)  
 
    return redirect(url_for("index"))

@app.route("/remove/<int:index>")
def remove(index):
    
    if 0 <= index < len(to_do):
        del to_do[index]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

