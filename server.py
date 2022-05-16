from flask import Flask, render_template,request
import requests
import smtplib

data = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
print(data)
MY_EMAIL = "samigogo339@gmail.com"
PASSWORD = "samigogo1990"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("post.html")


@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        print(name)
        print(email)
        print(phone)
        print(message)
        with smtplib.SMTP("smtp.gmail.com", port=587) as letter:
            letter.starttls()
            letter.login(user=MY_EMAIL, password=PASSWORD)
            letter.sendmail(
                from_addr=MY_EMAIL,
                to_addrs= MY_EMAIL,
                msg= f"There is someone who tries to contact with you using your website. The person's data:\n\n Name: {name}\n\n Email: {email} \n\nPhone: {phone}\n\n Message: {message}"
            )
        return render_template("contact.html", title="Your message sent successfully")
    return render_template("contact.html", title="Contact Me")


@app.route("/index.html")
def to_home():
    return render_template("index.html")

@app.route("/form-entry", methods=["post"])
def from_entry():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    print(name)
    print(email)
    print(phone)
    print(message)
    return "<h1>YES, THANK GOD</h1>"


if __name__ == "__main__":
    app.run(debug="True")