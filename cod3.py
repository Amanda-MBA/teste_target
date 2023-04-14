import json

with open('dados.json', 'r') as f:
    dados = json.load(f)

faturamento_diario = [dado['valor'] for dado in dados]
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

dias_acima_da_media = len([valor for valor in faturamento_diario if valor > media_mensal])

print("Menor valor de faturamento diário: R$ {:.2f}".format(menor_valor))
print("Maior valor de faturamento diário: R$ {:.2f}".format(maior_valor))
print("Número de dias acima da média mensal: {}".format(dias_acima_da_media))
