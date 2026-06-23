# Challenge 5 — Dunder Methods
# We extend c3_types and c4_electric by adding __str__, __repr__, __eq__,
# __hash__, and __lt__ to the base Vehicle class.
# All subclasses get these for free through inheritance.

from c1_vehicle import Vehicle
from c3_types import Car, Truck, Motorcycle
from c4_electric import ElectricCar


# We patch the dunder methods directly onto Vehicle.
# (In a real project you'd edit the original file, but the worksheet asks for a new file.)

def _vehicle_str(self) -> str:
    """What you see when you print(vehicle). Same as describe()."""
    return self.describe()

def _vehicle_repr(self) -> str:
    """Developer-friendly representation. Shows the class name automatically."""
    cls = type(self).__name__   # e.g. "Car", "Truck", "ElectricCar"
    return f"{cls}('{self.plate}', '{self.make}', '{self.model}', {self.year})"

def _vehicle_eq(self, other) -> bool:
    """Two vehicles are the same if they share the same plate."""
    if not isinstance(other, Vehicle):
        return NotImplemented
    return self.plate == other.plate

def _vehicle_hash(self) -> int:
    """Needed whenever we define __eq__, so vehicles still work in sets/dicts."""
    return hash(self.plate)

def _vehicle_lt(self, other) -> bool:
    """Lets us sort a list of vehicles by plate with sorted()."""
    if not isinstance(other, Vehicle):
        return NotImplemented
    return self.plate < other.plate

# Attach them to the class
Vehicle.__str__  = _vehicle_str
Vehicle.__repr__ = _vehicle_repr
Vehicle.__eq__   = _vehicle_eq
Vehicle.__hash__ = _vehicle_hash
Vehicle.__lt__   = _vehicle_lt


# ── Quick demo ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    c  = Car("B-CD-5678", "Toyota", "Yaris", 2023, seats=5)
    tr = Truck("B-CD-5678", "MAN", "Other", 2000, payload_kg=1)
    tr2 = Truck("B-EF-9012", "MAN", "TGX", 2021, payload_kg=18000)
    e  = ElectricCar("B-EV-0001", "Tesla", "Model 3", 2024,
                     battery_kwh=60.0, range_km=400)

    print(str(c))    # 2023 Toyota Yaris (B-CD-5678), car, 5 seats
    print(repr(c))   # Car('B-CD-5678', 'Toyota', 'Yaris', 2023)
    print(c == tr)   # True  — same plate
    print(c == Car("B-XX-0000", "Toyota", "Yaris", 2023))  # False — different plate
    print(repr(tr2)) # Truck('B-EF-9012', 'MAN', 'TGX', 2021)
    print(repr(e))   # ElectricCar('B-EV-0001', 'Tesla', 'Model 3', 2024)

    # Set test: adding the same vehicle twice gives a set of size 1
    s = {c, Car("B-CD-5678", "Toyota", "Corolla", 2020)}
    assert len(s) == 1, "Set should deduplicate by plate"
    print("Set test passed ✓")
