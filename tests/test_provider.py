from __future__ import annotations

import typing as t
from dataclasses import dataclass
from datetime import date
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from decimal import Decimal
from uuid import UUID

import pytest
from flask import Flask
from flask import request
from flask.testing import FlaskClient


def test_request_response(app: Flask, client: FlaskClient) -> None:
    @app.post("/")
    def echo() -> t.Any:
        return request.json

    class User:
        def __init__(self, name: str) -> None:
            self.name = name

        def __html__(self) -> str:
            return f"<a>{self.name}</a>"

    @dataclass
    class Roll:
        count: int
        sides: int

    pst = timezone(timedelta(hours=-8), "PST")
    rv = client.post(
        "/",
        json={
            "datetime-naive": datetime(2024, 1, 12, 9, 42),
            "datetime-aware": datetime(2024, 1, 12, 9, 42, tzinfo=pst),
            "date": date(2024, 1, 12),
            "decimal": Decimal("3.14159"),
            "uuid": UUID("d0086ec3-d2f8-4bd9-9602-dae3ffabc0da"),
            "dataclass": Roll(1, 20),
            "html": User("flask"),
        },
    )
    assert rv.json == {
        "datetime-naive": "2024-01-12T09:42:00+00:00",
        "datetime-aware": "2024-01-12T09:42:00-08:00",
        "date": "2024-01-12",
        "decimal": 3.14159,
        "uuid": "d0086ec3-d2f8-4bd9-9602-dae3ffabc0da",
        "dataclass": {"count": 1, "sides": 20},
        "html": "<a>flask</a>",
    }


def test_default_unsupported(app: Flask) -> None:
    with pytest.raises(TypeError):
        app.json.dumps({"a": ...})
