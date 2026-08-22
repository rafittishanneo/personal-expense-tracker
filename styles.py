import streamlit as st


def inject_custom_css():
    st.markdown(
        """
        <style>

        /* ---------------------------------------------------
           GLOBAL
        --------------------------------------------------- */

        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont,
                         'Segoe UI', sans-serif;
        }

        .block-container {
            padding-top: 2.2rem;
            padding-bottom: 3rem;
        }

        /* subtle scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-thumb {
            background: #1F2937;
            border-radius: 8px;
        }
        ::-webkit-scrollbar-track {
            background: transparent;
        }

        /* ---------------------------------------------------
           SIDEBAR
        --------------------------------------------------- */

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0F172A 0%, #0B1120 100%);
            border-right: 1px solid #1F2937;
        }

        section[data-testid="stSidebar"] h1 {
            font-size: 1.35rem;
            font-weight: 700;
            letter-spacing: -0.02em;
        }

        /* radio nav -> pill style buttons */
        section[data-testid="stSidebar"] div[role="radiogroup"] label {
            background: transparent;
            border-radius: 10px;
            padding: 0.55rem 0.9rem;
            margin-bottom: 0.15rem;
            transition: background 0.15s ease;
            width: 100%;
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
            background: rgba(45, 212, 191, 0.08);
        }

        /* ---------------------------------------------------
           TITLES / CAPTIONS
        --------------------------------------------------- */

        h1 {
            font-weight: 800 !important;
            letter-spacing: -0.03em;
        }

        h2, h3 {
            font-weight: 700 !important;
            letter-spacing: -0.02em;
        }

        [data-testid="stCaptionContainer"] {
            color: #9CA3AF !important;
        }

        /* ---------------------------------------------------
           CARD WRAPPER
           Wrap any block in <div class="app-card"> ... </div>
        --------------------------------------------------- */

        .app-card {
            background: #111827;
            border: 1px solid #1F2937;
            border-radius: 16px;
            padding: 1.4rem 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
        }

        .app-card-tight {
            background: #111827;
            border: 1px solid #1F2937;
            border-radius: 14px;
            padding: 1rem 1.2rem;
            margin-bottom: 0.75rem;
        }

        /* ---------------------------------------------------
           METRIC CARDS (dashboard summary)
        --------------------------------------------------- */

        div[data-testid="stMetric"] {
            background: #111827;
            border: 1px solid #1F2937;
            border-radius: 16px;
            padding: 1.1rem 1.3rem 1rem 1.3rem;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
        }

        div[data-testid="stMetricLabel"] {
            font-weight: 600;
            color: #9CA3AF !important;
        }

        div[data-testid="stMetricValue"] {
            font-weight: 800 !important;
            letter-spacing: -0.02em;
        }

        /* ---------------------------------------------------
           BUTTONS
        --------------------------------------------------- */

        .stButton > button, .stFormSubmitButton > button {
            border-radius: 10px !important;
            font-weight: 600 !important;
            border: 1px solid #1F2937 !important;
            transition: transform 0.08s ease, border-color 0.15s ease;
        }

        .stFormSubmitButton > button {
            background: #2DD4BF !important;
            color: #0B1120 !important;
            border: none !important;
        }

        .stFormSubmitButton > button:hover {
            transform: translateY(-1px);
            filter: brightness(1.05);
        }

        .stButton > button:hover {
            border-color: #2DD4BF !important;
            color: #2DD4BF !important;
        }

        /* ---------------------------------------------------
           INPUTS
        --------------------------------------------------- */

        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        .stNumberInput > div > div,
        .stDateInput > div > div {
            background: #0B1120 !important;
            border-radius: 10px !important;
            border: 1px solid #1F2937 !important;
        }

        /* ---------------------------------------------------
           STATUS PILLS (success / error / warning / info)
        --------------------------------------------------- */

        div[data-testid="stAlertContentSuccess"],
        div[data-testid="stAlertContentError"],
        div[data-testid="stAlertContentWarning"],
        div[data-testid="stAlertContentInfo"] {
            border-radius: 10px !important;
            font-weight: 600 !important;
        }

        /* ---------------------------------------------------
           DIVIDERS
        --------------------------------------------------- */

        hr {
            border-color: #1F2937 !important;
            margin: 1.6rem 0 !important;
        }

        /* ---------------------------------------------------
           PROGRESS BAR (budgets)
        --------------------------------------------------- */

        div[data-testid="stProgress"] > div > div {
            background-color: #1F2937 !important;
            border-radius: 8px !important;
        }

        div[data-testid="stProgress"] > div > div > div {
            border-radius: 8px !important;
        }

        /* ---------------------------------------------------
           DATAFRAME
        --------------------------------------------------- */

        [data-testid="stDataFrame"] {
            border-radius: 12px !important;
            overflow: hidden;
            border: 1px solid #1F2937 !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
