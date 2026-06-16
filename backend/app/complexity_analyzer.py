import re

def analyze_complexity(code):
    functions = len(re.findall(r'def\s+\w+|function\s+\w+', code))
    loops = len(re.findall(r'for |while ', code))

    score = functions * 5 + loops * 3

    return {
        "complexity_score": score,
        "functions": functions,
        "loops": loops
    }