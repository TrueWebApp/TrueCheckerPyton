from io import StringIO
from pathlib import Path

import pytest

from truechecker import TrueChecker
from truechecker.exceptions import BadState, BadRequest, Unauthorized
from truechecker.models import CheckJob

pytestmark = pytest.mark.asyncio


class TestCheckProfile:
    async def test_success(self, checker: TrueChecker, file_path: str):
        job = await checker.check_profile(file=file_path, delay=0.5)
        print(f"Result: {job}")
        assert isinstance(job, CheckJob)
        await checker.cancel_job(job.id)

    async def test_bad_file(self, checker: TrueChecker):
        with pytest.raises(TypeError):
            await checker.check_profile(file=None)  # noqa

    async def test_path_object(self, checker: TrueChecker, file_path: str):
        path = Path(file_path)
        job = await checker.check_profile(file=path)
        print(f"Result: {job}")
        assert isinstance(job, CheckJob)
        await checker.cancel_job(job.id)

    async def test_file_io(self, checker: TrueChecker, file_path: str):
        file = open(file_path, "r")
        lines = file.readlines()
        file_io = StringIO("".join(lines))
        job = await checker.check_profile(file=file_io)
        print(f"Result: {job}")
        assert isinstance(job, CheckJob)
        await checker.cancel_job(job.id)

    async def test_already_running(self, checker: TrueChecker, file_path: str):
        job = await checker.check_profile(file=file_path, delay=1)
        with pytest.raises(BadState):
            result = await checker.check_profile(file=file_path)
            print(f"Result: {result}")
        await checker.cancel_job(job.id)

    async def test_bad_token(self, file_path: str):
        checker = TrueChecker(None)  # noqa
        with pytest.raises(BadRequest):
            result = await checker.check_profile(file=file_path)
            print(f"Result: {result}")

    async def test_invalid_token(self, file_path: str):
        checker = TrueChecker("1234567890:qwertyuiop")  # noqa
        with pytest.raises(Unauthorized):
            result = await checker.check_profile(file=file_path)
            print(f"Result: {result}")
