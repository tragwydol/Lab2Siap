from math import prod
def func(arg):
    try:
        #Проверяет, является ли аргумент arg множеством
        if isinstance(arg, set):
            return round(prod(arg), 2)
        #Проверяет, является ли аргумент arg списком
        elif isinstance(arg, list):
            new_list = [x for x in arg if x != 0]
            if len(new_list) >= 2:
              return new_list[0] * new_list[1]
        #Проверяет, является ли аргумент arg целым числом
        elif isinstance(arg, int):
            return len(str(arg).split(".")[0])
        #Проверяет, является ли аргумент arg строкой
        elif isinstance(arg, str):
            return len([x for x in arg if x.isdigit()])
        else:
           return None
    except TypeError:
       return "Неверный тип аргумента"
    finally:
       print("Функция выполнена")


print(func({1, 2, 3, 4}))  # 24
print(func([1, 2, 3, 0]))  # 2
print(func(1236))  # 4
print(func("129658"))  # 6
print(func("abc"))  # 0