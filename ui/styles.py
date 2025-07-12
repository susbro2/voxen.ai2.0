"""
Custom styles and theming for the AI Math Chat System
"""

import streamlit as st
from config.settings import UI_CONFIG

def apply_custom_css():
    """Apply custom CSS styles to the Streamlit app"""
    
    # Custom CSS for better styling
    custom_css = """
    <style>
    /* Main container styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Header styling */
    .main h1 {
        color: #FF6B6B;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .main h2 {
        color: #4A90E2;
        font-weight: 600;
        margin-bottom: 0.8rem;
    }
    
    .main h3 {
        color: #7B68EE;
        font-weight: 500;
        margin-bottom: 0.6rem;
    }
    
    /* Chat message styling */
    .stChatMessage {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        border-left: 4px solid #FF6B6B;
    }
    
    .stChatMessage[data-testid="chatMessage"] {
        background-color: #e3f2fd;
        border-left-color: #4A90E2;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #FF6B6B;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #FF5252;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* Input field styling */
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        padding: 0.5rem;
        transition: border-color 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #FF6B6B;
        box-shadow: 0 0 0 2px rgba(255, 107, 107, 0.2);
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div > select {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        padding: 0.5rem;
    }
    
    /* Metric styling */
    .stMetric {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 1rem;
        border: 1px solid #e0e0e0;
    }
    
    .stMetric > div > div > div {
        color: #FF6B6B;
        font-weight: bold;
    }
    
    /* Success message styling */
    .stSuccess {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 8px;
        padding: 1rem;
        color: #155724;
    }
    
    /* Error message styling */
    .stError {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        border-radius: 8px;
        padding: 1rem;
        color: #721c24;
    }
    
    /* Info message styling */
    .stInfo {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 8px;
        padding: 1rem;
        color: #0c5460;
    }
    
    /* Warning message styling */
    .stWarning {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 8px;
        padding: 1rem;
        color: #856404;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #f8f9fa;
    }
    
    .css-1d391kg .sidebar-content {
        padding: 1rem;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 0.5rem;
        font-weight: 500;
    }
    
    /* Code block styling */
    .stCodeBlock {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 1rem;
        border: 1px solid #e0e0e0;
    }
    
    /* Plotly chart styling */
    .js-plotly-plot {
        border-radius: 8px;
        overflow: hidden;
    }
    
    /* Custom card styling */
    .custom-card {
        background-color: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border: 1px solid #e0e0e0;
        margin-bottom: 1rem;
    }
    
    /* Math expression styling */
    .math-expression {
        background-color: #f8f9fa;
        border: 1px solid #e0e0e0;
        border-radius: 6px;
        padding: 0.5rem;
        font-family: 'Courier New', monospace;
        font-size: 1.1em;
    }
    
    /* Loading spinner styling */
    .stSpinner > div {
        border-color: #FF6B6B;
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div {
        background-color: #FF6B6B;
    }
    
    /* File uploader styling */
    .stFileUploader > div > div {
        border-radius: 8px;
        border: 2px dashed #e0e0e0;
        padding: 2rem;
        text-align: center;
    }
    
    .stFileUploader > div > div:hover {
        border-color: #FF6B6B;
        background-color: #f8f9fa;
    }
    
    /* Dark theme overrides */
    @media (prefers-color-scheme: dark) {
        .main {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        
        .stChatMessage {
            background-color: #262730;
            border-left-color: #FF6B6B;
        }
        
        .stChatMessage[data-testid="chatMessage"] {
            background-color: #1E1E2E;
            border-left-color: #4A90E2;
        }
        
        .stTextInput > div > div > input {
            background-color: #262730;
            border-color: #404040;
            color: #FAFAFA;
        }
        
        .stSelectbox > div > div > select {
            background-color: #262730;
            border-color: #404040;
            color: #FAFAFA;
        }
        
        .stMetric {
            background-color: #262730;
            border-color: #404040;
        }
        
        .custom-card {
            background-color: #262730;
            border-color: #404040;
        }
        
        .math-expression {
            background-color: #1E1E2E;
            border-color: #404040;
            color: #FAFAFA;
        }
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem;
        }
        
        .custom-card {
            padding: 1rem;
        }
        
        .stButton > button {
            width: 100%;
            margin-bottom: 0.5rem;
        }
    }
    
    /* Animation for smooth transitions */
    * {
        transition: all 0.3s ease;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #FF6B6B;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #FF5252;
    }
    
    /* Focus indicators for accessibility */
    .stButton > button:focus,
    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        outline: 2px solid #FF6B6B;
        outline-offset: 2px;
    }
    
    /* Print styles */
    @media print {
        .sidebar,
        .stButton,
        .stFileUploader {
            display: none !important;
        }
        
        .main {
            margin: 0 !important;
            padding: 0 !important;
        }
    }
    </style>
    """
    
    st.markdown(custom_css, unsafe_allow_html=True)

def apply_dark_theme():
    """Apply dark theme specific styles"""
    dark_css = """
    <style>
    /* Dark theme specific overrides */
    .main {
        background-color: #0E1117 !important;
        color: #FAFAFA !important;
    }
    
    .stApp {
        background-color: #0E1117 !important;
    }
    
    .stChatMessage {
        background-color: #262730 !important;
        color: #FAFAFA !important;
    }
    
    .stTextInput > div > div > input {
        background-color: #262730 !important;
        color: #FAFAFA !important;
        border-color: #404040 !important;
    }
    
    .stSelectbox > div > div > select {
        background-color: #262730 !important;
        color: #FAFAFA !important;
        border-color: #404040 !important;
    }
    
    .stMetric {
        background-color: #262730 !important;
        border-color: #404040 !important;
    }
    
    .stMetric > div > div > div {
        color: #FF6B6B !important;
    }
    
    .stExpander {
        background-color: #262730 !important;
        border-color: #404040 !important;
    }
    
    .streamlit-expanderHeader {
        background-color: #262730 !important;
        color: #FAFAFA !important;
    }
    
    .stCodeBlock {
        background-color: #1E1E2E !important;
        border-color: #404040 !important;
        color: #FAFAFA !important;
    }
    
    .custom-card {
        background-color: #262730 !important;
        border-color: #404040 !important;
        color: #FAFAFA !important;
    }
    
    .math-expression {
        background-color: #1E1E2E !important;
        border-color: #404040 !important;
        color: #FAFAFA !important;
    }
    </style>
    """
    
    st.markdown(dark_css, unsafe_allow_html=True)

def apply_light_theme():
    """Apply light theme specific styles"""
    light_css = """
    <style>
    /* Light theme specific overrides */
    .main {
        background-color: #FFFFFF !important;
        color: #262730 !important;
    }
    
    .stApp {
        background-color: #FFFFFF !important;
    }
    
    .stChatMessage {
        background-color: #F0F2F6 !important;
        color: #262730 !important;
    }
    
    .stTextInput > div > div > input {
        background-color: #FFFFFF !important;
        color: #262730 !important;
        border-color: #E0E0E0 !important;
    }
    
    .stSelectbox > div > div > select {
        background-color: #FFFFFF !important;
        color: #262730 !important;
        border-color: #E0E0E0 !important;
    }
    
    .stMetric {
        background-color: #F8F9FA !important;
        border-color: #E0E0E0 !important;
    }
    
    .stMetric > div > div > div {
        color: #FF6B6B !important;
    }
    
    .stExpander {
        background-color: #F8F9FA !important;
        border-color: #E0E0E0 !important;
    }
    
    .streamlit-expanderHeader {
        background-color: #F8F9FA !important;
        color: #262730 !important;
    }
    
    .stCodeBlock {
        background-color: #F8F9FA !important;
        border-color: #E0E0E0 !important;
        color: #262730 !important;
    }
    
    .custom-card {
        background-color: #FFFFFF !important;
        border-color: #E0E0E0 !important;
        color: #262730 !important;
    }
    
    .math-expression {
        background-color: #F8F9FA !important;
        border-color: #E0E0E0 !important;
        color: #262730 !important;
    }
    </style>
    """
    
    st.markdown(light_css, unsafe_allow_html=True)

def get_theme_css(theme: str = "light"):
    """Get CSS for specific theme"""
    if theme.lower() == "dark":
        return apply_dark_theme
    else:
        return apply_light_theme 