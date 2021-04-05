import pytest

from truechecker import TrueChecker
from truechecker.models import CheckJob

pytestmark = pytest.mark.asyncio


class TestCheckProfile:
    async def test_check_profile_success(self, checker: TrueChecker, file_path: str):
        job = await checker.check_profile(file=file_path, delay=0.5)
        print(f"Result: {job}")
        assert isinstance(job, CheckJob)
