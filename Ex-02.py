internet = float(input('Informe a quantidade de internet consumida: '))
ligacao_local = int(input('Informe a quantidade de ligações local consumida: '))
ligacao_interurbana = int(input('Informe a quantidade de ligações interurbana consumida: '))
torpedo = int(input('Informe a quantidade de torpedos enviados: '))

total_internet = internet * 0.50
total_ligacao_local = ligacao_local * 0.35
total_ligacao_interurbana = ligacao_interurbana * 0.60
total_torpedo = torpedo * 0.20

total_fatura = total_torpedo + total_internet + total_ligacao_local + total_ligacao_interurbana

if internet > 50 and total_internet * 0.95 > total_ligacao_local * 0.90 and total_internet * 0.95 > total_ligacao_interurbana * 0.90\
        and total_internet * 0.95 > total_torpedo * 0.80:
    desconto = total_internet * 0.95
    print("O desconto concedido foi em cima do serviço de Internet.")
elif ligacao_local > 200 and total_ligacao_local * 0.90 > total_ligacao_interurbana * 0.90 and total_ligacao_local * 0.90 > total_torpedo * 0.80:
    desconto = total_ligacao_local * 0.90
    print("O desconto concedido foi em cima do serviço de Ligação Local.")
elif ligacao_interurbana > 150 and total_ligacao_interurbana * 0.90 > total_torpedo * 0.80:
    desconto = total_ligacao_interurbana * 0.90
    print("O desconto concedido foi em cima do serviço de Ligação Interurbana.")
else:
    desconto = total_torpedo * 0.80
    print("O desconto concedido foi em cima do serviço de Torpedos.")

fatura_liquida = total_fatura - desconto

print(f'O total da fatura sem desconto é de R${total_fatura:.2f}.')
print(f'O valor do desconto foi de R$ {desconto:.2f}.')
print(f'O total da fatura com o desconto foi de R$ {fatura_liquida:.2f}.')
