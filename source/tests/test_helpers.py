from app.helpers import get_mapped_dtos_from_csv
import os
from app.domain.rated_property import PropertyDTO


def test_get_mapped_dtos_from_csv():
    root_dir = os.path.dirname(os.path.realpath("__file__"))
    file_path = os.path.join(root_dir, "tests/sample_property.csv")

    property_map = get_mapped_dtos_from_csv(
        file_path=file_path, dto_class=PropertyDTO, map_key="street_name"
    )

    assert isinstance(property_map, dict)
    assert len(list(property_map.keys())) == 2
