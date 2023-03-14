# Импортируем модуль math для использования математических функций
import math

# Создаем класс Calculator для хранения состояния калькулятора
class Calculator:
    # Инициализируем атрибуты класса
    def __init__(self):
        # input хранит введенное пользователем выражение
        self.input = ""
        # output хранит результат вычисления выражения
        self.output = ""
        # error хранит сообщение об ошибке в случае невалидного выражения
        self.error = ""

    # Определяем метод display для отображения состояния калькулятора
    def display(self):
        # Если есть ошибка, выводим ее на экран
        if self.error:
            print(self.error)
        # Иначе выводим введенное выражение и результат
        else:
            print(f"Input: {self.input}")
            print(f"Output: {self.output}")

    # Определяем метод clear для очистки состояния калькулятора
    def clear(self):
        # Обнуляем все атрибуты класса
        self.input = ""
        self.output = ""
        self.error = ""

    # Определяем метод append для добавления символа к введенному выражению
    def append(self, symbol):
        # Добавляем символ к атрибуту input
        self.input += symbol

    # Определяем метод calculate для вычисления результата введенного выражения
    def calculate(self):
        try:
            # Пытаемся выполнить математическое действие с помощью функции eval и присвоить результат атрибуту output 
            self.output = eval(self.input)
            # Если результат - бесконечность или не число, генерируем исключение ValueError 
            if math.isinf(self.output) or math.isnan(self.output):
                raise ValueError("Invalid result")
            # Форматируем результат с двумя знаками после запятой 
            self.output = f"{self.output:.2f}"
        
        except (SyntaxError, NameError, ZeroDivisionError, ValueError) as e:
            # Если возникло исключение при выполнении функции eval или проверки результата, присваиваем сообщение об ошибке атрибуту error 
            self.error = f"Error: {e}"

# Создаем объект calculator из класса Calculator 
calculator = Calculator()

# Тестируем работу калькулятора с разными примерами 

# Пример 1: 2 + 3 
calculator.append("2")
calculator.append("+")
calculator.append("3")
calculator.calculate()
calculator.display()
# Output: Input: 2+3 Output: 5.00

# Пример 2: 7 - 4 
calculator.clear()
calculator.append("7")
calculator.append("-")
calculator.append("4")
calculator.calculate()
calculator.display()
# Output: Input: 7-4 Output: 3.00

# Пример 3: 6 * 8 
calculator.clear()
calculator.append("6")
calculator.append("*")
calculator.append("8")
calculator.calculate()
calculator.display()
# Output: Input: 6*8 Output: 48.00

# Пример 4: 9 / 3 
calculator.clear()
calculator.append("9")
calculator.append("/")
calculator.append("3")
calculator.calculate()
calculator.display()
# Output: Input: 9/3 Output: 3.00

# Пример 5: . + .
calculator.clear()
calculator.append(".")
calculator.append("+")
calculator.append(".")
calculator.calculate()
calculator.display()
# Output: Error: invalid syntax

# Пример 6: 5 + . 
calculator.clear()
calculator.append("5")
calculator.append("+")
calculator.append(".")
calculator.calculate()
calculator.display()
# Output: Error: invalid syntax

# Пример 7: 9 / 0 
calculator.clear()
calculator.append("9")
calculator.append("/")
calculator.append("0")
calculator.calculate()
calculator.display()
# Output: Error: division by zero
