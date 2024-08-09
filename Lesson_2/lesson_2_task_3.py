import math
def square(side):
    area = side ** 2
    if not isinstance(area, int):
        area = math.ceil(area)
    return area
print(square(3.2))
print(square(10.3))