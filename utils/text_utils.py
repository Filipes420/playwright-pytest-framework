import re

def clean_text(text: str):
    ## removes all special chars

    return re.sub(r'[^A-Za-z0-9]', '', text)