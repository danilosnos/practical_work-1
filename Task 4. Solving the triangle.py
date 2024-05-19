import math
def get_angle(a,b,c):
    r = math.acos((b*b + c*c - a*a)/(2*b*c))*180/math.pi
    return r


a = float(input("Введите сторону 1: "))
b = float(input("Введите сторону 2: "))
c = float(input("Введите сторону 3: "))
P=a+b+c

def geron_area(a, b, c):
    # Полупериметр
    s = (a + b + c) / 2
    # Формула Герона для площади треугольника

    return __import__('math').sqrt(s * (s - a) * (s - b) * (s - c))
triangle_area = geron_area(a, b, c)


angle_a = get_angle(a,b,c)
angle_b = get_angle(b,a,c)
angle_c = get_angle(c,a,b)

print("Угол напротив стороны a:",round(angle_a,2))
print("Угол напротив стороны b:",round(angle_b,2))
print("Угол напротив стороны c:",round(angle_c,2))
print()
print("Периметр треугольника = ",P)
print(f"Площадь треугольника = {triangle_area}")