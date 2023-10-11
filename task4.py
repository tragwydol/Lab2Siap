def divide():
    try:
        x = float(input("Введите делимое: "))
        y = float(input("Введите делитель: "))
        return x/y
    except ZeroDivisionError:
        return "Деление на ноль невозможно"
    except ValueError:
        return "Ввод не является числом"
    finally: 
        print("Завершение работы функции divide()")
        
print(divide())