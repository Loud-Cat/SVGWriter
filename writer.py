from shapes imoprt *

class SVG:
    def __init__(self, filename="file.svg", width=500, height=500):
        self.filename = filename
        self.lines = [f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">']

    def append(self, shape):
        self.lines.append(shape)

    def __repr__(self):
        return "\n".join(self.lines + ["</svg>"])
    __str__ = __repr__

    def write(self):
        with open(self.filename, "w") as svg:
            svg.write( str(self) )
