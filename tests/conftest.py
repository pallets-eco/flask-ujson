from __future__ import annotations

import pytest
from flask import Flask
from flask.testing import FlaskClient

from flask_ujson import UjsonProvider


@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    app.json = UjsonProvider(app)
    return app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()
