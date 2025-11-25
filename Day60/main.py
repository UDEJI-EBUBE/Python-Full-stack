import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests
from smtplib import SMTP_SSL

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

load_dotenv()
SMTP= os.getenv("SMTP_ADDRESS")
sender= os.getenv("EMAIL_ADDRESS")
receiver = os.getenv("RECEIVER")
PASSWORD= os.getenv("EMAIL_PASSWORD")

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/contact", methods=["POST", "GET"])
def contact():
    msg_sent = False
    if request.method == "POST":
        message = request.form["message"]
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        with SMTP_SSL(SMTP) as connection:
            connection.login(user=sender, password=PASSWORD)
            connection.sendmail(from_addr=sender, to_addrs=receiver,
                                msg=f"Subject: New Contact Message\n\n"
                                    f"name: {name}\n"
                                    f"Email: {email}\n"
                                    f"Phone: {phone}\n"
                                    f"Message: {message}")
        msg_sent =True
        return render_template("contact.html", msg=msg_sent)
    return render_template("contact.html")




@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
