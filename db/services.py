from typing import Any, Optional

from peewee import DoesNotExist

from .models import TrainStation
from .exceptions import FieldDoesNotExist


def get_train_station(id: int) -> Optional[TrainStation]:
    return TrainStation.get_or_none(TrainStation.id == id)


def create_train_station(**kwargs) -> dict[str, Any]:
    return TrainStation.create(**kwargs)


def delete_train_station(id: int) -> None:
    train_station = get_train_station(id)
    if train_station is None:
        raise DoesNotExist
    train_station.delete().where(TrainStation.id == id).execute()


def get_train_stations(page: int, limit: int):
    return (
        TrainStation.select()
        .order_by(TrainStation.station)
        .paginate(page, limit)
        .execute()
    )


def search_train_station(field: str, value: Any):
    try:
        train_station_field = getattr(TrainStation, field)
        return (
            TrainStation.select()
            .where(train_station_field == value)
            .order_by(TrainStation.id)
            .execute()
        )
    except AttributeError:
        raise FieldDoesNotExist
