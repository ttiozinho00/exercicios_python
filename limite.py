import sympy as sp

# Define a variável x
x = sp.Symbol('x')

# Define a expressão
expression = (x**2 - 4) / (x - 4)

# Calcula o limite
limit_result = sp.limit(expression, x, 2)

# Verifica se há indeterminação
if sp.limit(expression, x, 2, dir='-') == sp.limit(expression, x, 2, dir='+') == limit_result:
    indetermination = "Não há indeterminação"
else:
    indetermination = "Há indeterminação"

print("O limite da função é:", limit_result)
print(indetermination)
