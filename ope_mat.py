# Solicitar ao usuário que insira o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Solicitar ao usuário que insira o segundo número
num2 = float(input("Digite o segundo número: "))

# Solicitar ao usuário que escolha uma operação
operacao = input("Escolha uma operação (+, -, *, /): ")

# Realizar a operação escolhida
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero!"
else:
    resultado = "Operação inválida!"

# Exibir o resultado
print("O resultado da operação é:", resultado)
