import pytest

from truechecker import TrueChecker
from truechecker.models import CheckJob

pytestmark = pytest.mark.asyncio


class TestCancelJob:
    async def test_cancel_job(self, checker: TrueChecker, file_path: str):
        # start a new job
        job = await checker.check_profile(file=file_path, delay=1)
        assert isinstance(job, CheckJob)

        # cancel the same job
        cancelled_job = await checker.cancel_job(job.id)
        print(f"Result: {cancelled_job}")
        assert isinstance(cancelled_job, CheckJob)
