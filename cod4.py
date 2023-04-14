string = "Hello World"

# Invertendo a string
string_invertida = ""
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

# Exibindo o resultado
print(string_invertida)
