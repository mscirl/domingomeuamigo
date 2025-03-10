import sys
import os
from document_reader import DocumentReader
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

# Variável para indicar o arquivo a ser testado
file_test = Path("stories/hissing, wagging, dripping.pdf")


# Função para testar a extração de dados do arquivo
def test_extraction():
    reader = DocumentReader(file_test)
    reader.read()
    result = reader.process_text()
    
    assert result["personagens"] == ["Jungkook", "Taehyung."]
    assert result["locais"] == ["Armazém", "Porto"]
    assert ["2023"] in result["data"], "Data não encontrada"