from fastapi import APIRouter
from .client import fetch_raw_stations
from .filter import clean_stations

router = APIRouter()

@router.get("/stations")
def get_stations(country: str = "CA", tag: str = "music"):
    raw = fetch_raw_stations(country, tag=tag)
    clean = clean_stations(raw)
    return {"country": country.upper(), "count": len(clean), "stations": clean}