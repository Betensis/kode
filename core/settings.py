from pathlib import Path
from os import environ
from distutils.util import strtobool

from dotenv import load_dotenv, find_dotenv

if dotenv_path := find_dotenv():
    load_dotenv(dotenv_path)

DB_PATH = Path(".").joinpath("sqlite.db")
CSV_FILE_PATH = (
    Path(environ.get("CSV_FILE_PATH")) if environ.get("CSV_FILE_PATH") else None
)

PROJECT_NAME = "Train station service"
DEBUG = strtobool(environ.get("DEBUG", "False"))
RELOAD_APP = strtobool(environ.get("RELOAD_APP", "False"))
