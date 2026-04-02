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
        "title": "From Life to Art: The Story Behind Ela Arts",
        "author": "Elahe Sadeghi",
        "date": "Oct 23, 2024",
        "read_time": "1 min read",
        "image": "/static/blog1.jpg",
        "excerpt": """
            Welcome to Ela Arts — and welcome to my very first blog post!
            I’m Elahe, and I’m so happy you’re here...
                        """,
        "content": """
            <p>I’m Elahe, and I’m so happy you’re here.</p>
    
            <p>I wanted my first post to be a little window into the heart of Ela Arts—where it all began, what inspired it, and why this space means so much to me.</p>
    
            <p>Art has been a part of my life for as long as I can remember. Even though I chose a career in software development, the love for painting and creativity never really left me. Life took me from Malaysia to the Netherlands and eventually to the USA, and with every move, that quiet longing for art grew stronger.</p>
    
            <p>Everything changed when my son was born. Watching him fall in love with the pictures in his books sparked something deep inside me. I began writing children’s stories—this time weaving Persian language and culture into them. With my husband’s support, my first book, “Did You Know?”, was published, and I’m now joyfully working on my second book, “Nowruz.” As I wrote, painted, and created, a dream slowly took shape: a warm, joyful space filled with books, crafts, and thoughtful gifts—little treasures that bring happiness to everyday life.</p>
    
            <p>Ela Arts is the home of that dream. Through this blog, I hope to share pieces of my journey—behind-the-scenes moments, creative inspiration, cultural stories, and the magic that goes into every item I create.</p>
    
            <p>Thank you for being here at the very beginning. I can’t wait to grow this space with you.</p>
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
