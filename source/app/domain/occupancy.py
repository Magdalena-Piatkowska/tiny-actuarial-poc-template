import logging

from pydantic import BaseModel, NonNegativeFloat
from app.helpers import get_mapped_dtos_from_csv

logger = logging.getLogger(__name__)


class UnknownOccupancy(Exception):
    pass


class OccupancyDTO(BaseModel):
    name: str
    rate: NonNegativeFloat = 0.0


OCCUPANCY_FILE_PATH = "app/domain/occupancy_rates.csv"


def get_occupancy_map() -> dict:
    return get_mapped_dtos_from_csv(
        file_path=OCCUPANCY_FILE_PATH, dto_class=OccupancyDTO, map_key="name"
    )


def get_occupancy(name: str, occupancy_map: dict) -> OccupancyDTO:
    occupancy = occupancy_map.get(name, None)
    if not occupancy:
        raise UnknownOccupancy
    return occupancy
