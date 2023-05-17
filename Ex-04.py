curso_idiomas = int(input("Digite o número de horas de Curso de Idiomas: "))
eventos = int(input("Digite o número de horas de Participação em Eventos: "))
visitas_tecnicas = int(input("Digite o número de horas de Visitas Técnicas: "))
cursos_extensao = int(input("Digite o número de horas de Cursos de Extensão: "))

limite_curso_idiomas = 40
limite_eventos = 40
limite_visitas_tecnicas = 20
limite_cursos_extensao = 80

soma_total_horas = curso_idiomas + eventos + visitas_tecnicas + cursos_extensao

horas_validas_curso_idiomas = curso_idiomas
if curso_idiomas > limite_curso_idiomas:
    horas_validas_curso_idiomas = limite_curso_idiomas

horas_validas_eventos = eventos
if eventos > limite_eventos:
    horas_validas_eventos = limite_eventos

horas_validas_visitas_tecnicas = visitas_tecnicas
if visitas_tecnicas > limite_visitas_tecnicas:
    horas_validas_visitas_tecnicas = limite_visitas_tecnicas

horas_validas_cursos_extensao = cursos_extensao
if cursos_extensao > limite_cursos_extensao:
    horas_validas_cursos_extensao = limite_cursos_extensao

soma_total_horas_validas = (
    horas_validas_curso_idiomas
    + horas_validas_eventos
    + horas_validas_visitas_tecnicas
    + horas_validas_cursos_extensao
)

if soma_total_horas_validas >= 100:
    mensagem = "O aluno alcançou o número mínimo de horas necessárias."
else:
    mensagem = "O aluno não alcançou o número mínimo de horas necessárias."

print("Soma total das horas de todas as categorias:", soma_total_horas)
print("Total de horas válidas em Curso de Idiomas:", horas_validas_curso_idiomas)
print("Total de horas válidas em Participação em Eventos:", horas_validas_eventos)
print("Total de horas válidas em Visitas Técnicas:", horas_validas_visitas_tecnicas)
print("Total de horas válidas em Cursos de Extensão:", horas_validas_cursos_extensao)
print("Soma total das horas válidas de todas as categorias:", soma_total_horas_validas)

