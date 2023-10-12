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
  D=b ** 2 - 4 * a * c

  if D < 0:
    return 'корней нет'
  elif D==0:
    return -b/(2*a)
  

  x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
  x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

  # Сортировка корней

  if x1 >= x2:
    return x1, x2
  else:
    return x2, x1

try:
  a=int(input('Input a : '))
  b=int(input('Input b : '))
  c=int(input('Input c : '))
except:
  print("Неверный ввод")
  exit()

  
print(solve(a, b, c))