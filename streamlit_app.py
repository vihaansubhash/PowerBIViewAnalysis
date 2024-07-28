import re
import streamlit as st

def find_unique_views(text):
    # Convert entire content to uppercase
    text = text.upper()
    
    # Find all view names with 'VW_' prefix
    pattern = re.compile(r'\bVW_\w+\b', re.IGNORECASE)
    views = pattern.findall(text)
    
    # Remove duplicates and return the result
    unique_views = set(views)
    return unique_views

def main():
    st.title("WortSodhana - Text Searcher")
    
    uploaded_file = st.file_uploader("Choose a text file", type=["txt"])
    
    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8")
        st.text_area("Text content", content, height=200)
        
        unique_views = find_unique_views(content)
        
        st.write(f"Total unique views: {len(unique_views)}")
        st.write("Unique Views:")
        for view in unique_views:
            st.write(view)

if __name__ == "__main__":
    main()
