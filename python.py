import numpy as np
a = np.array([10, 20, 30])
b = np.array([1, 2, 5])
result_op = a + b
result_func = np.add(a, b)
print(f"Addition (operator): {result_op}") 
print(f"Addition (function): {result_func}") 
result_op1 = a - b
result_func1 = np.subtract(a, b)
print(f"Subtraction (operator): {result_op1}") 
print(f"Subtraction (function): {result_func1}") 
result_op2 = a * b
result_func2 = np.multiply(a, b)
print(f"Multiplication (operator): {result_op2}")
print(f"Multiplication (function): {result_func2}") 
result_op3 = a / b
result_func3 = np.divide(a, b)
print(f"Division (operator): {result_op3}") 
print(f"Division (function): {result_func3}") 