# Exemplo de uso de métodos de string em Python

# Definindo uma string
texto = "    Olá, Mundo!    "

# Métodos de string
# 1. strip(): Remove espaços em branco no início e no final da string
texto_stripped = texto.strip()

# 2. lower(): Converte a string para minúsculas
texto_lower = texto.lower()

# 3. upper(): Converte a string para maiúsculas
texto_upper = texto.upper()

# 4. replace(): Substitui uma substring por outra
texto_replace = texto.replace("Mundo", "Python")

# 5. split(): Divide a string em uma lista usando um delimitador
palavras = texto.split()

# 6. find(): Retorna o índice da primeira ocorrência de uma substring (ou -1 se não encontrar)
indice = texto.find("Mundo")

# 7. count(): Retorna o número de ocorrências de uma substring na string
contagem = texto.count("o")

# Exibindo os resultados
print("Original:", texto)
print("Stripped:", texto_stripped)
print("Lowercased:", texto_lower)
print("Uppercased:", texto_upper)
print("Replaced:", texto_replace)
print("Split into words:", palavras)
print("Index of 'Mundo':", indice)
print("Count of 'o':", contagem)
