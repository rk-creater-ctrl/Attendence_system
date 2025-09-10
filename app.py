from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store attendance in a dictionary
attendance = {str(i): [] for i in range(1, 13)}

@app.route("/")
def home():
    return render_template("index.html", classes=attendance.keys())

@app.route("/mark", methods=["POST"])
def mark_attendance():
    cls = request.form["class"]
    roll = request.form["roll"]

    if cls in attendance:
        attendance[cls].append(roll)
    return redirect(url_for("home"))

@app.route("/class/<cls>")
def show_class(cls):
    return f"Class {cls}: {attendance.get(cls, [])}"

@app.route("/all")
def show_all():
    total = sum(len(students) for students in attendance.values())
    return render_template("all.html", attendance=attendance, total=total)

if __name__ == "__main__":
    app.run(debug=True)
