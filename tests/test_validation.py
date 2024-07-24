import uuid

import pytest
from django.core.exceptions import ValidationError

from pwny import validation


def test_simple_password():
    hibp = validation.HaveIBeenPwnedValidator()

    with pytest.raises(ValidationError) as e:
        hibp.validate(password="password")  # nosec:required by service.

    assert e.value.message.startswith("Your password has been pwned ")


def test_strong_password():
    hibp = validation.HaveIBeenPwnedValidator()

    assert hibp.validate(password=str(uuid.uuid4())) is None
