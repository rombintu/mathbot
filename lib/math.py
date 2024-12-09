import random
import fractions
import math 

def generate_math_problem_5_class():
    # Выбираем случайным образом операцию: 1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление
    operation = random.randint(1, 4)
    
    # Генерируем два случайных числа в диапазоне от 1 до 100
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    
    if operation == 1:
        # Сложение
        problem = f"{num1} + {num2} = ?"
        answer = num1 + num2
    elif operation == 2:
        # Вычитание
        problem = f"{num1} - {num2} = ?"
        answer = num1 - num2
    elif operation == 3:
        # Умножение
        problem = f"{num1} * {num2} = ?"
        answer = num1 * num2
    elif operation == 4:
        # Деление
        # Убеждаемся, что деление будет без остатка
        num1 = num1 * num2
        problem = f"{num1} / {num2} = ?"
        answer = num1 // num2
    
    return problem, answer


def generate_math_problem_7_class():
    # Выбираем случайным образом тип задачи: 1 - дроби, 2 - проценты, 3 - степени, 4 - обычная арифметика
    problem_type = random.randint(1, 4)
    
    if problem_type == 1:
        # Задача с дробями
        num1 = random.randint(1, 10)
        denom1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        denom2 = random.randint(1, 10)
        
        fraction1 = fractions.Fraction(num1, denom1)
        fraction2 = fractions.Fraction(num2, denom2)
        
        operation = random.choice(['+', '-', '*', '/'])
        
        if operation == '+':
            problem = f"{fraction1} + {fraction2} = ?"
            answer = fraction1 + fraction2
        elif operation == '-':
            problem = f"{fraction1} - {fraction2} = ?"
            answer = fraction1 - fraction2
        elif operation == '*':
            problem = f"{fraction1} * {fraction2} = ?"
            answer = fraction1 * fraction2
        elif operation == '/':
            problem = f"{fraction1} / {fraction2} = ?"
            answer = fraction1 / fraction2
    
    elif problem_type == 2:
        # Задача с процентами
        number = random.randint(1, 1000)
        percent = random.randint(1, 100)
        
        problem = f"{percent}% от {number} = ?"
        answer = (percent / 100) * number
    
    elif problem_type == 3:
        # Задача со степенями
        base = random.randint(1, 10)
        exponent = random.randint(1, 5)
        
        problem = f"{base}^{exponent} = ?"
        answer = base ** exponent
    
    elif problem_type == 4:
        # Обычная арифметика
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        
        operation = random.choice(['+', '-', '*', '/'])
        
        if operation == '+':
            problem = f"{num1} + {num2} = ?"
            answer = num1 + num2
        elif operation == '-':
            problem = f"{num1} - {num2} = ?"
            answer = num1 - num2
        elif operation == '*':
            problem = f"{num1} * {num2} = ?"
            answer = num1 * num2
        elif operation == '/':
            num1 = num1 * num2  # Убеждаемся, что деление будет без остатка
            problem = f"{num1} / {num2} = ?"
            answer = num1 // num2
    
    return problem, answer


def generate_math_problem_9_class():
    # Выбираем случайным образом тип задачи: 1 - квадратное уравнение, 2 - тригонометрия, 3 - логарифмы, 4 - обычная арифметика
    problem_type = random.randint(1, 4)
    
    if problem_type == 1:
        # Задача с квадратным уравнением
        a = random.randint(1, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        
        problem = f"Решите квадратное уравнение: {a}x^2 + {b}x + {c} = 0"
        
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            answer = f"x1 = {x1}, x2 = {x2}"
        elif discriminant == 0:
            x1 = -b / (2*a)
            answer = f"x1 = x2 = {x1}"
        else:
            answer = "Нет действительных корней"
    
    elif problem_type == 2:
        # Задача с тригонометрией
        angle = random.randint(0, 360)
        trig_func = random.choice(['sin', 'cos', 'tan'])
        
        problem = f"Вычислите {trig_func}({angle}°) = ?"
        
        if trig_func == 'sin':
            answer = math.sin(math.radians(angle))
        elif trig_func == 'cos':
            answer = math.cos(math.radians(angle))
        elif trig_func == 'tan':
            answer = math.tan(math.radians(angle))
        
        answer = round(answer, 4)
    
    elif problem_type == 3:
        # Задача с логарифмами
        base = random.randint(2, 10)
        number = random.randint(1, 100)
        
        problem = f"Вычислите log_{base}({number}) = ?"
        
        answer = math.log(number, base)
        answer = round(answer, 4)
    
    elif problem_type == 4:
        # Обычная арифметика
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        
        operation = random.choice(['+', '-', '*', '/'])
        
        if operation == '+':
            problem = f"{num1} + {num2} = ?"
            answer = num1 + num2
        elif operation == '-':
            problem = f"{num1} - {num2} = ?"
            answer = num1 - num2
        elif operation == '*':
            problem = f"{num1} * {num2} = ?"
            answer = num1 * num2
        elif operation == '/':
            num1 = num1 * num2  # Убеждаемся, что деление будет без остатка
            problem = f"{num1} / {num2} = ?"
            answer = num1 // num2
    
    return problem, answer