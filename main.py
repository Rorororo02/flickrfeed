from flask import abort, Flask, jsonify, render_template, request
from feedparser import parse as feedparse

app = Flask(__name__)

@app.route('/')
def index():
    feed = feedparse('https://api.flickr.com/services/feeds/photos_public.gne')
    return render_template('index.html', feed=feed)

@app.route('/_search/')
def search():
    tags = request.args.get('tags', '')
    feed = feedparse('https://api.flickr.com/services/feeds/photos_public.gne?tags=%s' % tags)

    # render page in case the search is not via ajax
    if not request.is_xhr:
        return render_template('index.html', feed=feed)

    contents = []
    for entry in feed.entries:
        rendered = render_template("entry.html", entry=entry)
        contents.append(rendered)

    return jsonify({'contents': " ".join(contents)})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')