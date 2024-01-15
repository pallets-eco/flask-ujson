# flask-ujson

A [Flask][]/[Quart][] {class}`~.flask.json.provider.JSONProvider` using the fast
[ujson][] library. Using this provider will significantly speed up reading JSON
data in requests and generating JSON responses.

[Flask]: https://flask.palletsprojects.com
[Quart]: https://quart.palletsprojects.com
[ujson]: https://github.com/ultrajson/ultrajson

## Usage

```python
from flask import Flask
from flask_ujson import UjsonProvider

app = Flask(__name__)
json_provider = UjsonProvider(app)
app.json = json_provider
```

## Dump Arguments

Ujson takes a number of options to control the behavior of `dumps`. Many of
these mirror the default {func}`json.dumps` arguments, and a few others are
described in the ujson docs.

Flask-ujson sets the following defaults:

- `ensure_ascii=False`
- `encode_html_chars=True`
- `default` converts the same types as Flask's default provider. However, it
  uses ISO 8601 format for `datetime` and `date`.

## Complex Data

It's possible to set a `default` function in {attr}`~.UjsonProvider.dump_args`
to handle any data. However, we recommend using a dedicated object serialization
library to first convert complex data to JSON types, before serializing that to
JSON. This gives you full control over how your data is represented, as well as
the ability to deserialize data in requests. Some such libraries include
[cattrs][], [Marshmallow][], and [Pydantic][].

[cattrs]: https://catt.rs
[marshmallow]: https://marshmallow.readthedocs.io
[Pydantic]: https://docs.pydantic.dev

```{toctree}
:hidden:

api
changes
license
```
