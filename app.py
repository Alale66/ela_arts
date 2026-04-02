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

blog_posts = [
    {
        "slug": "the-story",
        "title": "The Story of Elahe Sadeghi and the Birth of Ela Arts",
        "author": "Elahe Sadeghi",
        "date": "Oct 23, 2024",
        "read_time": "1 min read",
        "image": "/static/blog1.jpg",
        "excerpt": "Welcome to Ela Arts! Hello, I'm Elahe. I'd love to share a bit about myself and the inspiration behind Ela Arts...",
        "content": """
            Welcome to Ela Arts!
            Hello, I'm Elahe. I'd love to share a bit about myself and the inspiration behind Ela Arts.

            As far back as I can remember, I've always been passionate about painting and art. However, I decided to
            pursue a career in software. After graduating and working as a software developer, my life changed when my
            son was born. Having lived in Malaysia, the Netherlands, and now the USA, I felt a growing void without art
            in my life. Inspired by my son's love for the pictures in his books, I began writing children's books.
            Including Persian language in my stories made this journey even more fulfilling, especially with my
            husband's support.

            My first book, "Did you know?", has been published, and I'm now working on my second book, "Nowruz". As I
            worked on these books, I realized my dream of creating a space full of delightful gifts that bring joy—from
            books and crafts to special occasion gifts. This website is the culmination of that dream. I hope the items
            here can add a touch of happiness to your life.
        """
    }
]

@app.route("/blog-list")
def blog_list():
    return render_template("blog-list.html", posts=blog_posts)

@app.route("/blog/<slug>")
def blog(slug):
    post = next((p for p in blog_posts if p["slug"] == slug), None)
    return render_template("blog.html", post=post)

@app.route("/blog")
def blog_redirect():
    return render_template("blog-list.html", posts=blog_posts)

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

if __name__ == "__main__":
    app.run(debug=True)
