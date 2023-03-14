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

    # Если символ - точка и в выражении уже есть точка, не добавляем его

    if symbol == "." and "." in self.input:

        return

    # Иначе добавляем символ к атрибуту input

    self.input += symbol




# Определяем метод calculate для вычисления результата введенного выражения
def calculate(self):
    try:
        # Проверяем длину и содержание выражения 
        if len(self.input) == 0 or all(char in ".+-*/" for char in self.input):
            # Генерируем исключение ValueError с сообщением "Empty or invalid expression"
            raise ValueError("Empty or invalid expression")
        
        # Пытаемся разделить выражение на два операнда и оператор по пробелу 
        operand1, operator, operand2 = self.input.split()
        
        # Проверяем каждый символ в операндах на то, что он является цифрой или точкой 
        if not all(char.isdigit() or char == "." for char in operand1) or not all(char.isdigit() or char == "." for char in operand2):
            # Генерируем исключение ValueError с сообщением "Invalid operands"
            raise ValueError("Invalid operands")
        
        # Преобразуем операнды в числа с плавающей запятой 
        operand1 = float(operand1)
        operand2 = float(operand2)
        
        # Выполняем математическое действие в зависимости от оператора и присваиваем результат атрибуту output 
        if operator == "+":
            self.output = operand1 + operand2
        elif operator == "-":
            self.output = operand1 - operand2
        elif operator == "*":
            self.output = operand1 * operand2
        elif operator == "/":
            self.output = operand1 / operand2
        else:
            raise ValueError("Invalid operator")
        
        # Если результат - бесконечность или не число, генерируем исключение ValueError 
        if math.isinf(self.output) or math.isnan(self.output):
            raise ValueError("Invalid result")
        
        # Форматируем результат с двумя знаками после запятой 
        self.output = f"{self.output:.2f}"
    
    except (ValueError) as e:
         # Если возникло исключение при разборе или выполнении выражения, присваиваем сообщение об ошибке атрибуту error 
         self.error = f"Error: {e}"


# Определяем метод display для отображения состояния калькулятора

def display(self):

    # Если есть ошибка, выводим ее на экран

    if self.error:

        print(self.error)

    # Иначе выводим введенное выражение и результат

    else:

        print(f"Input: {self.input}")



# Создаем объект calculator из класса Calculator 
calculator = Calculator()


