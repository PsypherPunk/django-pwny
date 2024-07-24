# `django-pwny`

*Have I Been Pwned?* password validator. Inspired by a
[blog post](https://www.thedatashed.co.uk/2019/02/07/django-pwny/) on
the subject.

## Quickstart

Install `django-pwny`:

```sh
pip install django-pwny
```

Add it to your `AUTH_PASSWORD_VALIDATORS`:

``` python
AUTH_PASSWORD_VALIDATORS = [
    ...
    "pwny.validation.HaveIBeenPwnedValidator",
    ...
]
```

## Running Tests

`django-pwny` makes use of
[`pytest-dev/pytest-django`](https://github.com/pytest-dev/pytest-django) to
run tests via [`pytest`](https://docs.pytest.org/).

Assuming dependencies are installed, simply run:

```sh
pytest
```

## Credits

Tools used in rendering this package:

- [Cookiecutter](https://github.com/audreyr/cookiecutter)
- [cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage)
