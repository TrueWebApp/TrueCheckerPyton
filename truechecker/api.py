import io
from pathlib import Path
from typing import Optional, Union

from .base import BaseClient
from .const import HTTPMethods

API_HOST = "https://checker.trueweb.app/api"


class TrueChecker(BaseClient):
    API_VERSION = "1.1.0"

    def __init__(self, api_host: Optional[str] = None):
        super().__init__()
        self._api_host = api_host or API_HOST

    async def check_profile(
            self,
            bot_token: str,
            file: Union[str, Path, io.IOBase],
            delay: Optional[float] = None,
    ) -> dict:
        """ Bot check request. """
        method = HTTPMethods.PUT
        url = f"{self._api_host}/profile/{bot_token}"

        # prepare params
        params = {}
        if delay is not None:
            params["delay"] = delay
        form = self._prepare_form(file)

        return await self._make_request(method, url, params=params, data=form)

    async def get_profile(self, username: str):
        """ Returns checked bot profile on success. """
        method = HTTPMethods.GET
        url = f"{self._api_host}/profile/{username}"
        return await self._make_request(method, url)

    async def get_job_status(self, job_id):
        """ Returns current job status. """
        method = HTTPMethods.GET
        url = f"{self._api_host}/job/{job_id}"
        return await self._make_request(method, url)

    async def cancel_job(self, job_id):
        """ Cancel running Job. """
        method = HTTPMethods.DELETE
        url = f"{self._api_host}/job/{job_id}"
        return await self._make_request(method, url)
