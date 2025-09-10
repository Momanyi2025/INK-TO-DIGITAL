import streamlit as st
import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Define a constant for the assets directory
ASSETS_DIR = "app/assets"

def create_sample_image(text, filename):
    """Create a sample handwritten image if it doesn't exist."""
    filepath = os.path.join(ASSETS_DIR, filename)
    if os.path.exists(filepath):
        return # Don't recreate if it already exists

    img = Image.new('RGB', (400, 300), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except Exception: # Catch broader exceptions for font loading
        font = ImageFont.load_default()

    d.text((20, 20), text, fill=(0, 0, 0), font=font)

    # Save to assets
    if not os.path.exists(ASSETS_DIR):
        os.makedirs(ASSETS_DIR)

    img.save(filepath)
    return # No need to return the image object itself here

def upload_component():
    st.subheader("Upload Your Handwritten Document")

    col1, col2 = st.columns(2)

    # Initialize session state for holding the currently selected file path/object
    if 'selected_file' not in st.session_state:
        st.session_state.selected_file = None

    with col1:
        st.markdown('<div class="upload-box">', unsafe_allow_html=True)
        # Use a key for the file_uploader to avoid potential issues with multiple identical widgets
        uploaded_file_obj = st.file_uploader(" ", type=["png", "jpg", "jpeg"], label_visibility="collapsed", key="file_uploader_main")

        # If a new file is uploaded, update session state and display it
        if uploaded_file_obj is not None and uploaded_file_obj != st.session_state.selected_file:
            st.session_state.selected_file = uploaded_file_obj
            st.image(uploaded_file_obj, caption="Uploaded Image", use_column_width=True)
        elif uploaded_file_obj is None and isinstance(st.session_state.selected_file, (str, Image.Image)):
            # If a sample was previously selected and now file_uploader is empty, display the sample
            # Need to handle opening the image file if it's a path
            if os.path.exists(st.session_state.selected_file):
                st.image(st.session_state.selected_file, caption="Selected Sample Image", use_column_width=True)
            else:
                st.info("Drag and drop an image here or click to browse")
        else: # Initial state or no file selected
            st.info("Drag and drop an image here or click to browse")


        st.markdown("Supported formats: PNG, JPG, JPEG")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("Or try a sample:")

        # Ensure sample images exist
        create_sample_image("Sample Handwritten Note\n\nThis is a test of the\nINK TO DIGITAL system", "sample1.png")
        create_sample_image("Another Example\n\nWith different handwriting\nand formatting styles", "sample2.png")

        sample_col1, sample_col2 = st.columns(2)
        with sample_col1:
            if st.button("Sample Note 1", key="sample_btn_1"):
                st.session_state.selected_file = os.path.join(ASSETS_DIR, "sample1.png")
                # Clear the file uploader if a sample is selected, to avoid conflict
                uploaded_file_obj = None # This will clear the widget on the next rerun
                st.experimental_rerun() # Force a rerun to update the UI immediately
        with sample_col2:
            if st.button("Sample Note 2", key="sample_btn_2"):
                st.session_state.selected_file = os.path.join(ASSETS_DIR, "sample2.png")
                # Clear the file uploader if a sample is selected
                uploaded_file_obj = None # This will clear the widget on the next rerun
                st.experimental_rerun() # Force a rerun to update the UI immediately

        # Display the currently selected file if it's a sample
        if isinstance(st.session_state.selected_file, str) and os.path.exists(st.session_state.selected_file):
            st.image(st.session_state.selected_file, caption="Selected Sample Image", use_column_width=True)


    with col2:
        st.markdown("### How it works:")
        st.markdown("""
        1. Upload a photo of your handwritten notes
        2. Our AI analyzes the handwriting and converts it to digital text
        3. Customize the style and format of your digital document
        4. Export in your preferred format (PDF, SVG, or DOCX)
        """)

        st.markdown("---")
        st.markdown("**Perfect for:**")
        st.markdown("- 📝 Converting handwritten notes to digital formats")
        st.markdown("- 🎨 Preserving your unique handwriting style digitally")
        st.markdown("- 📚 Digitizing journals, recipes, and personal documents")
        st.markdown("- 💼 Creating professional documents from sketches")

    # The upload_component now returns the value from session state
    # main.py will read st.session_state.selected_file
    return st.session_state.selected_file
