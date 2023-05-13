# 1) Numa eleição para presidente concorrem 3 candidatos: João, Pedro e Paulo. Sabendo que
# para que um presidente seja eleito no primeiro turno, o mesmo deve conquistar um total de
# votos superior a 50%, desenvolver um programa que:
# a) Indique o percentual de votos de cada candidato na eleição.
# b) Indique se houve vencedor em primeiro turno, e qual o vencedor
# c) Indique se houve a necessidade de realização de segundo turno, e quais serão os
# candidatos a disputá-lo

votos_joao = int(input('Informe a quantidade de votos em que João recebeu: '))
votos_pedro = int(input('Informe a quantidade de votos em que Pedro recebeu: '))
votos_paulo = int(input('Informe a quantidade de votos em que Paulo recebeu: '))

total_votos = votos_pedro + votos_joao + votos_paulo

total_joao = (votos_joao / total_votos) * 100
total_pedro = (votos_pedro / total_votos) * 100
total_paulo = (votos_paulo / total_votos) * 100

print(f'O percentual de votos nessa eleição foi de: João {total_joao:.2f}%, Pedro {total_pedro:.2f}%, Paulo {total_paulo:.2f}%.')

if total_joao > 50:
    print(f'Houve vencedor no primeiro turno, portanto João é o vencedor das eleições com {total_joao:.2f}% dos votos.')
elif total_pedro > 50:
    print(f'Houve vencedor no primeiro turno, portanto Pedro é o vencedor das eleições com {total_pedro:.2f}% dos votos.')
elif total_paulo > 50:
    print(f'Houve vencedor no primeiro turno, portanto Paulo é o vencedor das eleições com {total_paulo:.2f}% dos votos.')
else:
    print('Nenhum candidato recebeu mais de 50% dos votos, portanto haverá segundo turno.')

    if total_joao > total_pedro and total_joao > total_paulo:
        print('João irá disputar o segundo turno.')
        if total_pedro > total_paulo:
            print('Pedro também irá disputar o segundo turno.')
        else:
            print('Paulo também irá disputar o segundo turno.')

    elif total_pedro > total_joao and total_pedro > total_paulo:
        print('Pedro irá disputar o segundo turno.')
        if total_paulo > total_joao:
            print('Paulo também irá disputar o segundo turno.')
        else:
            print('João também irá disputar o segundo turno.')

    else:
        print('Paulo irá disputar o segundo turno.')
        if total_pedro > total_joao:
            print('Pedro também irá disputar o segundo turno.')
        else:
            print('João também irá disputar o segundo turno.')
