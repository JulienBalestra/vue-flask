import time

import os

from app import monitoring
from flask import Flask, jsonify
from flask import render_template
from werkzeug.contrib.cache import FileSystemCache

app = application = Flask("VueFlask")
monitoring.monitor_flask(app)
cache = FileSystemCache(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache"))


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/one")
def one():
    o = cache.get("one")
    if not o:
        o = {"one": [k for k in range(10)]}
        cache.set("one", o, timeout=30)
    return jsonify(o)


@app.route("/api/two")
def two():
    return jsonify({
        "two": [k for k in range(10, 20)]
    })


@app.route("/healthz")
def healthz():
    return jsonify({
        "flask": True,
        "global": True
    })


@app.route("/api/ts")
def ts():
    return jsonify({
        "now": time.time()
    })


if __name__ == '__main__':
    app.run(debug=True)
