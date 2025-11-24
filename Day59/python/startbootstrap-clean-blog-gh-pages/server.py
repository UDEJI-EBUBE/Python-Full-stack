import requests
from flask import Flask, render_template

API_ENDPOINT = "https://api.npoint.io/674f5423f73deab1e9a7"
response = requests.get(API_ENDPOINT)
blog = response.json()
print(blog)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", blog=blog)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:num>")
def get_blog(num):
    print(num)
    requested_post = None
    for blogs in blog:
        if blogs["id"]==num:
            requested_post = blogs
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)