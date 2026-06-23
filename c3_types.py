# Challenge 3 — Inheritance for Vehicle Types
# We import the classes we already built instead of copying them.

from c1_vehicle import Vehicle
from c2_tank import FuelTank


class FuelledVehicle(Vehicle):
    """A vehicle that has a fuel tank. Parent of Car, Truck, and Motorcycle."""

    def __init__(self, plate: str, make: str, model: str, year: int,
                 capacity: float, consumption: float) -> None:
        super().__init__(plate, make, model, year)  # set up the base Vehicle
        self.tank = FuelTank(capacity)              # give it a fuel tank
        self.consumption = consumption              # litres used per 100 km

    def refuel(self, litres: float) -> None:
        """Pour litres into the tank."""
        self.tank.fill(litres)

    def drive(self, km: int) -> float:
        """
        Drive km kilometres.
        Burns fuel first — if there's not enough, raises ValueError and nothing changes.
        Returns how many litres were used.
        """
        litres_needed = self.consumption * km / 100

        # This will raise ValueError if there's not enough fuel.
        # Because we haven't touched kilometres yet, nothing changes on failure.
        self.tank.consume(litres_needed)

        # Only reach here if consume() succeeded
        super().drive(km)
        return litres_needed

    def range_remaining(self) -> float:
        """Return how many km we can still drive on current fuel."""
        return (self.tank.get_level() / self.consumption) * 100


class Car(FuelledVehicle):

    def __init__(self, plate: str, make: str, model: str, year: int,
                 seats: int = 5) -> None:
        super().__init__(plate, make, model, year, capacity=50.0, consumption=6.0)
        self.seats = seats

    def describe(self) -> str:
        return super().describe() + f", car, {self.seats} seats"


class Truck(FuelledVehicle):

    def __init__(self, plate: str, make: str, model: str, year: int,
                 payload_kg: int) -> None:
        super().__init__(plate, make, model, year, capacity=200.0, consumption=18.0)
        self.payload_kg = payload_kg

    def describe(self) -> str:
        return super().describe() + f", truck, {self.payload_kg} kg payload"


class Motorcycle(FuelledVehicle):

    def __init__(self, plate: str, make: str, model: str, year: int) -> None:
        super().__init__(plate, make, model, year, capacity=15.0, consumption=3.5)

    def describe(self) -> str:
        return super().describe() + ", motorcycle"


class Van(FuelledVehicle):
    """Stretch goal: a Van with cargo volume."""

    def __init__(self, plate: str, make: str, model: str, year: int,
                 volume_m3: float) -> None:
        super().__init__(plate, make, model, year, capacity=75.0, consumption=9.0)
        self.volume_m3 = volume_m3

    def describe(self) -> str:
        return super().describe() + f", van, {self.volume_m3} m³"
