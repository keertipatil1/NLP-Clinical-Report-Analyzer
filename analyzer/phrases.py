import spacy

nlp = spacy.load("en_core_web_md")

def extract_key_phrases(text):
    doc = nlp(text)
    return list(set(chunk.text.strip() for chunk in doc.noun_chunks if len(chunk.text.strip()) > 3))
