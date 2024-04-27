from fastapi import APIRouter, Depends, HTTPException
from .strategy import CarRoute, BikeRoute, RouteStrategy, MotorcycleRoute
from enum import Enum


class Vehicle(Enum):
    CAR = "car"
    BIKE = "bike"
    MOTORCYCLE = "motorcycle"


def get_strategy(vehicle: Vehicle) -> RouteStrategy:
    if vehicle == Vehicle.CAR:
        return CarRoute()
    elif vehicle == Vehicle.BIKE:
        return BikeRoute()
    elif vehicle == Vehicle.MOTORCYCLE:
        return MotorcycleRoute()
    else:
        raise HTTPException(status_code=400, detail="Invalid vehicle")


router = APIRouter()


@router.get("/best_route")
def best_route(origin: int, destination: int, vehicle: RouteStrategy = Depends(get_strategy)) -> dict:
    return vehicle.get_best_route(origin=origin, destination=destination)


@router.get("/cost")
def cost(origin: int, destination: int, vehicle: RouteStrategy = Depends(get_strategy)) -> float:
    return vehicle.get_cost(origin=origin, destination=destination)


@router.get("/time")
def time(origin: int, destination: int, vehicle: RouteStrategy = Depends(get_strategy)) -> float:
    return vehicle.get_time(origin=origin, destination=destination)
