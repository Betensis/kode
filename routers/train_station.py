from utils.log import logging_query
from db.exceptions import FieldDoesNotExist
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from peewee import DoesNotExist, IntegrityError

from db import services
from . import schemas


api_prefix = "/api/data"

router = APIRouter(prefix=api_prefix)


@router.get("/{id}")
def get_train_station(id: int):
    train_station = services.get_train_station(id)
    if train_station is None:
        error = HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        logging_query(
            message=f"{id=}",
            error={"detail": error.detail},
            endpoint=api_prefix + "/{id}",
        )
        raise error
    logging_query(
        message=f"{id=}",
        endpoint=api_prefix + "/{id}",
    )
    return schemas.TrainStation.from_orm(train_station)


@router.post("/add")
def set_train_station(train_station: schemas.TrainStation):
    try:
        train_station = schemas.TrainStation.from_orm(
            services.create_train_station(**train_station.dict())
        )
        logging_query(
            message=train_station.json(),
            endpoint=api_prefix + "/add",
        )
        return train_station
    except IntegrityError:
        error = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The train station with id={train_station.id} already exists",
        )
        logging_query(
            message=train_station.json(),
            error={
                "detail": error.detail,
            },
            endpoint=api_prefix + "/add",
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error.detail,
        )


@router.delete("/{id}")
def delete_train_station(id: int):
    try:
        services.delete_train_station(id)
        logging_query(
            message=f"{id=}",
            endpoint=api_prefix + "/{id}",
        )
    except DoesNotExist:
        error = HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        logging_query(
            message=f"{id=}",
            error=error.detail,
            endpoint=api_prefix + "/{id}",
        )
        raise error


@router.get("/list/{page}/{limit}")
def get_train_stations(page: int, limit: int):
    logging_query(
        message=f"{page=}|{limit=}",
        endpoint=api_prefix + "/list/{page}/{limit}",
    )
    return {
        "data": [
            schemas.TrainStation.from_orm(record)
            for record in services.get_train_stations(page, limit)
        ]
    }


@router.post("/search")
def search_train_station(search: schemas.SearchTrainStation):
    try:
        result = {
            "data": [
                schemas.TrainStation.from_orm(record)
                for record in services.search_train_station(**search.dict())
            ]
        }
        logging_query(
            message=search.json(),
            endpoint=api_prefix + "/search",
        )
        return result
    except FieldDoesNotExist:
        error = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid field name",
        )
        logging_query(
            message=search.json(),
            error={"detail": error.detail},
            endpoint=api_prefix + "/search",
        )
        raise error
