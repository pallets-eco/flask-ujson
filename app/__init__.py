from flask import Flask, jsonify

from flask_ujson import UJSON

ultra_json = UJSON()


def create_app():
    app = Flask(__name__)
    ultra_json.init_app(app)  # Replaces the standard JSON encoder with UltraJSON

    @app.route("/")
    def index():
        """
        Outputs a JSON response using UltraJSON library

        https://github.com/ultrajson/ultrajson
        """
        return {"hello": "world"}

    @app.route("/jsonify")
    def using_jsonify():
        """
        jsonify is not really needed for most cases, but here's an example.
        """
        return jsonify({"hello": "world"})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
