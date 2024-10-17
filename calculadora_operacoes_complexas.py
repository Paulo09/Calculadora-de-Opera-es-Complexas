# Solicitar ao usuário dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Perguntar ao usuário qual operação deseja realizar
operacao = input("Escolha a operação (soma, subtração, multiplicação, divisão, exponenciação): ").lower()

# Usar estruturas condicionais para realizar a operação escolhida
if operacao == "soma":
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")

elif operacao == "subtração":
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")

elif operacao == "multiplicação":
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")

elif operacao == "divisão":
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida!")

elif operacao == "exponenciação":
    resultado = num1 ** num2
    print(f"O resultado da exponenciação é: {resultado}")

else:
    print("Operação inválida! Por favor, escolha entre soma, subtração, multiplicação, divisão, ou exponenciação.")
