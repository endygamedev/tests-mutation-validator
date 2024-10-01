from dataclasses import dataclass
from math import sqrt


@dataclass
class TriangleProperties:
    area: float
    perimiter: float
    inradius: float
    circumradius: float


def calculate_properties(a: float, b: float, c: float) -> TriangleProperties:
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Such triangle does not exists")

    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    perimiter = a + b + c
    inradius = area / s
    circumradius = (a * b * c) / (4 * area)

    return TriangleProperties(area=area, perimiter=perimiter, inradius=inradius, circumradius=circumradius)
    