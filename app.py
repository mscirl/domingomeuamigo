import spacy

nlp = spacy.load("pt_core_news_md")

texto = "Estou aprendendo a usar o spacy"

doc = nlp(texto)

for sent in doc.sents:
    print(sent)



# print("=== Tokens e POS Tags ===")
# for token in doc:
#     print(f"Palavra: {token.text:<15} | POS: {token.pos_} | Lemma: {token.lemma_}")

# print("\n=== Entidades Reconhecidas ===")
# for entidade in doc.ents:
#     print(f"Entidade: {entidade.text} | Tipo: {entidade.label_}")