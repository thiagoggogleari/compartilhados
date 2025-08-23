# 7. Peça ao usuário um ano e informe se ele é bissexto

# Para ser bisexto o ano deve ser divisível por 4 exceto em anos centenários, divisíveis por 100

ano = int(input("Insira um ano e vou verificar se ele é bisexto: "))

if((ano % 100 == 0) or (ano % 4 == 0)):
    print("O ano %i não é um ano bisexto"%(ano))
else:
    print("O ano %i é um ano bisexto"%(ano))
