# Challenge 4 — Polymorphism with an ElectricCar
# ElectricCar inherits directly from Vehicle (NOT FuelledVehicle)
# because it has no fuel tank — it has a battery.
# The magic: it still has drive(), so it works in any loop alongside other vehicles.

from c1_vehicle import Vehicle
from c3_types import Car, Truck, Motorcycle  # for the polymorphic example


class ElectricCar(Vehicle):

    def __init__(self, plate: str, make: str, model: str, year: int,
                 battery_kwh: float, range_km: float) -> None:
        super().__init__(plate, make, model, year)
        self.battery_kwh = battery_kwh  # total battery size
        self.range_km = range_km        # how far a full charge takes you
        self.__charge = 0.0             # current charge (starts empty)

    def get_charge(self) -> float:
        """Return the current charge in kWh."""
        return self.__charge

    def charge(self, kwh: float) -> None:
        """Add kwh to the battery. Raises ValueError if invalid or would overflow."""
        if kwh <= 0:
            raise ValueError("Must charge with a positive amount")
        if self.__charge + kwh > self.battery_kwh:
            raise ValueError("That would exceed battery capacity")
        self.__charge += kwh

    def drive(self, km: int) -> float:
        """
        Drive km kilometres using battery energy.
        Returns the kWh used.
        """
        energy_needed = self.battery_kwh * km / self.range_km

        if energy_needed > self.__charge:
            raise ValueError("Not enough charge to drive that far")

        # Only update AFTER the check passes
        self.__charge -= energy_needed
        super().drive(km)
        return energy_needed

    def describe(self) -> str:
        return super().describe() + ", electric car"
