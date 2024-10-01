from triangle_calculator import calculate_properties, TriangleProperties


def main() -> None:
    assert TriangleProperties(area=1.7320508075688772, perimiter=6, inradius=0.5773502691896257, circumradius=1.1547005383792517) == calculate_properties(2, 2, 2)
    assert TriangleProperties(area=1.984313483298443, perimiter=7, inradius=0.5669467095138409, circumradius=1.5118578920369088) == calculate_properties(2, 2, 3)
