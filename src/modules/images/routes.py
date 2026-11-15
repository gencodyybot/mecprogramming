from fastapi import APIRouter, Query

from .wikimedia import get_photos

router = APIRouter()


@router.get("/images")
def get_images(
    latitude: float,
    longitude: float,
    radius: int = Query(default=10000, ge=1, le=10000),
    limit: int = Query(default=3, ge=1, le=50),
):
    return get_photos(latitude, longitude, radius=radius, limit=limit)
