import os
from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

import json

app = Flask(__name__)
load_dotenv()
with open("./data/projects.json", "r") as f:
    projects = json.load(f)

with open("./data/blogs.json", "r", encoding="utf-8") as f:
    blogs = json.load(f)


@app.route("/")
def home():
    return render_template("profile.html")


from flask import render_template


@app.route("/project/<slug>")
def project_page(slug):
    # ❗ Check if slug exists
    if slug not in projects:
        return "Project not found", 404

    # ⭐ Create an ordered list of slugs
    project_slugs = list(projects.keys())

    # ⭐ Find current index
    current_index = project_slugs.index(slug)

    # ⭐ Calculate previous and next
    prev_slug = project_slugs[current_index - 1] if current_index > 0 else None
    next_slug = project_slugs[current_index + 1] if current_index < len(project_slugs) - 1 else None

    # ⭐ Get the project data
    project = projects[slug]

    # ⭐ Send everything to template
    return render_template(
        "project.html",
        project=project,
        prev_slug=prev_slug,
        next_slug=next_slug
    )


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


@app.route("/blog-list")
def blog_list():
    return render_template("blog-list.html", posts=blogs)


@app.route("/blog/<slug>")
def blog(slug):
    post = next((p for p in blogs if p["slug"] == slug), None)

    if not post:
        return "Blog post not found", 404

    return render_template("blog.html", post=post)



@app.route("/blog")
def blog_redirect():
    return render_template("blog-list.html", posts=blogs)


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
