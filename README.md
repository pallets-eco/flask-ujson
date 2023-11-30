# flask-ujson

[![PyPI version](https://badge.fury.io/py/flask-ujson.svg)](https://badge.fury.io/py/flask-ujson)
[![License](https://img.shields.io/badge/license-LGPL_v2-red.svg)](https://raw.githubusercontent.com/CheeseCake87/flask-ujson/master/LICENSE)

Flask with UltraJSON.

[https://github.com/ultrajson/ultrajson](https://github.com/ultrajson/ultrajson)

```python
from flask import Flask

from flask_ujson import UJSON

ultra_json = UJSON()


def create_app():
    app = Flask(__name__)
    ultra_json.init_app(app)

    @app.route("/")
    def index():
        """
        Outputs a JSON response using UltraJSON library
        https://github.com/ultrajson/ultrajson
        """
        return {"hello": "world"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

```