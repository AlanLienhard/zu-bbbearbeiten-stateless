from flask import Flask, request, render_template, redirect, url_for
import helper

app = Flask(__name__)

@app.route("/")
def index():
    # get_all() liefert die Liste – NICHT eine Variable 'items'
    return render_template("index.html", items=helper.get_all())

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("text")
    due_date = request.form.get("due_date")   # 🔹 NEU: Datum aus Formular holen
    if title:                                 # 🔹 IF bleibt bestehen
        helper.add(title, due_date)           # 🔹 Datum ans helper.add() übergeben
    return redirect(url_for("index"))


@app.route("/update/<int:index>")
def update(index):
    helper.update(index)
    return redirect(url_for("index"))

# Für Azure brauchst du 'app' auf Modulebene, kein app.run()
if __name__ == "__main__":
    app.run(debug=True)
