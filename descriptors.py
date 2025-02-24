class Unit:
    def __init__(self, base_unit, conversion_factor=1.0):
        self.base_unit = base_unit
        self.conversion_factor = conversion_factor
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        # Check if the value has been set for this unit on this instance
        if self._name not in instance.__dict__:
            # If not, try to get it from another unit (conversion)
            for unit_name, unit in owner.__dict__.items():
                if isinstance(unit, Unit) and unit.base_unit == self.base_unit and unit._name != self._name and unit._name in instance.__dict__:
                    # Found another unit that stores the value in the correct base unit
                    value = instance.__dict__[unit._name]
                    # Convert it to the requested unit and store it
                    instance.__dict__[self._name] = value * unit.conversion_factor / self.conversion_factor
                    break  # Stop after the first conversion
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value / self.conversion_factor

class Length:
    meters = Unit("meters")
    feet = Unit("meters", 3.281)
    inches = Unit("meters", 39.37)

    def __init__(self, meters=None, feet=None, inches=None):
        if meters is not None:
            self.meters = meters
        elif feet is not None:
            self.feet = feet
        elif inches is not None:
            self.inches = inches


length = Length(feet=10)
print(length.meters)    # Output: 3.048
print(length.feet)      # Output: 10.0
length.inches = 100
print(length.meters) # Output: 2.54
print(length.inches) # Output: 100.0

length.meters = 2
print(length.feet) # Output: 6.562