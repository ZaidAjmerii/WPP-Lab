class Converter:
    # Conversion factors to meters
    conversion_factors = {
        "inches": 0.0254,
        "feet": 0.3048,
        "yards": 0.9144,
        "miles": 1609.34,
        "kilometers": 1000,
        "meters": 1,
        "centimeters": 0.01,
        "millimeters": 0.001
    }

    def _init_(self, length, unit):
        if unit not in self.conversion_factors:
            raise ValueError(f"Invalid unit: {unit}. Choose from {list(self.conversion_factors.keys())}.")
        self.length_in_meters = length * self.conversion_factors[unit]  # Convert to meters

    def inches(self):
        return self.length_in_meters / self.conversion_factors["inches"]

    def feet(self):
        return self.length_in_meters / self.conversion_factors["feet"]

    def yards(self):
        return self.length_in_meters / self.conversion_factors["yards"]

    def miles(self):
        return self.length_in_meters / self.conversion_factors["miles"]

    def kilometers(self):
        return self.length_in_meters / self.conversion_factors["kilometers"]

    def meters(self):
        return self.length_in_meters

    def centimeters(self):
        return self.length_in_meters / self.conversion_factors["centimeters"]

    def millimeters(self):
        return self.length_in_meters / self.conversion_factors["millimeters"]


# Example Usage:
c = Converter(9, 'inches')
print(c.feet())  # 0.75
print(c.meters())  # 0.2286
print(c.yards())  # ~0.25