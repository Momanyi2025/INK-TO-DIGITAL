import streamlit as st
from components.upload import upload_component
from components.processing import processing_component # This component might now just show a spinner
from components.output import output_component
from components.styling import apply_custom_styles

# Assume you have functions for the actual heavy lifting
# (These would ideally be in a separate utility or service file)
# For now, we'll mock them.
import time # For simulating processing time

def perform_document_processing(uploaded_file):
    """
    This function would contain the actual logic for OCR, vectorization, etc.
    It takes the uploaded file and returns processed data (e.g., text, vector graphics).
    """
    # Simulate a delay for processing
    time.sleep(3) # Represents the time taken for OCR, vectorization, etc.

    # In a real app, you would pass uploaded_file to your OCR/vectorization engine
    # For demonstration, we'll return some mock data.
    mock_processed_text = "This is the digitally recognized text from your handwritten notes."
    mock_vector_data = "SVG data representing your cleaned-up drawings."

    return {"text": mock_processed_text, "vector": mock_vector_data}


def main():
    # Apply custom styling
    apply_custom_styles()

    # Set page configuration
    st.set_page_config(
        page_title="INK TO DIGITAL",
        page_icon="✍️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # App header
    st.markdown('<h1 class="header">✍️ INK TO DIGITAL</h1>', unsafe_allow_html=True)
    st.markdown("Transform your handwritten notes into polished digital documents")

    # Initialize session state for better control
    # 'uploaded_file': Stores the file object after upload
    # 'processing_started': True when "Start Processing" is clicked
    # 'processed_data': Stores the result after processing is complete
    # 'current_tab': Helps control which tab is active (optional, but useful)

    if 'uploaded_file' not in st.session_state:
        st.session_state.uploaded_file = None
    if 'processing_started' not in st.session_state:
        st.session_state.processing_started = False
    if 'processed_data' not in st.session_state:
        st.session_state.processed_data = None
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = "Upload" # Default tab

    # Create tabs for different stages
    # Use key to manage active tab more explicitly if needed later
    tab_titles = ["Upload", "Processing", "Output"]
    tab1, tab2, tab3 = st.tabs(tab_titles)

    with tab1:
        st.session_state.current_tab = "Upload"
        uploaded_file = upload_component()
        if uploaded_file:
            st.session_state.uploaded_file = uploaded_file
            st.success("File uploaded successfully! Go to the 'Processing' tab to continue.")
            # Optionally, automatically switch tab
            # st.session_state.current_tab = "Processing" # This won't work directly to switch tabs instantly on button click due to Streamlit's reruns

    with tab2:
        st.session_state.current_tab = "Processing"
        if st.session_state.uploaded_file:
            st.write("---") # Separator for clarity
            st.image(st.session_state.uploaded_file, caption="Uploaded Document Preview", use_column_width=True)
            st.write("---") # Separator for clarity

            if st.button("Start Processing", type="primary", key="start_processing_btn"):
                st.session_state.processing_started = True
                st.session_state.processed_data = None # Clear previous data if reprocessing

            if st.session_state.processing_started:
                with st.spinner("Processing document... This may take a moment."):
                    # Call the actual processing function
                    processed_result = perform_document_processing(st.session_state.uploaded_file)
                    st.session_state.processed_data = processed_result

                st.success("Processing complete! Go to the 'Output' tab to see the results.")
                st.session_state.processing_started = False # Reset state after processing is done
                # Optionally, here you could try to programmatically switch to the output tab
                # This often requires a bit more advanced Streamlit state management or
                # using the 'key' argument for tabs and setting it in session state.
                # For now, a message is sufficient.

            elif st.session_state.processed_data: # If already processed and not actively processing
                 st.info("Document already processed. Go to the 'Output' tab to view results, or upload a new file.")

        else:
            st.info("Please upload an image in the 'Upload' tab to begin processing.")

    with tab3:
        st.session_state.current_tab = "Output"
        if st.session_state.processed_data:
            output_component(st.session_state.processed_data) # Pass the data to the output component
        else:
            st.info("Process a document in the 'Processing' tab to see the output preview.")

if __name__ == "__main__":
    main()
