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
