import pytest
import os

from app.domain.rated_property import PropertyDTO, get_rated_properties
from app.helpers import get_dtos_from_csv


@pytest.fixture
def sample_properties():
    root_dir = os.path.dirname(os.path.realpath("__file__"))
    file_path = os.path.join(root_dir, "tests/sample_property.csv")

    properties_generator = get_dtos_from_csv(file_path=file_path, dto_class=PropertyDTO)

    return [property_ for property_ in properties_generator]


def test_get_rated_properties(sample_properties):

    rated_properties = get_rated_properties(properties=sample_properties)
    assert rated_properties[0].model_loss_cost_fgu == 10000.0
    assert rated_properties[1].model_loss_cost_fgu == 20000.0
