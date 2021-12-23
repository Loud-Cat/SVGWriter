def Rect(x,y, w,h, fill="black", stroke="none", sw=0):
    return f'\t<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" />'

def Circle(cx,cy, r, fill="black", stroke="none", sw=0):
    return f'\t<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" />'

def Ellipse(cx,cy, rx,ry, fill="black", stroke="none", sw=0):
    return f'\t<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" />'

def Line(x1,y1, x2,y2, stroke="black", sw=5):
    return f'\t<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" />'

def Polyline(points, fill="none", stroke="black", sw=5):
    newpoints = " ".join([f"{x},{y}" for x,y in points])
    return f'\t<polyline points="{newpoints}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" />'

def Polygon(points, fill="black", stroke="none", sw=0):
    newpoints = " ".join([f"{x},{y}" for x,y in points])
    return f'\t<polygon points="{newpoints}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" />'
