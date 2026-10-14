
from flask import Flask, render_template # type: ignore

app = Flask(__name__)


# Route 1: Home
@app.get("/")
def home():
    return render_template("index.html")


# Route 2: About
@app.get("/about")
def about():
    return render_template("about.html")


# Route 3: Contact
@app.get("/contact")
def contact():
    return render_template("contact.html")


# Route 4: Services
@app.get("/services")
def services():
    return render_template("services.html")


# Route 5: Profile
@app.get("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
