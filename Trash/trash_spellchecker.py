# from spellchecker import SpellChecker

# checker=SpellChecker()
# sentence="Taj mahal is beutiful"
# collect=[]
# for word in sentence.split(" "):
#     if word in checker:
#         collect.append(word)
#     else:
#         collect.append(checker.correction(word))
# print(" ".join(collect))

# import spacy

# nlp = spacy.load("en_core_web_sm")

# text = "taj mahal is beatiful"

# doc = nlp(text)

# for ent in doc.ents:
#     print(ent.text, ent.label_)

import spacy
from symspellpy.symspellpy import SymSpell

# -----------------------------
# Load spaCy
# -----------------------------

nlp = spacy.load("en_core_web_sm")

# -----------------------------
# Load SymSpell
# -----------------------------

sym_spell = SymSpell(max_dictionary_edit_distance=2)

dictionary_path = r"Data\frequency_dictionary_en_82_765.txt"

sym_spell.load_dictionary(dictionary_path, 0, 1)

# -----------------------------
# Correction Function
# -----------------------------

def correct_query(text):

    doc = nlp(text)

    corrected_words = []

    for token in doc:

        # Protect nouns and proper nouns
        if token.pos_ in ["PROPN", "NOUN"]:

            corrected_words.append(token.text)

        else:

            suggestions = sym_spell.lookup(
                token.text,
                verbosity=0,
                max_edit_distance=2
            )

            if suggestions:
                corrected_words.append(suggestions[0].term)
            else:
                corrected_words.append(token.text)

    return " ".join(corrected_words)


query = "tej mahel is beatiful"

print(correct_query(query))