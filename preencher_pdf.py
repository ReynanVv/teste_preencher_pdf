from pdfrw import PdfReader, PdfWriter, PageMerge
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

reader = PdfReader('Modelo_RADOC.pdf')

dados = {
    "semestre": 1,
    "codigo_disciplina": "ABC123",
    "nome_disciplina": "Disciplina 1",
    "ano_e_semestre": "2024/1",
    "curso": "Curso A",
    "nivel": "Graduação",
    "numero_turmas_teorico": 2,
    "numero_turmas_pratico": 1,
    "ch_turmas_teorico": 30.5,
    "ch_turmas_pratico": 15.5,
    "docentes_envolvidos_e_cargas_horarias": {
     "deciola": 40
     }
}

# Mapeamento de cada campo para uma posição (x, y) e número de página
mapeamento = {
    "nome_disciplina": (135, 605, 2),
    "codigo_disciplina": (84, 605, 2),
    # Adicione o restante dos campos aqui
}

lista_textos_coodenadas_paginas = []

for campo, valor in dados.items():
    if campo in mapeamento:
        x, y, pagina = mapeamento[campo]
        texto = str(valor)  # Converta o valor para string
        lista_textos_coodenadas_paginas.append((texto, x, y, pagina))

for texto, x, y, pagina in lista_textos_coodenadas_paginas:
    # Crie um novo PDF com o texto na posição desejada
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(x, y, texto)
    can.save()

    # Mova para o início do StringIO buffer
    packet.seek(0)
    new_pdf = PdfReader(packet)

    # Adiciona o novo PDF à página existente
    merger = PageMerge(reader.pages[pagina - 1])
    merger.add(new_pdf.pages[0]).render()

writer = PdfWriter()
for page in reader.pages:
    writer.addPage(page)

writer.write('Modelo_RADOC.pdf')