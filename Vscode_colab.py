

# Atividade - Par ou ímpar



#numero = int (input("Digite um número:"))




# Exemplo de uso


# Atividade Cálculo de Ímpostos

# Solicitar ao usuário que insira o valor da renda anual
renda_anual = float(input("Insira o valor da sua renda anual: "))

# Inicializar a variável para armazenar o imposto a ser pago
imposto = 0.0

# Estrutura condicional para calcular a alíquota de imposto
if renda_anual <= 22000:
    print("Você está isento de pagar imposto.")
elif 22000 < renda_anual <= 50000:
    imposto = renda_anual * 0.15  # 15% de imposto
    print(f"O valor do imposto a ser pago é: R$ {imposto:.2f}")
else:  # renda_anual > 50000
    imposto = renda_anual * 0.275  # 27.5% de imposto
    print(f"O valor do imposto a ser pago é: R$ {imposto:.2f}")
    
    
lojas = ["Paulo","Pedro","Antonio"]

cont = 0
for loja in lojas:
    cont+=1;
    print(cont)
print("Acabou o For")    
    








