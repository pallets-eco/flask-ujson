# flask-ujson

[![PyPI version](https://badge.fury.io/py/flask-ujson.svg)](https://badge.fury.io/py/flask-ujson)
[![License](https://img.shields.io/badge/license-LGPL_v2-red.svg)](https://raw.githubusercontent.com/CheeseCake87/flask-ujson/master/LICENSE)

`pip install flask-ujson`

Flask with UltraJSON.

[https://github.com/ultrajson/ultrajson](https://github.com/ultrajson/ultrajson)

```python
from flask import Flask, request

from flask_ujson import UJSON

ultra_json = UJSON()


def create_app():
    app = Flask(__name__)
    ultra_json.init_app(app)  # Sets UltraJSON as the default JSON encoder

    @app.route("/")
    def index():
        """
        Outputs a JSON response using UltraJSON library

        https://github.com/ultrajson/ultrajson
        """
        return {
            "timestamp": 1556283673.1523004,
            "task_uuid": "0ed1a1c3-050c-4fb9-9426-a7e72d0acfc7",
            "task_level": [1, 2, 1],
            "action_status": "started",
            "action_type": "main",
            "key": "value",
            "another_key": 123,
            "and_another": ["a", "b"],
        }

    @app.post("/post")
    def accept_json():
        json = request.get_json()
        return json

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

```