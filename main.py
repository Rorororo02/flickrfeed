from flask import Flask, render_template
from feedparser import parse as feedparse

app = Flask(__name__)

@app.route('/')
def index():
    feed = feedparse('https://api.flickr.com/services/feeds/photos_public.gne')

    return render_template('index.html', feed=feed)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')