consumo = float(input("Digite o consumo em m³: "))

taxa_basica = 34.49
valor_faixa1 = 1.07
valor_faixa2 = 5.94
valor_faixa3 = 5.97
valor_faixa4 = 6.02
valor_faixa5 = 10.19

valor_total = taxa_basica

if consumo > 5:
    if 6 <= consumo <= 10:
        valor_total += (consumo - 5) * valor_faixa1
    elif 11 <= consumo <= 15:
        valor_total += 5 * valor_faixa1 + (consumo - 10) * valor_faixa2
    elif 16 <= consumo <= 20:
        valor_total += 5 * valor_faixa1 + 5 * valor_faixa2 + (consumo - 15) * valor_faixa3
    elif 21 <= consumo <= 30:
        valor_total += 5 * valor_faixa1 + 5 * valor_faixa2 + 5 * valor_faixa3 + (consumo - 20) * valor_faixa4
    else:
        valor_total += 5 * valor_faixa1 + 5 * valor_faixa2 + 5 * valor_faixa3 + 10 * valor_faixa4 + (consumo - 30) * valor_faixa5

print("O valor total da fatura é: R$", valor_total)
