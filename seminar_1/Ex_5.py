# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# AB = √(xb - xa)2 + (yb - ya)2

xa = int(input('Напишите координату Х первой точки: '))
ya = int(input('Напишите координату У первой точки: '))
xb = int(input('Напишите координату Х второй точки: '))
yb = int(input('Напишите координату У второй точки: '))
import math
print(f"{math.sqrt((xb - xa) * (xb - xa) + (yb - ya) *(yb - ya)):.4f}")
