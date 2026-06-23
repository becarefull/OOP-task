OOP Workout

## Challenges completed
- Challenge 1: Vehicle  class
- Challenge 2: FuelTank with encapsulation
- Challenge 3: Car, Truck, Motorcycle via inheritance
- Challenge 4: ElectricCar (polymorphism)
- Challenge 5: Dunder methods
- Challenge 6: Fleet manager


## Difficulties

Getting inheritance to click took a while, it wasn't obvious at first why you would
extend a class instead of just writing everything from scratch. The super() calls were
especially confusing because it's not clear where the code "goes" when you call it.

The double underscore encapsulation (__attr) was tricky because Python doesn't block
access the way you'd expect it just renames it, which felt strange at first.

The ElectricCar challenge was probably the hardest. Because it doesn't inherit from
FuelledVehicle, you have to build the drive() logic yourself from scratch, and it's
easy to forget to check the charge before updating anything.

The "validate first, mutate after" pattern took some getting used to the instinct
is to update the value and then check if something went wrong, but that causes bugs
when the error check fails halfway through.
