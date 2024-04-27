from fastapi import APIRouter, Depends, HTTPException
from .strategy import CarRoute, BikeRoute, RouteStrategy, MotorcycleRoute
from enum import Enum
from datetime import datetime

class Vehicle(Enum):
    CAR = "car"
    BIKE = "bike"
    MOTORCYCLE = "motorcycle"

class DiscountType(Enum):
    CHILD = "child"
    MILITARY = "military"
    WEEKDAY = "weekday"
    NORMAL = "normal"

def get_strategy(vehicle: Vehicle, discount_type: DiscountType) -> RouteStrategy:
    if vehicle == Vehicle.CAR:
        return CarRoute()
    elif vehicle == Vehicle.BIKE:
        return BikeRoute()
    elif vehicle == Vehicle.MOTORCYCLE:
        return MotorcycleRoute()
    else:
        raise HTTPException(status_code=400, detail="Invalid vehicle")

def get_discount_type(age: int, is_military: bool, date: datetime) -> DiscountType:
    if age < 5:
        return DiscountType.CHILD
    elif is_military:
        return DiscountType.MILITARY
    elif date.weekday() < 5:  # Monday to Friday
        return DiscountType.WEEKDAY
    else:
        return DiscountType.NORMAL

router = APIRouter()

@router.get("/best_route")
def best_route(origin: int, destination: int, vehicle: Vehicle = Vehicle.CAR, discount_type: DiscountType = DiscountType.NORMAL,
               route_strategy: RouteStrategy = Depends(get_strategy)) -> dict:
    return route_strategy.get_best_route(origin=origin, destination=destination)

@router.get("/cost")
def cost(origin: int, destination: int, vehicle: Vehicle = Vehicle.CAR, discount_type: DiscountType = DiscountType.NORMAL,
         route_strategy: RouteStrategy = Depends(get_strategy)) -> float:
    return route_strategy.get_cost(origin=origin, destination=destination)

@router.get("/time")
def time(origin: int, destination: int, vehicle: Vehicle = Vehicle.CAR, discount_type: DiscountType = DiscountType.NORMAL,
         route_strategy: RouteStrategy = Depends(get_strategy)) -> float:
    return route_strategy.get_time(origin=origin, destination=destination)