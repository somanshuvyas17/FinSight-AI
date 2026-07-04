# import streamlit as st
# import pandas as pd
# import plotly.express as px

# from utils.pdf_parser import extract_text
# from utils.company_extractor import find_company_name
# from utils.financial_extractor import extract_financial_metrics
# from utils.risk_extractor import extract_risk_factors
# from utils.ai_summary import generate_summary


# st.set_page_config(
#     page_title="AI Financial Analyst Assistant",
#     page_icon="📈",
#     layout="wide"
# )


# def convert_to_number(value):

#     try:
#         return float(
#             value.replace("$", "").replace(",", "")
#         )

#     except:
#         return 0


# st.title("📈 AI Financial Analyst Assistant")

# uploaded_file = st.file_uploader(
#     "Upload Annual Report PDF",
#     type="pdf"
# )


# if uploaded_file:

#     text = extract_text(uploaded_file)

#     company_name = find_company_name(text)

#     financials = extract_financial_metrics(text)

#     risks = extract_risk_factors(text)

#     summary = generate_summary(text)    

#     revenue = convert_to_number(
#         financials["Revenue"]
#     )

#     net_income = convert_to_number(
#         financials["Net Income"]
#     )

#     chart_data = pd.DataFrame({
#         "Metric": [
#             "Revenue",
#             "Net Income"
#         ],
#         "Amount": [
#             revenue,
#             net_income
#         ]
#     })

#     st.success("PDF Loaded Successfully!")

#     tab1, tab2, tab3, tab4 = st.tabs(
#         [
#             "Overview",
#             "Risk Analysis",
#             "Document Text",
#             "AI Summary"
#         ]
#     )

#     with tab1:

#         st.subheader("🏢 Company Information")

#         st.metric(
#             "Company Name",
#             company_name
#         )

#         st.subheader("💰 Financial Metrics")

#         col1, col2 = st.columns(2)

#         with col1:
#             st.metric(
#                 "Revenue",
#                 financials["Revenue"]
#             )

#         with col2:
#             st.metric(
#                 "Net Income",
#                 financials["Net Income"]
#             )

#         st.subheader("📊 Document Statistics")

#         col1, col2 = st.columns(2)

#         with col1:
#             st.metric(
#                 "Characters",
#                 len(text)
#             )

#         with col2:
#             st.metric(
#                 "Words",
#                 len(text.split())
#             )

#         st.subheader("\n📈 Financial Dashboard")

#         fig = px.bar(
#             chart_data,
#             x="Metric",
#             y="Amount",
#             title="Financial Metrics"
#         )

#         st.plotly_chart(
#             fig,
#             width="stretch"
#         )

#     with tab2:

#         st.subheader("⚠️ Key Risk Factors")

#         if risks:

#             for i, risk in enumerate(risks, start=1):

#                 st.write(
#                     f"{i}. {risk}"
#                 )

#         else:

#             st.warning(
#                 "No risk factors detected."
#             )

#     with tab3:

#         st.text_area(
#             "Extracted Text",
#             text[:10000],
#             height=500
#         )

#     with tab3:

#     st.subheader("🤖 AI Executive Summary")

#     with st.spinner("🔍 AI is analyzing the annual report..."):

#         summary = generate_summary(text)

#     st.markdown(summary)

# else:

#     st.info(
#         "Upload an annual report PDF to begin analysis."
#     )







import streamlit as st
import pandas as pd
import plotly.express as px

from utils.pdf_parser import extract_text
from utils.company_extractor import find_company_name
from utils.financial_extractor import extract_financial_metrics
from utils.risk_extractor import extract_risk_factors
from utils.ai_summary import generate_summary


# ------------------------
# PAGE CONFIG
# ------------------------

st.set_page_config(
    page_title="FinSight AI",
    page_icon="📈",
    layout="wide"
)

st.title("📈 FinSight AI")
st.caption("AI-Powered Financial Report Analyzer")


# ------------------------
# HELPER FUNCTION
# ------------------------

def convert_to_number(value):
    try:
        return float(
            value.replace("$", "").replace(",", "")
        )
    except:
        return 0


# ------------------------
# FILE UPLOAD
# ------------------------

uploaded_file = st.file_uploader(
    "Upload Annual Report (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    with st.spinner("Extracting PDF..."):

        text = extract_text(uploaded_file)

    company_name = find_company_name(text)

    financials = extract_financial_metrics(text)

    risks = extract_risk_factors(text)

    revenue = convert_to_number(
        financials["Revenue"]
    )

    net_income = convert_to_number(
        financials["Net Income"]
    )

    chart_data = pd.DataFrame({
        "Metric": [
            "Revenue",
            "Net Income"
        ],
        "Amount": [
            revenue,
            net_income
        ]
    })

    st.success("PDF Loaded Successfully!")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📊 Overview",
            "⚠️ Risk Analysis",
            "🤖 AI Summary",
            "📄 Document Text"
        ]
    )

    # ===================================
    # TAB 1
    # ===================================

    with tab1:

        st.subheader("🏢 Company Information")

        st.metric(
            "Company",
            company_name
        )

        st.divider()

        st.subheader("💰 Financial Metrics")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Revenue",
                financials["Revenue"]
            )

        with col2:
            st.metric(
                "Net Income",
                financials["Net Income"]
            )

        st.divider()

        st.subheader("📑 Document Statistics")

        col3, col4 = st.columns(2)

        with col3:
            st.metric(
                "Characters",
                len(text)
            )

        with col4:
            st.metric(
                "Words",
                len(text.split())
            )

        st.divider()

        st.subheader("📈 Financial Dashboard")

        fig = px.bar(
            chart_data,
            x="Metric",
            y="Amount",
            color="Metric",
            text="Amount",
            title="Financial Metrics"
        )

        fig.update_layout(
            height=450
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # ===================================
    # TAB 2
    # ===================================

    with tab2:

        st.subheader("⚠️ Key Risk Factors")

        if risks:

            for i, risk in enumerate(risks, start=1):

                st.markdown(
                    f"**{i}.** {risk}"
                )

        else:

            st.info(
                "No risk factors detected."
            )

    # ===================================
    # TAB 3
    # ===================================

    with tab3:

        st.subheader("🤖 AI Executive Summary")

        with st.spinner("AI is analyzing the report..."):

            try:

                summary = generate_summary(text)

                st.markdown(summary)

            except Exception as e:

                st.error(
                    f"AI Error: {e}"
                )

    # ===================================
    # TAB 4
    # ===================================

    with tab4:

        st.subheader("📄 Extracted Document")

        st.text_area(
            "Extracted Text",
            text[:10000],
            height=600
        )

else:

    st.info(
        "Upload an Annual Report PDF to begin analysis."
    )