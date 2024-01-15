# flask-ujson

A [Flask][]/[Quart][] JSON provider using the fast [ujson][] library. Using
this provider will significantly speed up reading JSON data in requests and
generating JSON responses.

[flask]: https://flask.palletsprojects.com
[quart]: https://quart.palletsprojects.com
[ujson]: https://github.com/ultrajson/ultrajson

## Example

```python
from flask import Flask
from flask_ujson import UjsonProvider

app = Flask(__name__)
app.json = UjsonProvider(app)
```
