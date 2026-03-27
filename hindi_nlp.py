import spacy

nlp = spacy.load("xx_ent_wiki_sm")

def process_text(text):
    doc = nlp(text)
    
    tokens = []
    for token in doc:
        if not token.is_punct and not token.is_space:
            tokens.append(token.text)
    
    return tokens