import spacy
method=spacy.load("en_core_web_sm")

def data_lemmatise(text):
    text=method(text)
    lst=[]
    for token in text:
        lst.append(token.lemma_)
    return " ".join(lst)