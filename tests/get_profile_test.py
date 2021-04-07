import pytest

from truechecker import TrueChecker
from truechecker.models import Profile

pytestmark = pytest.mark.asyncio


class TestGetProfile:
    async def test_get_profile_success(self, checker: TrueChecker, username: str):
        profile = await checker.get_profile(username)
        print(f"Result: {profile}")
        assert isinstance(profile, Profile)
