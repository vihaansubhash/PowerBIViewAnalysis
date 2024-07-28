import re
import streamlit as st

def find_unique_views(text, prefix):
    # Convert entire content to uppercase
    text = text.upper()
    
    # Create a dynamic regex pattern based on the prefix
    pattern = re.compile(rf'\b{prefix}\w+\b', re.IGNORECASE)
    views = pattern.findall(text)
    
    # Remove duplicates and return the result
    unique_views = set(views)
    return unique_views

def main():
    st.title("WordSodhan - Text Searcher")
    
    uploaded_file = st.file_uploader("Choose a text file", type=["txt"])
    
    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8")
        st.text_area("Text content", content, height=200)
        
        prefix = st.text_input("Enter the prefix to search for", "VW_")
        
        if st.button("Search"):
            if prefix:
                unique_views = find_unique_views(content, prefix)
                
                st.write(f"Total unique views with prefix '{prefix}': {len(unique_views)}")
                st.write("Unique Views:")
                for view in unique_views:
                    st.write(view)
            else:
                st.error("Please enter a prefix to search for.")

if __name__ == "__main__":
    main()
