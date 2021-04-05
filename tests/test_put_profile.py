from pathlib import Path

import pytest

from truechecker import TrueChecker

pytestmark = pytest.mark.asyncio

FILE_STR_PATH = "tests/dataset/user_ids.txt"
FILE_PATH = Path("tests/dataset/user_ids.txt")


class TestCheckProfile:
    async def test_check_profile_success(self, checker: TrueChecker):
        result = await checker.check_profile(file=FILE_PATH)
        assert isinstance(result, dict)

        job_id = result.get("id")
        assert job_id is not None
