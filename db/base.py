from peewee import SqliteDatabase

from core.settings import DB_PATH


db = SqliteDatabase(DB_PATH)
