import pytest

from truechecker import TrueChecker
from truechecker.models import CheckJob

pytestmark = pytest.mark.asyncio


class TestGetJobStatus:
    async def test_get_job_status_success(self, checker: TrueChecker, job_id: str):
        job = await checker.get_job_status(job_id)
        print(f"Result: {job}")
        assert isinstance(job, CheckJob)
