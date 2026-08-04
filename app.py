import os
from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

import json

app = Flask(__name__)
load_dotenv()
with open("static/data/projects.json", "r", encoding="utf-8") as f:
    projects = json.load(f)

with open("static/data/blogs.json", "r", encoding="utf-8") as f:
    blogs = json.load(f)

with open("static/data/shop-categories.json", "r", encoding="utf-8") as f:
    shop_categories = json.load(f)

with open("static/data/products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

with open("static/data/art_sections.json", "r", encoding="utf-8") as f:
    art_sections = json.load(f)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/portfolio")
def portfolio():
    return render_template("profile.html")


@app.route("/portfolio-tech")
def portfolio_tech():
    return render_template("portfolio-tech.html")


@app.route("/portfolio-art")
def portfolio_art():
    return render_template("portfolio-art.html", categories=art_sections)


@app.route("/portfolio-art/<slug>")
def portfolio_art_sections(slug):
    # Find the matching item inside art_sections
    item = None
    for section in art_sections.values():
        for entry in section:
            if entry.get("slug") == slug:
                item = entry
                break

    # If not found → show coming soon
    if not item:
        return render_template("coming-soon.html")

    # Render a template based on slug
    template_name = f"{slug}.html"

    return render_template(template_name, item=item, categories=art_sections)


@app.route("/portfolio-art/<group>/<slug>")
def project_page(group, slug):
    if group not in projects:
        return render_template("coming-soon.html")

    group_projects = projects[group]

    if slug not in group_projects:
        return render_template("coming-soon.html")

    item = group_projects[slug]

    # 🔹 اگر کلکسیون است → صفحه‌ی collection.html
    if "items" in item:
        children = [
            {**group_projects[child], "slug": child, "group": group}
            for child in item["items"]
        ]

        return render_template(
            "collection.html",
            collection=item,
            children=children,
            group=group
        )

    # 🔹 اگر پروژه تکی است → باید ببینیم عضو کدام کلکسیون است
    parent_collection = None
    for key, value in group_projects.items():
        if "items" in value and slug in value["items"]:
            parent_collection = value
            break

    # 🔹 اگر عضو کلکسیون است → prev/next فقط از همان کلکسیون
    if parent_collection:
        slugs = parent_collection["items"]
    else:
        slugs = list(group_projects.keys())

    idx = slugs.index(slug)
    prev_slug = slugs[idx - 1] if idx > 0 else None
    next_slug = slugs[idx + 1] if idx < len(slugs) - 1 else None

    return render_template(
        "project.html",
        project=item,
        prev_slug=prev_slug,
        next_slug=next_slug,
        group=group
    )


@app.route("/shop")
def shop():
    return render_template("shop.html", categories=shop_categories)


@app.route("/shop/<slug>")
def shop_category(slug):
    category = next((c for c in shop_categories if c["slug"] == slug), None)
    if not category:
        return "Category not found", 404

    category_products = products.get(slug, [])

    return render_template("shop-category.html",
                           category=category,
                           products=category_products)


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
