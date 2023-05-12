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
    print(f'Os candidatos que irão disputar o segundo turno são:')
    if total_joao < 50:
        print('João')
    if total_pedro < 50:
        print('Pedro')
    if total_paulo < 50:
        print('Paulo')
# Calcula os votos dos candidatos restantes
votos_restantes = total_votos - max(votos_joao, votos_pedro, votos_paulo)
votos_segundo_turno = max(votos_joao, votos_pedro, votos_paulo) - votos_restantes

if votos_joao == votos_segundo_turno:
    print('O segundo turno será disputado entre João e ', end='')
    if votos_pedro > votos_paulo:
        print(f'Pedro, com {total_pedro:.2f}% e {votos_pedro} votos.')
    else:
        print(f'Paulo, com {total_paulo:.2f}% e {votos_paulo} votos.')
elif votos_pedro == votos_segundo_turno:
    print('O segundo turno será disputado entre Pedro e ', end='')
    if votos_joao > votos_paulo:
        print(f'João, com {total_joao:.2f}% e {votos_joao} votos.')
    else:
        print(f'Paulo, com {total_paulo:.2f}% e {votos_paulo} votos.')
else:
    print('O segundo turno será disputado entre Paulo e ', end='')
    if votos_joao > votos_pedro:
        print(f'João, com {total_joao:.2} ')
