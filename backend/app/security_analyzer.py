import re

def analyze_security(code):
    risks = []

    if "password =" in code:
        risks.append("Hardcoded password detected")

    if "api_key" in code.lower():
        risks.append("API key exposed")

    if "eval(" in code:
        risks.append("Use of eval() detected")

    return {
        "risk_count": len(risks),
        "risks": risks
    }