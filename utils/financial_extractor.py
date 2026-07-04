import re

def extract_financial_metrics(text):

    metrics = {
        "Revenue": "Not Found",
        "Net Income": "Not Found"
    }

    revenue_patterns = [
        r"Revenue.*?\$([\d,]+)",
        r"Total Revenue.*?\$([\d,]+)"
    ]

    income_patterns = [
        r"Net income.*?\$([\d,]+)",
        r"Net Income.*?\$([\d,]+)"
    ]

    for pattern in revenue_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            metrics["Revenue"] = "$" + match.group(1)
            break

    for pattern in income_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            metrics["Net Income"] = "$" + match.group(1)
            break

    return metrics