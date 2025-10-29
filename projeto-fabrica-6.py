def somarImposto(valor,taxa):
    preco_final = valor + (valor*(taxa/100))
    return preco_final

valor = float(input("Digite o valor do produto: "))
taxa = float(input("Digite o valor do imposto: "))
print(somarImposto(valor,taxa))