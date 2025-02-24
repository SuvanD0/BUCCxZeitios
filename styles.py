import streamlit as st

def apply_styles():
    """
    Apply custom CSS styles to the Streamlit app
    """
    st.markdown("""
        <style>
        /* Main container */
        .main {
            padding: 2rem;
        }

        /* Headers */
        .title {
            color: #6c757d; /* Changed to grey */
            font-weight: 600;
        }

        /* Form styling */
        .stForm {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        /* Input fields */
        .stTextInput {
            border: 1px solid #e1e1e1;
            border-radius: 5px;
        }

        /* Submit button */
        .stButton>button {
            background-color: #6c757d; /* Changed to grey */
            color: white;
            font-weight: 600;
            padding: 0.5rem 2rem;
            border-radius: 5px;
        }

        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }

        .stTabs [data-baseweb="tab"] {
            background-color: #f8f9fa;
            border-radius: 4px;
            color: #6c757d; /* Changed to grey */
            padding: 8px 16px;
        }

        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background-color: #6c757d; /* Changed to grey */
            color: white;
        }

        /* Text area styling */
        .stTextArea textarea {
            border: 1px solid #e1e1e1;
            border-radius: 5px;
            font-family: 'Inter', sans-serif;
            padding: 10px;
        }

        /* Success messages */
        .success {
            background-color: #ecfdf3;
            color: #027a48;
            padding: 1rem;
            border-radius: 5px;
        }

        /* Error messages */
        .error {
            background-color: #fef3f2;
            color: #b42318;
            padding: 1rem;
            border-radius: 5px;
        }

        /* Loading spinner */
        .stSpinner {
            color: #6c757d; /* Changed to grey */
        }

        /* Card styling */
        div[data-testid="stExpander"] {
            background-color: white;
            border-radius: 10px;
            border: 1px solid #e1e1e1;
            margin-bottom: 1rem;
        }

        div[data-testid="stExpander"] > div:first-child {
            background-color: #f8f9fa;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            padding: 1rem;
        }
        /* DataFrames */
        .dataframe {
            font-family: 'Inter', sans-serif;
            border-collapse: collapse;
            width: 100%;
        }

        .dataframe th {
            background-color: #f8f9fa;
            font-weight: 600;
            text-align: left;
            padding: 12px;
        }

        .dataframe td {
            padding: 12px;
            border-bottom: 1px solid #e1e1e1;
        }
        </style>
    """, unsafe_allow_html=True)