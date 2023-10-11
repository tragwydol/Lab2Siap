def is_increasing(row):
 for i in range(len(row) - 1):
    if row[i] > row[i + 1]:
       return False
 return True

def reverse_row(row):
 for i in range(len(row) // 2):
    row[i], row[-i - 1] = row[-i - 1], row[i]

def find_and_reverse(matrix):
 for i in range(len(matrix)):
     if is_increasing(matrix[i]):
        reverse_row(matrix[i])
        return i
 return -1

try:
  matrix = [[0, 0, 0], [2, 3, 4], [2, 8, -2]]
  i = find_and_reverse(matrix)
  if i != -1:
   print(f"Первая возрастающая строка: {matrix[i]}")
except IndexError as e:
  print(f"Ошибка: {e}")
finally:
  print("Завершено")
