import os

import pytest

from truechecker import TrueChecker

FILE_PATH = "tests/dataset/users.csv"


@pytest.fixture(name="token")
def token_fixture():
    token = os.getenv("CHECKER_TOKEN")
    if token is None:
        RuntimeError("`CHECKER_TOKEN` environment variable is not found.")
    return token


@pytest.fixture(name="username")
def username_fixture():
    username = os.getenv("CHECKER_USERNAME")
    if username is None:
        RuntimeError("`CHECKER_USERNAME` environment variable is not found.")
    return username


@pytest.fixture(name="job_id")
def job_id_fixture():
    job_id = os.getenv("CHECKER_JOB_ID")
    if job_id is None:
        RuntimeError("`CHECKER_JOB_ID` environment variable is not found.")
    return job_id


@pytest.fixture(name="file_path")
def file_path_fixture():
    file_path = os.getenv("CHECKER_FILE_PATH", FILE_PATH)
    return file_path


@pytest.fixture(name="checker")
async def checker_fixture(token):
    checker = TrueChecker(token)
    yield checker
    await checker.close()
