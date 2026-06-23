# Challenge 2 — A FuelTank with Encapsulation
# We use __level and __capacity (double underscore) so nothing outside
# this class can accidentally change the fuel level directly.

class FuelTank:

    def __init__(self, capacity: float) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero")
        self.__capacity = capacity  # max litres the tank holds
        self.__level = 0.0          # current litres in the tank

    def get_level(self) -> float:
        """Return the current fuel level, rounded to 2 decimal places."""
        return round(self.__level, 2)

    def get_capacity(self) -> float:
        """Return the total capacity of the tank."""
        return self.__capacity

    def fill(self, litres: float) -> None:
        """Add litres to the tank. Raises ValueError if invalid or would overflow."""
        if litres <= 0:
            raise ValueError("Must fill with a positive amount")
        if self.__level + litres > self.__capacity:
            raise ValueError("That would overfill the tank")
        # Only update AFTER all checks pass
        self.__level += litres

    def consume(self, litres: float) -> None:
        """Remove litres from the tank. Raises ValueError if not enough fuel."""
        if litres <= 0:
            raise ValueError("Must consume a positive amount")
        if litres > self.__level:
            raise ValueError("Not enough fuel in the tank")
        # Only update AFTER all checks pass
        self.__level -= litres

    def fill_to_full(self) -> float:
        """Top up the tank and return how many litres were added."""
        added = self.__capacity - self.__level
        self.__level = self.__capacity
        return round(added, 2)

    def percent_full(self) -> float:
        """Return the fuel level as a percentage, rounded to 1 decimal."""
        return round((self.__level / self.__capacity) * 100, 1)
