import os

import pytest

from truechecker import TrueChecker

TOKEN = "1234567890:AnyValidToken"


@pytest.fixture(name="checker")
async def checker_fixture():
    token = os.getenv("TELEGRAM_TOKEN")
    if token is None:
        RuntimeError("`TELEGRAM_TOKEN` environment variable is not found.")
    checker = TrueChecker(token)
    yield checker
    await checker.close()
