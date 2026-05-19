import re
def light_preprocessing(text):
    text=text.lower()
    text=re.sub(r"\s+"," ",text)
    text=re.sub(r"\.{2,}","",text)
    teext=re.sub(".","",text)
    text=re.sub("[-]"," ",text)
    text=re.sub(r"[•●▪*-,!$():/><]","",text)
    text = re.sub(r"[^a-zA-Z0-9@\s]", "", text)

    return text