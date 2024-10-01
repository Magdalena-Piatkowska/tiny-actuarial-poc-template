import logging
from typing import List

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from app.domain.rated_property import (
    PropertyDTO,
    RatedPropertyDTO,
    get_rated_properties,
)


logger = logging.getLogger(__name__)

root_prefix = f""

app = FastAPI(
    title="Tiny Actuarial PoC Template",
    description="Tiny Actuarial PoC Template",
    version="0.0.1",
    root_path=root_prefix,
)


@app.get("/")
async def version():
    return {"message": "Tiny Actuarial PoC Template"}


@app.get("/healthcheck", include_in_schema=True)
def healthcheck() -> JSONResponse:
    return JSONResponse(
        content={"status_message": "OK"},
        status_code=status.HTTP_200_OK,
    )


@app.post("/property-rates")
def get_property_rates(obj_in_list: List[PropertyDTO]) -> List[RatedPropertyDTO]:
    try:
        rated_properties = get_rated_properties(properties=obj_in_list)
        return rated_properties
    except Exception as err:
        logger.error(str(err))
        raise HTTPException(status_code=500, detail=str(err))
