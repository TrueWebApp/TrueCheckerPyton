import pytest

from truechecker import TrueChecker

pytestmark = pytest.mark.asyncio


class TestBaseClient:
    async def test_checker_double_close(self, checker: TrueChecker):
        checker._get_session()
        await checker.close()
        await checker.close()
        assert checker._session.closed

    async def test_no_session_close(self, checker: TrueChecker):
        checker._session = None
        await checker.close()
