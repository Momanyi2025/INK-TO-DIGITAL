import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .stButton>button {
            background-color: #4f46e5;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 12px 24px;
            font-weight: 600;
        }
        .stButton>button:hover {
            background-color: #4338ca;
            color: white;
        }
        .upload-box {
            background-color: white;
            padding: 30px;
            border-radius: 12px;
            border: 2px dashed #4f46e5;
            text-align: center;
            margin-bottom: 20px;
        }
        .processing-step {
            background-color: white;
            padding: 20px;
            border-radius: 88px;
            border-left: 5px solid #4f46e5;
            margin-bottom: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .output-preview {
            background-color: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        .header {
            color: #4f46e5;
            text-align: center;
            margin-bottom: 30px;
        }
    </style>
    """, unsafe_allow_html=True)
