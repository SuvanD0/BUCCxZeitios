import streamlit as st

def apply_styles():
    """
    Apply custom CSS styles to the Streamlit app
    """
    st.markdown("""
    <style>
    /* Global styles */
    .stApp {
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Headers */
    h1, h2, h3, h4 {
        font-weight: 500;
        color: #2d3748;
    }
    
    /* Form styling */
    .stForm > div[data-testid="stForm"] {
        border: none;
        background-color: #f7fafc;
        border-radius: 8px;
        padding: 1.5rem;
    }
    
    /* Radio buttons (navigation) */
    .stRadio > div {
        display: flex;
        gap: 8px;
        background-color: #f7fafc;
        padding: 8px;
        border-radius: 6px;
    }
    
    /* Prospect card styling */
    .prospect-card {
        background-color: white;
        border-radius: 8px;
        padding: 1.25rem;
        margin: 1rem 0;
        border: 1px solid #edf2f7;
    }
    
    .prospect-card h3 {
        color: #2d3748;
        margin: 0;
        font-size: 1.25rem;
        font-weight: 500;
    }
    
    .prospect-card .title {
        color: #4a5568;
        margin: 0.5rem 0;
        font-size: 1rem;
    }
    
    .prospect-details {
        margin-top: 0.75rem;
        color: #718096;
        font-size: 0.875rem;
    }
    
    /* Button styling */
    .stButton > button {
        border-radius: 6px;
        font-weight: 500;
        transition: all 0.2s;
        border: 1px solid #e2e8f0;
        background-color: #f8fafc;
        color: #2d3748;
    }
    
    .stButton > button[data-testid="baseButton-primary"] {
        background-color: #2d3748;
        color: white;
        border: none;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Text area styling */
    .stTextArea textarea {
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        font-size: 0.875rem;
        line-height: 1.5;
        padding: 0.75rem;
        font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    }
    
    /* Metrics styling */
    [data-testid="stMetricValue"] {
        font-size: 1.25rem;
        color: #2d3748;
    }
    
    /* Link styling */
    a {
        color: #2d3748;
        text-decoration: none;
        font-weight: 500;
    }
    
    a:hover {
        text-decoration: underline;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        background-color: #f7fafc;
        padding: 0.5rem;
        border-radius: 6px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 4px;
        padding: 0.5rem 1rem;
        color: #4a5568;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: white;
        color: #2d3748;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        font-size: 0.875rem;
        color: #4a5568;
    }
    
    /* Info box styling for refined criteria */
    .stAlert {
        border-radius: 6px;
        margin-bottom: 0.75rem;
    }
    
    /* Two-step form styling */
    .stSubheader {
        color: #2d3748;
        margin-bottom: 1rem;
        font-size: 1.1rem;
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        border-radius: 6px;
        border: 1px solid #e2e8f0;
    }
    
    /* General spacing */
    .stContainer {
        margin-bottom: 1.5rem;
    }
    </style>
    """, unsafe_allow_html=True)