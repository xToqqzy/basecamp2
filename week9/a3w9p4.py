class Converter:
    def __init__(self, lenght, unit):
        self.lenght = lenght
        self.unit = unit

        if self.unit == 'inches':
            return self.lenght * 0.0254
        elif self.unit == 'feet':
            return self.lenght * 0.3048
        elif self.unit == 'yards':
            return self.lenght * 0.9144
        elif self.unit == 'miles':
            return self.lenght * 1609, 344
        elif self.unit == 'kilometers':
            return self.lenght * 1000
        elif self.unit == 'meters':
            return self.lenght * 1
        elif self.unit == 'centimeters':
            return self.lenght * 0.01
        elif self.unit == 'millimeters':
            return self.lenght * 0.001

    def inches(self):
        self.unit == 'inches'
        return self.lenght / 0.0254

    def feet(self):
        self.unit == 'feet'
        return self.lenght / 3.28084

    def yards(self):
        self.unit == 'yards'
        return self.lenght / 1.09361

    def miles(self):
        self.unit == 'miles'
        return self.lenght / 0.0006214

    def kilomters(self):
        self.unit == 'kilometers'
        return self.lenght / 0.001

    def meters(self):
        self.unit == 'meters'
        return self.lenght / 1

    def centimeters(self):
        self.unit == 'centimeters'
        return self.lenght / 100

    def millimeters(self):
        self.unit == 'millimeters'
        return self.lenght / 1000


c = Converter(9, "inches")
print(c.feet())
