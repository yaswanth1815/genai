import re
def initial_processing(query):
    query=query.lower()
    query=re.sub(r"[^\s\w\d]","",query)
    query=re.sub(r"\s+"," ",query)
    return query