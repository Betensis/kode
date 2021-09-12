from fastapi import FastAPI

from core.settings import CSV_FILE_PATH, DEBUG, RELOAD_APP
from db import db
from db.models import TrainStation
from utils.csv import fill_db_from_csv
from routers import train_station


app = FastAPI(debug=DEBUG)


@app.on_event("startup")
def startup():
    db.connect()
    db.create_tables([TrainStation])
    if CSV_FILE_PATH is not None and CSV_FILE_PATH.exists():
        fill_db_from_csv(CSV_FILE_PATH)


@app.on_event("shutdown")
def shutdown():
    if not db.is_closed():
        db.close()


app.include_router(train_station.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=RELOAD_APP)
