## Version 2.0.0

Released 2024-01-14

- Simplify how the library is used and configured.
- The `UJSON` extension class is removed. Use `app.json = UjsonProvider(app)`.
- `UjsonProvider` has a `dump_args` attribute, a dict of default keyword
  arguments to `ujson.dumps`. Keyword arguments to `dumps` overrides these.
- The provider does not have `sort_keys` or `compact` as arguments or
  attributes. Use `dump_args` to set those arguments (and others) instead.
- The `__version__` attribute is removed. Call `importlib.metadata.version` instead.
- `datetime` and `date` objects use ISO 8601 format.
- Export type annotations.
- Change license to MIT.
- Use PyPI trusted publishing.
- Use `src` directory layout.

## Version 1.0.6

Released 2023-12-01

## Version 1.0.5

Released 2023-12-01

## Version 1.0.4

Released 2023-11-30

## Version 1.0.3

Released 2023-11-30

## Version 1.0.2

Released 2023-11-30

## Version 1.0.1

Released 2023-11-30

## Version 1.0.0

Released 2023-11-30

- Initial release.
