import peewee
from peewee import CharField, IntegerField

from .base import db


class TrainStation(peewee.Model):
    id = IntegerField(
        unique=True,
        primary_key=False,
    )
    station = CharField()
    line = IntegerField()
    adm_area = CharField()
    district = CharField()
    status = CharField()

    class Meta:
        database = db
        primary_key = False
