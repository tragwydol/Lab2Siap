import math

def solve(a, b, c):
  # Проверка входных данных
  
  try:
    if a == 0:
      raise ZeroDivisionError("Коэффициент a не может быть равен 0")
    if b == 0 and c == 0:
      raise ValueError("Коэффициенты b и c не могут быть равны 0")
  except ZeroDivisionError as e:
    print(e)
    return None
  except ValueError as e:
    print(e)
    return None

  # Вычисление корней уравнения

  x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
  x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

  # Сортировка корней

  if x1 >= x2:
    return x1, x2
  else:
    return x2, x1

a, b, c = 3, 0, 0

print(solve(a, b, c))