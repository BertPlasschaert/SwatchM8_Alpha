class Swatch:

    def __init__(self, name, coordinate, size, color):
        # type: (str, list, int, list) -> None

        self.name = name
        self.coordinate = coordinate
        self.size = size
        self.color = color
        self.parts = []

    def addPart(self, part):
        # type: (object) -> None

        self.parts.append(part)
