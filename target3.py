import json


with open('dados.json') as file: #Abre o arquivo JSON
    data = json.load(file)

soma = 0
dias = 0
maiorValor = 0
menorValor = 100000
for dados in data: #Percorre os dados para encontrar o maior e menor faturamento e a soma dos valores
    if dados['valor'] != 0:
        soma = soma + dados['valor']
        dias = dias + 1
    if dados['valor'] > maiorValor and dados['valor'] != 0:
        maiorValor = dados['valor']
    if dados['valor'] < menorValor and dados['valor'] != 0:
        menorValor = dados['valor']
media = soma/dias


diasFaturamento = 0
for dados in data: #Calcula em quantos dias o faturamento foi maior que a media mensal
    if dados['valor'] > media:
        diasFaturamento = diasFaturamento + 1

print(f"O maior faturamento foi de {maiorValor:.2f}")
print(f"O menor faturamento foi de {menorValor:.2f}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal = {diasFaturamento}")
file.close()