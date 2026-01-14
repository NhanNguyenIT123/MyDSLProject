class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"{self.type}:{self.value}"
    

KEYWORDS = {
    "start": "START",
    "finish": "FINISH",
    "feature": "FEATURE",
    "push": "PUSH",
    "pull": "PULL",
    "status": "STATUS",
    "stage": "STAGE",
    "all": "ALL",
    "commit": "COMMIT",
    "log": "LOG"
}

def tokenize(code):
    tokens = []
    words = code.strip().split()

    for word in words:
        if word.lower() in KEYWORDS:
            tokens.append(Token(KEYWORDS[word.lower()], word))
        else:
            tokens.append(Token("IDENTIFIER", word))

    return tokens