import re

def tokenize(text):
    patterns = {
        "punctuation": r"[.,!?(){}\[\];:'\"।]",
        "date": r"\b(?:\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}-\d{2}-\d{2})\b",
        "url": r"https?://\S+|www\.\S+",
        "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "number": r"\b\d{1,3}(?:,\d{2,3})*(?:\.\d+)?|\b\d+/\d+\b",
        "social_media": r"[@#][\w]+",
        "hindi_word": r"[\u0900-\u097F]+"  
    }

    regex = "|".join(f"(?P<{key}>{value})" for key, value in patterns.items())
    tokens = []

    for match in re.finditer(regex, text):
        for key, value in match.groupdict().items():
            if value:
                tokens.append((key, value))

    return tokens

text = input("Enter text: ")
tokens = tokenize(text)

for token_type, token in tokens:
    print(f"{token_type}: {token}")