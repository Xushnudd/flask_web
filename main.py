from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def name():
    datas = {
        "section": [
            {
                "image": {
                    "url": url_for("static", filename="imgs/section1.png"),
                    "alt": "https://www.w3schools.com/w3images/woods.jpg"
                },
                "title": "TITLE HEADING",
                "subtitle": "Title description",
                "date": "April 7, 2014",
                "text": "Mauris neque quam, fermentum ut nisl vitae, convallis maximus nisl. Sed mattis nunc id lorem euismod placerat. Vivamus porttitor magna enim, ac accumsan tortor cursus at. Phasellus sed ultricies mi non congue ullam corper. Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla.",
                "button": "read more >>",
                "comments": "0"
            },
            {
                "image": {
                    "url": url_for("static", filename="imgs/section2.png"),
                    "alt": "https://www.w3schools.com/w3images/bridge.jpg"
                },
                "title": "BLOG ENTRY",
                "subtitle": "Title description",
                "date": "April 2, 2014",
                "text": "Mauris neque quam, fermentum ut nisl vitae, convallis maximus nisl. Sed mattis nunc id lorem euismod placerat. Vivamus porttitor magna enim, ac accumsan tortor cursus at. Phasellus sed ultricies mi non congue ullam corper. Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla.",
                "button": "read more >>",
                "comments": "2"
            }
        ],
        "profile": {
            "image": {
                "url": url_for("static", filename="imgs/profile.png"),
                "alt": "https://www.w3schools.com/w3images/avatar_g.jpg"
            },
            "title": "My Name",
            "text": "Just me, myself and I, exploring the universe of uknownment. I have a heart of love and a interest of lorem ipsum and mauris neque quam blog. I want to share my world with you."
        },
        "posts": {
            "title": "Popular Posts",
            "datas": []
        },
        "tags": {
            "title": "Tags",
            "tags": [
                {"name": "Travel", "actual": True},
                {"name": "New York", "actual": False},
                {"name": "London", "actual": False},
                {"name": "IKEA", "actual": False},
                {"name": "NORWAY", "actual": False},
                {"name": "DIY Ideas", "actual": False},
                {"name": "Baby", "actual": False},
                {"name": "Family", "actual": False},
                {"name": "News", "actual": False},
                {"name": "Clothing", "actual": False},
                {"name": "Shopping", "actual": False},
                {"name": "Sports", "actual": False},
                {"name": "Games", "actual": False}
            ]
        },
        "footer": [
            {"name": "previous", "status": "old"},
            {"name": "next", "status": "next"}
        ]
    }
    
    for i in range(1, 5):
        datas["posts"]["datas"].append(
            {
                "img_url": url_for("static", filename=f"imgs/post{i}.png"),
                "img_alt": "Post image",
                "title": "Post title",
                "subtitle": "Subtitle"
            }
        )
    
    return render_template("name.html", datas=datas), 200

if __name__ == "__main__":
    app.run(debug=True)