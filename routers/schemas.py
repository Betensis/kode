from pydantic import BaseModel


class TrainStation(BaseModel):
    id: int
    station: str
    line: int
    adm_area: str
    district: str
    status: str

    class Config:
        orm_mode = True


class SearchTrainStation(BaseModel):
    field: str
    value: str
