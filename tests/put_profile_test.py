import asyncio
from io import StringIO
from pathlib import Path

import pytest

from truechecker import TrueChecker
from truechecker.exceptions import BadRequest, BadState, Unauthorized
from truechecker.models import CheckJob

pytestmark = pytest.mark.asyncio


class TestCheckProfile:
    async def test_success(self, checker: TrueChecker, file_path: str):
        job = await checker.check_profile(file=file_path, delay=1)
        print(f"Result: {job}")
        assert isinstance(job, CheckJob)
        await checker.cancel_job(job.id)
        await asyncio.sleep(10)

    async def test_bad_file(self, checker: TrueChecker):
        with pytest.raises(TypeError):
            await checker.check_profile(file=None)  # noqa

    async def test_path_object(self, checker: TrueChecker, file_path: str):
        path = Path(file_path)
        job = await checker.check_profile(file=path, delay=1)
        print(f"Result: {job}")
        assert isinstance(job, CheckJob)
        await checker.cancel_job(job.id)
        await asyncio.sleep(10)

    async def test_file_io(self, checker: TrueChecker, file_path: str):
        file = open(file_path, "r")
        lines = file.readlines()
        file_io = StringIO("".join(lines))
        job = await checker.check_profile(file=file_io, delay=1)
        print(f"Result: {job}")
        assert isinstance(job, CheckJob)
        await checker.cancel_job(job.id)
        await asyncio.sleep(10)

    async def test_already_running(self, checker: TrueChecker, file_path: str):
        job = await checker.check_profile(file=file_path, delay=1)
        with pytest.raises(BadState):
            await checker.check_profile(file=file_path)
        await checker.cancel_job(job.id)
        await asyncio.sleep(10)

    async def test_bad_token(self, file_path: str):
        checker = TrueChecker(None)  # noqa
        with pytest.raises(BadRequest):
            await checker.check_profile(file=file_path)

    async def test_invalid_token(self, file_path: str):
        checker = TrueChecker("1234567890:qwertyuiop")  # noqa
        with pytest.raises(Unauthorized):
            await checker.check_profile(file=file_path)
