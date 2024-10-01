from app.domain.occupancy import get_occupancy, get_occupancy_map, UnknownOccupancy
import pytest


def test_get_occupancy():
    occupancy_map = get_occupancy_map()
    agriculture = get_occupancy(name="AGRICULTURE", occupancy_map=occupancy_map)
    assert agriculture
    assert agriculture.rate == 0.0025063548880476


def test_get_occupancy_raises_error():
    occupancy_map = get_occupancy_map()
    with pytest.raises(UnknownOccupancy) as err:
        soviet_block_of_flats = get_occupancy(
            name="SOVIET BLOCK OF FLATS", occupancy_map=occupancy_map
        )
