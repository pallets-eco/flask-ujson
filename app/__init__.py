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
