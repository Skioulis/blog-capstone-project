import requests
from flask import Flask, render_template


app = Flask(__name__)

all_posts_url = "https://api.npoint.io/c790b4d5cab58020d391"
all_posts = requests.get(all_posts_url).json()

@app.route('/')
def home():
    # all_posts_url = "https://api.npoint.io/c790b4d5cab58020d391"
    # all_posts = requests.get(all_posts_url).json()

    return render_template("index.html", posts=all_posts)

@app.route('/blog/<int:id>')
def get_post(id):
    to_post = None
    for post in all_posts:
        if post['id']== id:
            to_post = post

    return render_template("post.html", post=to_post)
if __name__ == "__main__":
    app.run(debug=True)
