import os

from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()


@app.route("/")
def home():
    return render_template("profile.html")


@app.route("/shop")
def shop():
    return render_template("coming-soon.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/send-message", methods=["POST"])
def send_message():
    try:
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        full_message = f"""
        New message from Ela Arts Contact Page:

        Name: {name}
        Email: {email}
        Phone: {phone}

        Message:
        {message}
        """

        msg = MIMEText(full_message)
        msg["Subject"] = "New Contact Form Message"
        msg["From"] = email
        msg["To"] = "elahesadeghi.art@gmail.com"

        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        gmail_user = "elahesadeghi.art@gmail.com"
        gmail_password = os.getenv("GMAIL_PASSWORD")

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(gmail_user, gmail_password)
            server.send_message(msg)

        return render_template("contact.html", success=True)

    except Exception as e:
        print("Email error:", e)
        return render_template("contact.html", error=True)


@app.route("/blog")
def blog():
    return render_template("coming-soon.html")

@app.route("/log-in")
def log_in():
    return render_template("coming-soon.html")

@app.route("/cart")
def cart():
    return render_template("coming-soon.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/shipping-and-return")
def shipping_and_return():
    return render_template("shipping-and-return.html")

@app.route("/policy")
def policy():
    return render_template("store-policy.html")

# @app.route("/search")
# def search():
#     query = request.args.get('q', '')
#     # For now, just redirect to home with the search query
#     # You can implement actual search logic here later
#     return render_template("profile.html", search_query=query)

if __name__ == "__main__":
    app.run(debug=True)
