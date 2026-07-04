# import re

# def find_company_name(text):

#     lines = text.split("\n")

#     for line in lines[:30]:

#         line = line.strip()

#         if len(line) > 5 and len(line) < 80:

#             if any(word in line.lower() for word in
#                    ["inc", "corporation", "corp", "limited", "ltd"]):

#                 return line

#     return "Company Not Found"


# from utils.company_extractor import find_company_name

# text = extract_text(uploaded_file)

# company_name = find_company_name(text)

# st.subheader("Company Information")

# st.metric(
#     "Company Name",
#     company_name
# )

import re

def find_company_name(text):

    lines = text.split("\n")

    keywords = [
        "inc",
        "corporation",
        "corp",
        "limited",
        "ltd",
        "plc"
    ]

    for line in lines[:50]:

        line = line.strip()

        if 5 < len(line) < 100:

            for keyword in keywords:

                if keyword in line.lower():

                    return line

    return "Company Not Found"