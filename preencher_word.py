from docx import Document

def preencher_tabelas_vazias(documento, dados_por_tabela):
    for tabela_index, tabela in enumerate(documento.tables):
        dados = dados_por_tabela.get(tabela_index + 1, {})  # Obtém os dados para a tabela atual, se existirem
        row_count = len(tabela.rows)
        for row_index in range(row_count):
            linha = tabela.rows[row_index]
            next_row_is_empty = row_index + 1 >= row_count or all(cell.text.strip() == '' for cell in tabela.rows[row_index + 1].cells)
            if next_row_is_empty:
                # Adiciona uma nova linha à tabela antes de preencher a célula
                tabela.add_row()
            for cell_index, celula in enumerate(linha.cells):
                # Verifica se a célula está vazia
                if not celula.text.strip():
                    # Se a posição existir nos dados, preenche a célula
                    posicao = (row_index, cell_index)
                    if posicao in dados:
                        celula.text = dados[posicao]

# Carregar o documento existente
documento = Document("Modelo_RADOC.docx")

# Dados para preencher as tabelas
dados_por_tabela = {
    3: {
        (5, 0): "Valor 1",
        (5, 1): "Valor 2",
        (5, 2): "Valor 3",
        (5, 3): "Valor 4",
        (5, 4): "Valor 5",
        (5, 5): "Valor 6",
        (5, 6): "Valor 7",
        (5, 7): "Valor 8",
        (5, 8): "Valor 9",
        (5, 9): "Valor 10",
        (5, 10): "Valor 11",
        (5, 11): "Valor 12",
        (6, 0): "Valor 13",
        (6, 1): "Valor 14",
        (6, 2): "Valor 15",
        (6, 3): "Valor 16",
        (6, 4): "Valor 17",
        (6, 5): "Valor 18",
        (6, 6): "Valor 19",
        (6, 7): "Valor 20",
        (6, 8): "Valor 21",
        (6, 9): "Valor 22",
        (6, 10): "Valor 23",
        (6, 11): "Valor 24",
        (7, 0): "Valor 25",
        (7, 1): "Valor 26",
        (7, 2): "Valor 27",
        (7, 3): "Valor 28",
        (7, 4): "Valor 29",
        (7, 5): "Valor 30",
        (7, 6): "Valor 31",
        (7, 7): "Valor 32",
        (7, 8): "Valor 33",
        (7, 9): "Valor 34",
        (7, 10): "Valor 35",
        (7, 11): "Valor 36",
        (8, 0): "Valor 37",
        (8, 1): "Valor 38",
        (8, 2): "Valor 39",
        (8, 3): "Valor 40",
        (8, 4): "Valor 41",
        (8, 5): "Valor 42",
        (8, 6): "Valor 43",
        (8, 7): "Valor 44",
        (8, 8): "Valor 45",
        (8, 9): "Valor 46",
        (8, 11): "Valor 47",
    }
}

# Preencher as tabelas vazias com os dados
preencher_tabelas_vazias(documento, dados_por_tabela)

# Salvar o documento modificado
documento.save("documento_modificado.docx")
