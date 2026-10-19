# ====================================================================
# Nombre: Victor Hugo Reyna Leos
# Matrícula: 2630104
# ====================================================================

# ====================================================================
# RESUMEN 
# En Python, 'int' se usa para números enteros (sin decimales) y 'float'
# para números con punto decimal. Los booleanos (bool) solo pueden 
# valer True o False, y generalmente los obtenemos al hacer comparaciones 
# (como >, <, ==). Es muy importante validar que los datos estén en
# rangos correctos y evitar divisiones entre cero para que el programa
# no falle. Este documento cubre 6 problemas usando operaciones 
# matemáticas, cálculos de ratios y validaciones lógicas para tomar 
# decisiones a través de variables booleanas.
# ====================================================================

# ====================================================================
# PRINCIPIOS Y BUENAS PRÁCTICAS
# - Usar el tipo de dato correcto: int para contadores, float para dinero/medidas.
# - Validar siempre la entrada (que no haya horas negativas ni divisiones entre cero).
# - Usar funciones matemáticas básicas como min() y max() para simplificar el código.
# - Guardar resultados intermedios en variables para no repetir operaciones largas.
# - Nombrar variables descriptivamente en inglés para mantener un buen estándar.
# ====================================================================


# ====================================================================
# Problema 1: Convertidor de temperatura y bandera de rango
# Descripción: Convierte grados Celsius a Fahrenheit y Kelvin. Revisa si 
# la temperatura es mayor o igual a 30 para prender la bandera (True).
#
# Entradas:
# - temp_c_input (float/string)
# Salidas:
# - "Fahrenheit: <temp_f>"
# - "Kelvin: <temp_k>"
# - "High temperature: true|false"
# Validaciones:
# - Que el valor pueda ser convertido a float.
# - No permitir Kelvin menor a 0 (cero absoluto).
#
# Casos de prueba:
# 1) Normal: 25.0
# 2) Borde: 30.0 (exactamente en el límite de alta temperatura)
# 3) Error: "hola" (no es número) o -300 (Kelvin negativo imposible)
# ====================================================================

def problem_1_temperature(temp_c_input):
    try:
        temp_c = float(temp_c_input)
    except ValueError:
        print("Error: invalid input")
        return

    temp_k = temp_c + 273.15
    if temp_k < 0.0:
        print("Error: invalid input (physically impossible temperature)")
        return

    temp_f = temp_c * 9 / 5 + 32
    is_high_temperature = (temp_c >= 30.0)

    print(f"Fahrenheit: {temp_f}")
    print(f"Kelvin: {temp_k}")
    # str().lower() se usa para que imprima "true/false" en minúsculas
    print(f"High temperature: {str(is_high_temperature).lower()}")

print("--- Test Problem 1 ---")
problem_1_temperature(25.0) # Normal
problem_1_temperature(30.0) # Borde
problem_1_temperature(-300) # Error
print("\n")


# ====================================================================
# Problema 2: Horas de trabajo y pago de tiempo extra
# Descripción: Calcula el pago de un trabajador. Las primeras 40 horas 
# se pagan normal, las extras al 1.5x (150%).
#
# Entradas:
# - hours_worked_input (float)
# - hourly_rate_input (float)
# Salidas:
# - "Regular pay:", "Overtime pay:", "Total pay:", "Has overtime:"
# Validaciones:
# - hours_worked >= 0
# - hourly_rate > 0
#
# Casos de prueba:
# 1) Normal: 45 horas, pago de 100 por hora.
# 2) Borde: 40 horas (sin extras, límite exacto), pago de 100.
# 3) Error: -5 horas, o pago de -10.
# ====================================================================

def problem_2_payroll(hours_worked_input, hourly_rate_input):
    try:
        hours_worked = float(hours_worked_input)
        hourly_rate = float(hourly_rate_input)
    except ValueError:
        print("Error: invalid input")
        return

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
        return

    has_overtime = (hours_worked > 40.0)
    
    # min() y max() evitan usar if/else para separar las horas
    regular_hours = min(hours_worked, 40.0)
    overtime_hours = max(0.0, hours_worked - 40.0)

    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay

    print(f"Regular pay: {regular_pay}")
    print(f"Overtime pay: {overtime_pay}")
    print(f"Total pay: {total_pay}")
    print(f"Has overtime: {str(has_overtime).lower()}")

print("--- Test Problem 2 ---")
problem_2_payroll(45, 100) # Normal
problem_2_payroll(40, 100) # Borde
problem_2_payroll(-5, 100) # Error
print("\n")


# ====================================================================
# Problema 3: Elegibilidad de descuento con booleanos
# Descripción: Aplica un 10% de descuento si eres estudiante, mayor de 
# edad (senior) o si compras más de 1000.
#
# Entradas:
# - purchase_input (float)
# - student_text (string: "YES" o "NO")
# - senior_text (string: "YES" o "NO")
# Salidas:
# - "Discount eligible: true|false"
# - "Final total: <final_total>"
# Validaciones:
# - purchase_total >= 0.0
# - textos deben ser "YES" o "NO" (sin importar mayúsculas/minúsculas).
#
# Casos de prueba:
# 1) Normal: 500, "YES", "NO" (aplica por estudiante).
# 2) Borde: 1000, "NO", "NO" (aplica justo por el monto).
# 3) Error: -100, "Si", "NO" (precio negativo y texto inválido).
# ====================================================================

def problem_3_discount(purchase_input, student_text, senior_text):
    try:
        purchase_total = float(purchase_input)
    except ValueError:
        print("Error: invalid input")
        return

    if purchase_total < 0:
        print("Error: invalid input")
        return

    # Normalizar textos quitando espacios y pasando a mayúsculas
    student_clean = student_text.strip().upper()
    senior_clean = senior_text.strip().upper()

    if student_clean not in ["YES", "NO"] or senior_clean not in ["YES", "NO"]:
        print("Error: invalid input")
        return

    # Convertir a booleanos
    is_student = (student_clean == "YES")
    is_senior = (senior_clean == "YES")

    discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)

    if discount_eligible:
        final_total = purchase_total * 0.9 # Aplica el 10% de descuento
    else:
        final_total = purchase_total

    print(f"Discount eligible: {str(discount_eligible).lower()}")
    print(f"Final total: {final_total}")

print("--- Test Problem 3 ---")
problem_3_discount(500, "yes", "no") # Normal
problem_3_discount(1000, "NO", "no") # Borde
problem_3_discount(-100, "si", "no") # Error
print("\n")


# ====================================================================
# Problema 4: Estadísticas básicas de 3 enteros
# Descripción: Pide 3 números enteros y saca suma, promedio, el mayor, 
# el menor, y una bandera booleana si todos son pares.
#
# Entradas:
# - n1_input, n2_input, n3_input (int)
# Salidas:
# - "Sum:", "Average:", "Max:", "Min:", "All even: true|false"
# Validaciones:
# -Los 3 puedan ser convertidos a enteros.
#
# Casos de prueba:
# 1) Normal: 2, 4, 6 (todos pares).
# 2) Borde: 0, 0, 0 (el cero se considera par).
# 3) Error: 10, "hola", 5 (falla al convertir).
# ====================================================================

def problem_4_stats(n1_input, n2_input, n3_input):
    try:
        n1 = int(n1_input)
        n2 = int(n2_input)
        n3 = int(n3_input)
    except ValueError:
        print("Error: invalid input")
        return

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3.0 # Siempre float en Python 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    
    # % 2 == 0 comprueba si es par
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"Sum: {sum_value}")
    print(f"Average: {average_value}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")

print("--- Test Problem 4 ---")
problem_4_stats(2, 4, 6) # Normal
problem_4_stats(0, 0, 0) # Borde
problem_4_stats(10, "hola", 5) # Error
print("\n")


# ====================================================================
# Problema 5: Elegibilidad para préstamo (ingresos vs deudas)
# Descripción: Calcula si te dan un préstamo. Requisitos: ingreso 
# >= 8000, ratio de deuda <= 0.4 y score de crédito >= 650.
#
# Entradas:
# - income_input (float: ingreso mensual)
# - debt_input (float: deuda mensual)
# - score_input (int: puntaje de crédito)
# Salidas:
# - "Debt ratio: <ratio>"
# - "Eligible: true|false"
# Validaciones:
# - Ingreso > 0 (para evitar división por cero).
# - Deuda y Score >= 0.
#
# Casos de prueba:
# 1) Normal: ingreso 10000, deuda 2000, score 700 (Elegible).
# 2) Borde: ingreso 8000, deuda 3200 (ratio 0.4), score 650 (Apenas elegible).
# 3) Error: ingreso 0, deuda 1000 (división por cero) o textos.
# ====================================================================

def problem_5_loan(income_input, debt_input, score_input):
    try:
        monthly_income = float(income_input)
        monthly_debt = float(debt_input)
        credit_score = int(score_input)
    except ValueError:
        print("Error: invalid input")
        return

    # Ingreso debe ser mayor estricto a 0 para no dividir entre 0
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
        return

    debt_ratio = monthly_debt / monthly_income
    
    # Combinación lógica con AND (todas se deben cumplir)
    eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)

    print(f"Debt ratio: {debt_ratio}")
    print(f"Eligible: {str(eligible).lower()}")

print("--- Test Problem 5 ---")
problem_5_loan(10000, 2000, 700) # Normal
problem_5_loan(8000, 3200, 650) # Borde
problem_5_loan(0, 1000, 500) # Error
print("\n")


# ====================================================================
# Problema 6: Índice de Masa Corporal (BMI)
# Descripción: Calcula el BMI de una persona usando peso y altura. 
# Luego prende la bandera (booleano) correspondiente a su categoría.
#
# Entradas:
# - weight_input (float: peso en kg)
# - height_input (float: altura en metros)
# Salidas:
# - "BMI: <valor>", "Underweight: true|false", etc.
# Validaciones:
# - Peso y altura > 0 (altura no puede ser 0 por la división).
#
# Casos de prueba:
# 1) Normal: 75 kg, 1.80 m (Normal).
# 2) Borde: 81 kg, 1.80 m (BMI es 25 exactos, es Overweight).
# 3) Error: peso 70, altura 0 (provocaría división entre cero).
# ====================================================================

def problem_6_bmi(weight_input, height_input):
    try:
        weight_kg = float(weight_input)
        height_m = float(height_input)
    except ValueError:
        print("Error: invalid input")
        return

    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
        return

    # Cálculo
    bmi = weight_kg / (height_m * height_m)
    bmi_rounded = round(bmi, 2)

    # Booleanos dependiendo de la condición
    is_underweight = (bmi < 18.5)
    is_normal = (18.5 <= bmi < 25.0)
    is_overweight = (bmi >= 25.0)

    print(f"BMI: {bmi_rounded}")
    print(f"Underweight: {str(is_underweight).lower()}")
    print(f"Normal: {str(is_normal).lower()}")
    print(f"Overweight: {str(is_overweight).lower()}")

print("--- Test Problem 6 ---")
problem_6_bmi(75, 1.80) # Normal
problem_6_bmi(81, 1.80) # Borde
problem_6_bmi(70, 0) # Error
print("\n")


# ====================================================================
# CONCLUSIONES
# Esta tarea me enseñó que mezclar enteros (int) y flotantes (float) es 
# fundamental en problemas de la vida real, como en nóminas o finanzas. 
# Me quedó súper claro que una simple comparación como > o == se convierte
# automáticamente en un booleano, y eso nos permite tomar decisiones con 'if'. 
# Aprendí por qué las validaciones previas son tan importantes; por ejemplo,
# si no revisamos que la altura o el sueldo sean mayores a cero, el programa 
# fallará por una división matemática imposible. Combinar lógicas con AND/OR
# reduce muchísimo el código en lugar de hacer muchos IFs anidados.
# ====================================================================

# ====================================================================
# REFERENCIAS
# 1) Python documentation - Numeric Types: int, float.
# 2) Python documentation - Boolean Type: bool.
# 3) W3Schools: Python Arithmetic, Relational, and Logical Operators.
# 4) Videos tutoriales en YouTube: Canal "Fazt", curso de Python básico (Tema: Tipos de datos, int, float y booleanos).
# 5) "Aprende con Alf" - Tutorial básico de Python (Tipos de datos y condicionales).
# ====================================================================
