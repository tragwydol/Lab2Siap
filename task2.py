from math import prod
def func(arg):
    try:
        if isinstance(arg, set):
            return round(prod(arg), 2)
        elif isinstance(arg, list):
            new_list = [x for x in arg if x != 0]
            if len(new_list) >= 2:
              return new_list[0] * new_list[1]
       
        elif isinstance(arg, int):
            return len(str(arg).split(".")[0])
        elif isinstance(arg, str):
            return len([x for x in arg if x.isdigit()])
        else:
           return None
    except TypeError:
       return "Неверный тип аргумента"
    finally:
       print("Функция выполнена")


print(func({1, 2, 3, 4}))  # 24.0
print(func([1, 2, 3, 0]))  # 6
print(func(123))  # 3
print(func("12345"))  # 5
print(func("abc"))  # 0