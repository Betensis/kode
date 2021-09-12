from pathlib import Path
import csv

from db.models import TrainStation


def fill_db_from_csv(csv_path: Path):
    with open(csv_path.resolve()) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            TrainStation.get_or_create(
                id=row["ID"],
                station=row["Station"],
                line=row["Line"],
                adm_area=row["AdmArea"],
                district=row["District"],
                status=row["Status"],
            )
