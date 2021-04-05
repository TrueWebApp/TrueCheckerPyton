from pathlib import Path

import pytest

from truechecker import TrueChecker

pytestmark = pytest.mark.asyncio

FILE_STR_PATH = "tests/dataset/users.csv"
file_path = Path(FILE_STR_PATH)


class TestCheckProfile:
    async def test_check_profile_success(self, checker: TrueChecker):
        result = await checker.check_profile(file=file_path)
        print(f"Result: {result}")
        assert isinstance(result, dict)

        job_id = result.get("id")
        assert job_id is not None
