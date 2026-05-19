
def custom_stopwords_removal(text):
    stop_words=['the','in','an','a','are','is']
    lst=text.split(" ")
    txt=[]
    for word in lst:
        if word not in stop_words:
            txt.append(word)
    fin_text=" ".join(txt)
    return fin_text