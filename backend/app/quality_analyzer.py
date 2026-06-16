import re

def calculate_quality_score(code):
    score = 100
    suggestions = []

    # File size
    if len(code.splitlines()) > 200:
        score -= 10
        suggestions.append("Large file detected. Consider splitting code.")

    # Functions
    functions = len(re.findall(r'def\s+\w+|function\s+\w+', code))

    if functions > 10:
        score -= 10
        suggestions.append("Too many functions in a single file.")

    # Error handling
    if "try:" not in code and "catch" not in code:
        score -= 10
        suggestions.append("Consider adding error handling.")

    # Complexity
    loops = len(re.findall(r'for |while ', code))

    if loops > 5:
        score -= 10
        suggestions.append("High loop complexity detected.")

    return {
        "score": score,
        "suggestions": suggestions
    }