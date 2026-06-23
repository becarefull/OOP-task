# Challenge 1 — A First Class
# This is the base Vehicle class. Every other vehicle will build on this.

class Vehicle:
    fleet_size = 0  # This belongs to the CLASS, not any single vehicle

    def __init__(self, plate: str, make: str, model: str, year: int) -> None:
        self.plate = plate
        self.make = make
        self.model = model
        self.year = year
        self.kilometres = 0  # Every new vehicle starts at 0 km

        Vehicle.fleet_size += 1  # Count how many vehicles we've made

    def drive(self, km: int) -> None:
        """Add km to the odometer. km must be a positive number."""
        if km <= 0:
            raise ValueError("km must be greater than zero")
        self.kilometres += km

    def describe(self) -> str:
        """Return a human-readable description of the vehicle."""
        return f"{self.year} {self.make} {self.model} ({self.plate})"

    def service_due(self) -> bool:
        """Return True if the vehicle has driven more than 15 000 km."""
        return self.kilometres > 15000
