import streamlit as st

def output_component():
    st.subheader("Digital Output")
    
    # Output preview and customization
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="output-preview">', unsafe_allow_html=True)
        st.markdown("### Document Preview")
        
        # Create a simulated digital output
        preview_text = """
        # Analyzing Handwriting Patterns
        
        This text has been converted from your handwriting to a clean digital format while preserving your unique style.
        
        ## Key Features
        
        - **Style Preservation**: Maintains your handwriting characteristics
        - **Clean Formatting**: Proper spacing and alignment
        - **Editable Content**: Easy to modify and customize
        
        You can now export this document in various formats for sharing or further editing.
        """
        
        st.markdown(preview_text)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Customization Options")
        
        st.selectbox("Font Style", ["Rounded", "Elegant", "Modern", "Professional"])
        st.slider("Font Size", 12, 24, 16)
        st.selectbox("Text Alignment", ["Left", "Center", "Right"])
        st.color_picker("Text Color", "#000000")
        
        st.markdown("---")
        st.markdown("### Export Options")
        
        export_col1, export_col2 = st.columns(2)
        with export_col1:
            st.button("📄 PDF")
        with export_col2:
            st.button("🎨 SVG")
        
        st.download_button(
            label="📝 DOCX",
            data="Simulated document content",
            file_name="converted_document.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
        
        st.markdown("---")
        st.markdown("### Share")
        st.text_input("Shareable link", "https://ink-to-digital.example.com/doc/abc123")
