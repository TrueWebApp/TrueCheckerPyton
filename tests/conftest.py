import pytest

from truechecker import TrueChecker

TOKEN = "1234567890:AnyValidToken"


@pytest.fixture(name="checker")
async def checker_fixture():
    checker = TrueChecker(TOKEN)
    yield checker
    await checker.close()
