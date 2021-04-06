import asyncio
import io
import ssl
from pathlib import Path
from typing import Optional, Tuple, Union

import certifi
from aiohttp import ClientSession, FormData, TCPConnector
from aiohttp.typedefs import StrOrURL

from .exceptions import (
    BadRequest,
    BadState,
    TrueCheckerException,
    Unauthorized,
    ValidationError,
)
from .utils import json

EXC_MAPPING = {
    400: BadRequest,
    401: Unauthorized,
    404: BadRequest,
    409: BadState,
    422: ValidationError,
}


class BaseClient:
    def __init__(self):
        self._session: Optional[ClientSession] = None

    def _get_session(self):
        if isinstance(self._session, ClientSession) and not self._session.closed:
            return self._session

        ssl_context = ssl.create_default_context(cafile=certifi.where())
        connector = TCPConnector(ssl=ssl_context)

        self._session = ClientSession(
            connector=connector,
            json_serialize=json.dumps,
        )
        return self._session

    async def _make_request(
        self, method: str, url: StrOrURL, **kwargs
    ) -> Tuple[int, dict]:
        session = self._get_session()
        result = await session.request(method, url, **kwargs)
        status = result.status
        data = await result.json(loads=json.loads)
        if status != 200:
            raise self._process_exception(status, data)
        return status, data

    def _prepare_form(self, file: Union[str, Path, io.IOBase]):
        form = FormData()
        form.add_field("file", self._prepare_file(file))
        return form

    @staticmethod
    def _prepare_file(file: Union[str, Path, io.IOBase]):
        if isinstance(file, str):
            return open(file, "rb")

        if isinstance(file, io.IOBase):
            return file

        if isinstance(file, Path):
            return file.open("rb")

        raise TypeError("Not supported file type.")

    @staticmethod
    def _process_exception(status: int, data: dict) -> TrueCheckerException:
        text = data.get("message") or data.get("detail")
        exc = EXC_MAPPING.get(status, TrueCheckerException)
        return exc(text)

    async def close(self):
        if not isinstance(self._session, ClientSession):
            return

        if self._session.closed:
            return

        await self._session.close()
        await asyncio.sleep(0.25)
