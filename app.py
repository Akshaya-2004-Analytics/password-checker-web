from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 25
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 20
    else:
        suggestions.append("Include an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 20
    else:
        suggestions.append("Include a lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 20
    else:
        suggestions.append("Include a number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 15
    else:
        suggestions.append("Add a special character.")

    if score < 60:
        result = "Weak"
        color = "#e74c3c"
    elif score < 90:
        result = "Medium"
        color = "#f39c12"
    else:
        result = "Strong"
        color = "#2ecc71"

    return score, result, suggestions, color

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    score = 0
    suggestions = []
    color = "#ddd"
    
    if request.method == "POST":
        password = request.form["password"]
        score, result, suggestions, color = check_password_strength(password)

    return render_template("index.html", result=result, score=score, suggestions=suggestions, color=color)

if __name__ == "__main__":
    app.run(debug=True)
