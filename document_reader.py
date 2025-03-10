import spacy

from pathlib import Path
from docling import Document
from typing import Optional

class DocumentReader:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.text = None
        self.nlp = spacy.load("pt_core_news_md")
    
    def exists(self) -> bool:
        return self.file_path.exists()
    
    def read(self) -> Optional[str]:
        """Lendo o documento e extraindo o texto"""
        try:
            doc = Document(self.file_path)
            self.text = doc.extract_text()
            return self.text
        except Exception as e:
            print(f"Erro ao ler o arquivo {e}")
            return None
        
    def process_text(self) -> dict:
        """Processando o texto"""
        if not self.text:
            return{}
        
        doc = self.nlp(self.text)
        return {
            "personagens": list(set(ent.text for ent in doc.ents if ent.label_ == "PER")),
            "locais": list(set(ent.text for ent in doc.ents if ent.label_ == "LOC")),
            "data": list(set(ent.text for ent in doc.ents if ent.label_ == "DATE")),
        }
