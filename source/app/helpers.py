import csv
import logging
from io import StringIO, TextIOWrapper
from typing import Dict, Generator, List, Optional, Sequence, Type, Union

from pydantic import BaseModel

logger = logging.getLogger(__name__)


def get_dtos_from_csv(
    file_path: str,
    dto_class: Type[BaseModel],
    encoding: str = "utf-8",
) -> Generator[BaseModel, None, None]:
    file_content = open(file_path, mode="r", encoding=encoding)

    with file_content as f:
        reader = csv.reader(f)  # type: ignore
        csv_headers = next(reader)
        dto_attrs = set(dto_class.model_fields.keys())
        f.seek(0)
        dict_reader = csv.DictReader(f)
        assert set(csv_headers).issubset(dto_attrs)
        for row in dict_reader:
            yield dto_class(**row)


def get_mapped_dtos_from_csv(
    file_path,
    dto_class: Type[BaseModel],
    map_key: str,
    encoding: str = "utf-8",
) -> Dict[str, BaseModel]:
    """
    Turns the contents of a CSV file into a dict map,
    where dict keys are lookup values, and dict values are DTOs.
    """
    dtos = get_dtos_from_csv(
        file_path=file_path, dto_class=dto_class, encoding=encoding
    )
    mapped_dtos = dict()

    for dto in dtos:
        if map_key not in dto_class.model_fields.keys():
            err = f"The provided map_key '{str(map_key)}' does not match any of the dto_class attributes: '{str(dto_class.model_fields.keys())}'"
            logger.info(err)
            raise ValueError(err)
        dto_key = getattr(dto, map_key)
        mapped_dtos[dto_key] = dto

    return mapped_dtos
