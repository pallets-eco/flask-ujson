from __future__ import annotations

import dataclasses
import typing as t
from datetime import date
from datetime import datetime
from datetime import timezone
from uuid import UUID

import ujson
from flask.json.provider import JSONProvider
from flask.sansio.app import App


def _default(o: t.Any) -> t.Any:
    if isinstance(o, datetime):
        if o.tzinfo is None:
            o = o.replace(tzinfo=timezone.utc)

        return o.isoformat()

    if isinstance(o, date):
        return o.isoformat()

    if isinstance(o, UUID):
        return str(o)

    if dataclasses.is_dataclass(o):
        return dataclasses.asdict(o)

    if hasattr(o, "__html__"):
        return str(o.__html__())

    raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")


class UjsonProvider(JSONProvider):
    """A :class:`~flask.json.provider.JSONProvider` that uses the fast
    `ujson <https://github.com/ultrajson/ultrajson>`__ library.
    """

    dump_args: dict[str, t.Any] = {
        "ensure_ascii": False,
        "encode_html_chars": True,
        "default": _default,
    }
    """Default keyword arguments passed to ``ujson.dumps``."""

    def __init__(self, app: App) -> None:
        super().__init__(app)
        self.dump_args = self.dump_args.copy()

    def dumps(
        self,
        obj: t.Any,
        **kwargs: t.Any,
    ) -> str:
        """Serialize data as JSON.

        :param obj: The data to serialize.
        :param kwargs: Arguments passed to ``ujson.dumps``. Overrides defaults
            set by :attr:`dump_args`.
        """
        return ujson.dumps(obj, **self.dump_args, **kwargs)

    def loads(self, s: str | bytes, **kwargs: t.Any) -> t.Any:
        """Deserialize data as JSON.

        :param s: Text or UTF-8 bytes.
        :param kwargs: All keyword arguments are silently ignored.
        """
        return ujson.loads(s)
