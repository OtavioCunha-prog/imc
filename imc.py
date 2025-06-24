# Função para calcular o IMC e classificar
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return imc, "baixo peso"
    elif 18.5 <= imc < 24.9:
        return imc, "peso adequado"
    elif 25 <= imc < 29.9:
        return imc, "sobrepeso"
    elif 30 <= imc < 34.9:
        return imc, "obesidade grau I"
    elif 35 <= imc < 39.9:
        return imc, "obesidade grau II"
    else:
        return imc, "obesidade grau III"

# Coleta de dados do usuário
try:
    peso = float(input("Digite seu peso em kg (ex: 70.2): "))
    altura = float(input("Digite sua altura em metros (ex: 1.80): "))
except ValueError:
    print("Por favor, insira números válidos para peso e altura.")
    exit(1)

imc_valor, classificacao = calcular_imc(peso, altura)
print(f"Seu IMC é: {imc_valor:.2f}, e isso indica: {classificacao}")
