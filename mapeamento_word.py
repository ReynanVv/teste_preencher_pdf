from docx import Document

def obter_celulas_vazias(documento):
    celulas_vazias = []
    for tabela_index, tabela in enumerate(documento.tables):
        for row_index, linha in enumerate(tabela.rows):
            for cell_index, célula in enumerate(linha.cells):
                if not célula.text.strip():  # Verifica se a célula está vazia
                    celulas_vazias.append((tabela_index, row_index, cell_index))
    return celulas_vazias

# Carregar o documento existente
documento = Document("Modelo_RADOC.docx")

# Obter as células vazias do documento
celulas_vazias = obter_celulas_vazias(documento)

# Salvar as informações das células vazias em um arquivo de texto
with open("celulas_vazias.txt", "w") as arquivo:
    for tabela_index, row_index, cell_index in celulas_vazias:
        arquivo.write(f"Tabela: {tabela_index + 1}, Linha: {row_index}, Coluna: {cell_index}\n")
