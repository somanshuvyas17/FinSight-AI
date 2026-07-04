import re

def extract_risk_factors(text):

    risk_keywords = [
        "risk",
        "uncertainty",
        "competition",
        "cybersecurity",
        "regulation",
        "economic"
    ]

    risks = []

    sentences = re.split(r'(?<=[.!?])\s+', text)

    for sentence in sentences:

        sentence = sentence.strip()

        if len(sentence) > 50 and len(sentence) < 300:

            for keyword in risk_keywords:

                if keyword.lower() in sentence.lower():

                    risks.append(sentence)
                    break

        if len(risks) >= 5:
            break

    return risks