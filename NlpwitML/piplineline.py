import pandas as pd
import spacy

nlp=spacy.load("en_core_web_sm")

#helper fuctions 

def lower_remove(series):
    output=series.str.lower()
    output=output.str.replace(r'\[.*?\]', '', regex=True)
    output=output.str.replace(r'[^\w\s]', '', regex=True)
    return output


def token_lemma(series):
    doc=nlp(series)
    output=[token.lemma_ for token in doc if not token.is_stop]
    return ' '.join(output)


def clean_and_normilize(series):
    output=lower_remove(series)
    output=output.apply(token_lemma)
    return output

if __name__=="__main__":
    print("Text preprocessing module ready to use")
                              
    