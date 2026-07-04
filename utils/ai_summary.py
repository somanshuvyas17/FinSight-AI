# import subprocess

# def generate_summary(text):

#     prompt = f"""
#     Summarize this annual report.

#     Include:
#     - Business performance
#     - Major risks
#     - Overall outlook

#     Annual Report:
#     {text[50000:55000]}
#     """

#     try:

#         result = subprocess.run(
#             ["ollama", "run", "llama3.2"],
#             input=prompt,
#             capture_output=True,
#             text=True,
#             encoding="utf-8",      # ← THIS FIXES IT
#             errors="ignore",       # ← Ignore problematic characters
#             timeout=180
#         )

#         return result.stdout.strip()

#     except Exception as e:

#         return f"Error generating summary:\n{str(e)}"


# def generate_summary(text):
#     return "🔥 AI Summary Function Was Called Successfully!"



import ollama

def generate_summary(text):

    prompt = f"""
    You are a financial analyst.

    Summarize the following annual report.

    Include:

    • Company overview

    • Financial performance

    • Key risks

    • Future outlook

    Report:

    {text[:5000]}
    """

    response = ollama.chat(
        model="llama3.2:latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


    