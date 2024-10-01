import logging
from typing import Dict, List

from pydantic import BaseModel, NonNegativeFloat

from app.domain.occupancy import OccupancyDTO, get_occupancy, get_occupancy_map

logger = logging.getLogger(__name__)


class PropertyDTO(BaseModel):
    street_name: str = "122 Leadenhall St"
    country: str = "GB"
    air_occupancy: str = "OFFICES"
    tiv_total: NonNegativeFloat = 0.0


class RatedPropertyDTO(PropertyDTO):
    occupancy_rate: NonNegativeFloat = 0.0
    model_loss_cost_fgu: NonNegativeFloat = 0.0


def get_rated_property(
    property: PropertyDTO, occupancy_map: Dict[str, OccupancyDTO]
) -> RatedPropertyDTO:
    occupancy = get_occupancy(name=property.air_occupancy, occupancy_map=occupancy_map)
    rated_property = RatedPropertyDTO(**property.model_dump())

    rated_property.occupancy_rate = occupancy.rate
    rated_property.model_loss_cost_fgu = rated_property.tiv_total * occupancy.rate

    return rated_property


def get_rated_properties(properties: List[PropertyDTO]) -> List[RatedPropertyDTO]:
    occupancy_map = get_occupancy_map()
    rated_properties: List[RatedPropertyDTO] = []
    for property in properties:
        rated_property = get_rated_property(
            property=property, occupancy_map=occupancy_map
        )
        rated_properties.append(rated_property)
    return rated_properties
