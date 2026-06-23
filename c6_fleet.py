# Challenge 6 — A Fleet Manager
# The Fleet class holds any mix of vehicles and can operate on all of them at once.

import c5_dunders  # makes sure the dunder methods are attached to Vehicle

from c1_vehicle import Vehicle
from c3_types import Car, Truck, Motorcycle
from c4_electric import ElectricCar


class Fleet:

    def __init__(self, name: str) -> None:
        self.name = name
        # We use a dict keyed by plate so lookups are fast and duplicates are easy to spot.
        self._vehicles: dict[str, Vehicle] = {}

    def add(self, vehicle: Vehicle) -> None:
        """Add a vehicle. Raises ValueError if its plate is already in the fleet."""
        if vehicle.plate in self._vehicles:
            raise ValueError(f"A vehicle with plate {vehicle.plate} is already in the fleet")
        self._vehicles[vehicle.plate] = vehicle

    def remove(self, plate: str) -> None:
        """Remove a vehicle by plate. Raises KeyError if not found."""
        if plate not in self._vehicles:
            raise KeyError(f"No vehicle with plate {plate}")
        del self._vehicles[plate]

    def find(self, plate: str) -> Vehicle | None:
        """Return the vehicle with this plate, or None if not found."""
        return self._vehicles.get(plate)  # .get() returns None automatically if missing

    def total_kilometres(self) -> int:
        """Return the total km driven by the whole fleet."""
        return sum(v.kilometres for v in self._vehicles.values())

    def drive_all(self, km: int) -> tuple[list, list]:
        """
        Try to drive every vehicle km kilometres.
        Returns (successes, failures).
        successes = list of plates that worked.
        failures  = list of (plate, error message) for those that didn't.
        """
        successes = []
        failures = []
        for plate, vehicle in self._vehicles.items():
            try:
                vehicle.drive(km)
                successes.append(plate)
            except ValueError as e:
                failures.append((plate, str(e)))
        return successes, failures

    def cars_only(self) -> list:
        """
        Stretch: return only the Car instances.
        isinstance is acceptable here because the POINT of this method is
        to filter by type. In print_summary we deliberately avoid it so that
        any new vehicle type works without changing print_summary.
        """
        return [v for v in self._vehicles.values() if isinstance(v, Car)]

    def average_kilometres(self) -> float:
        """
        Return the mean km across the fleet.
        Returns 0.0 for an empty fleet (avoids division by zero).
        """
        if len(self._vehicles) == 0:
            return 0.0
        return self.total_kilometres() / len(self._vehicles)

    # ── Dunder methods ───────────────────────────────────────────────────────

    def __len__(self) -> int:
        return len(self._vehicles)

    def __iter__(self):
        """Allows: for v in fleet"""
        return iter(self._vehicles.values())

    def __contains__(self, plate: str) -> bool:
        """Allows: "B-1" in fleet"""
        return plate in self._vehicles

    def __str__(self) -> str:
        return f"Fleet '{self.name}': {len(self)} vehicle(s)"


# ── Top-level summary function ───────────────────────────────────────────────

def print_summary(fleet: Fleet) -> None:
    """Print a full fleet report. No isinstance — every vehicle describes itself."""
    print("=== FLEET REPORT ===")
    print(fleet)
    print(f"Total kilometres: {fleet.total_kilometres()}")
    print("-" * 20)
    for vehicle in fleet:          # uses __iter__
        print(vehicle)             # uses __str__ → describe()
    print("=" * 20)


# ── Quick demo ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    fleet = Fleet("Main")
    fleet.add(Car("B-1", "Toyota", "Yaris", 2023, seats=5))
    fleet.add(Truck("B-2", "MAN", "TGX", 2021, payload_kg=18000))
    fleet.add(Motorcycle("B-3", "Yamaha", "MT-07", 2024))
    fleet.add(ElectricCar("B-4", "Tesla", "Model 3", 2024,
                          battery_kwh=60.0, range_km=400))

    print(len(fleet))           # 4
    print("B-2" in fleet)      # True
    print("B-99" in fleet)     # False
    print(fleet.find("B-3").make)  # Yamaha
    print(fleet.find("B-99"))      # None

    # Empty tanks → drive_all fails for everyone
    succ, fail = fleet.drive_all(10)
    print(succ)       # []
    print(len(fail))  # 4

    # Refuel / charge each vehicle
    fleet.find("B-1").refuel(5)
    fleet.find("B-2").refuel(5)
    fleet.find("B-3").refuel(5)
    fleet.find("B-4").charge(20)

    succ, fail = fleet.drive_all(10)
    print(len(succ))  # 4
    print(len(fail))  # 0
    print(fleet.total_kilometres())  # 40

    fleet.remove("B-3")
    print(len(fleet))       # 3
    print("B-3" in fleet)  # False

    print()
    print_summary(fleet)
