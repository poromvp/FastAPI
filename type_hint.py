from typing import Any

text: str = "value"
pert: int = 90
temp: float = 37.5

number: int | float = 12

digits: list [int] = [1,2,3,4,5]

table_5: tuple[int, ...] = (5,10,15)

city_temp: tuple[str, float] = ("City", 20.5)

optional: str | None

shipment: dict[str, str | int] = {
    "id" : 12,
    "content" : "wooden table",
    "status" : "in transit"
}

Shipment: dict[str, Any] = {
    "id" : 12,
    "content" : "wooden table",
    "status" : "in transit"
}

class City:
    def __init__(self, name, location):
        self.name = name
        self.location = location

hanoi = City("Hà Nội", 1244 )
city: tuple[City, float] = (hanoi, 20.5)

def root(num: int | float, exp: float | None = .5) -> float:

    return pow(num, .5)

root_25 = root(25)