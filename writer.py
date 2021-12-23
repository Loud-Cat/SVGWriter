class SVG:
    def __init__(self, filename="file.svg", width=500, height=500):
        self.filename = filename
        self.lines = [f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">', '</svg>']

    def __repr__(self):
        return "\n".join(self.lines)
    __str__ = __repr__

    def save(self):
        with open(self.filename, "w") as svg:
            svg.write( str(self) )

    def Rect(self, x,y, w,h, fill="black", stroke="none", sw=0):
        self.lines.insert(-1, f'\t<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" />')
        self.save()

    def Circle(self, cx,cy, r, fill="black", stroke="none", sw=0):
        self.lines.insert(-1, f'\t<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" />')
        self.save()

    def Ellipse(self, cx,cy, rx,ry, fill="black", stroke="none", sw=0):
        self.lines.insert(-1, f'\t<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" />')
        self.save()

    def Line(self, x1,y1, x2,y2, stroke="black", sw=5):
        self.lines.insert(-1, f'\t<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" />')
        self.save()

    def Polyline(self, points, fill="none", stroke="black", sw=5):
        newpoints = " ".join([f"{x},{y}" for x,y in points])
        self.lines.insert(-1, f'\t<polyline points="{newpoints}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" />')
        self.save()

    def Polygon(self, points, fill="black", stroke="none", sw=0):
        newpoints = " ".join([f"{x},{y}" for x,y in points])
        self.lines.insert(-1, f'\t<polygon points="{newpoints}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" />')
        self.save()
