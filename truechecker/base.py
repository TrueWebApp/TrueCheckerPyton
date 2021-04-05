import io
import os
from pathlib import Path
from typing import Optional, Union

from aiohttp import ClientSession, FormData
from aiohttp.typedefs import StrOrURL


class BaseClient:
    def __init__(self):
        self._session: Optional[ClientSession] = None

    def _get_session(self):
        if isinstance(self._session, ClientSession) and not self._session.closed:
            return self._session

        self._session = ClientSession()
        return self._session

    async def _make_request(self, method: str, url: StrOrURL, **kwargs):
        session = self._get_session()
        return await session.request(method, url, **kwargs)

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
