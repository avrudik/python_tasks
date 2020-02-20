# Пользователь вводит три стороны треугольника. Определить является ли он прямоугольным.
# Примечание: проверить существование треугольника.
# Сделать ввод значений до тех пор, пока пользователь не введет правильные значения.


x = 0


def check():
    """Проверяет, правильно ли вбито значение стороны треугольника."""
    global x
    try:
        if int(x) > 0:
            x = int(x)
            return x
        else:
            x = int(input('Введите положительное значение стороны треугольника: '))
            check()
    except ValueError:
        x = input('Введите корректное значение для стороны треугольника: ')
        check()


triangle = list()
for a in range(3):
    x = input(f'Введите {a + 1} сторону треугольника: ')
    check()
    triangle.append(x)

if (triangle[0] > triangle[1] + triangle[2] or
        triangle[1] > triangle[0] + triangle[2] or
        triangle[2] > triangle[0] + triangle[1]):
    print(f'Треугольника со сторонами {triangle[0]}, {triangle[1]}, {triangle[2]} не существует.')
elif (triangle[0] ** 2 == triangle[1] ** 2 + triangle[2] ** 2 or
      triangle[1] ** 2 == triangle[0] ** 2 + triangle[2] ** 2 or
      triangle[2] ** 2 == triangle[0] ** 2 + triangle[1] ** 2):
    print(f'Треугольник со сторонами {triangle[0]}, {triangle[1]}, {triangle[2]} - прямоугольный.')
