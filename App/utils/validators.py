import re

def isValidEmail(text : str) -> bool:
    pattern : str = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, text) is not None

