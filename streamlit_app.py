import re
import streamlit as st
import pandas as pd

# Function to extract words based on a search term
def extract_with_search_term(text, search_term):
    # Regex pattern to find words containing the search term
    # This pattern will find any word that contains the search term, regardless of its position
    pattern = re.compile(rf'\b\w*{re.escape(search_term)}\w*\b', re.IGNORECASE)
    matches = pattern.findall(text)
    return set(matches)

def main():
    st.title("Keyword Search and Table Name Extractor")

    uploaded_file = st.file_uploader("Choose a text file", type=["txt"])

    if uploaded_file is not None:
        try:
            content = uploaded_file.read().decode("utf-8")
        except UnicodeDecodeError:
            st.error("Error decoding the file. Please upload a valid UTF-8 encoded text file.")
            return

        # Replace all occurrences of "[" and "]" with spaces
        content = content.replace('[', ' ').replace(']', ' ')
        
        # Replace all occurrences of #(lf)where with space at the start
        content = content.replace('#(lf)where', ' #(lf)where')
        
        st.subheader("Modified Data")
        st.text_area("Content", content, height=300)
        
        st.subheader("Search for Keywords")
        
        # Input for searching with a specific search term
        search_term = st.text_input("Enter the keyword or prefix to search for", "")
        
        if st.button("Search"):
            if search_term:
                unique_keywords = extract_with_search_term(content, search_term)
                
                st.write(f"Total unique keywords containing '{search_term}': {len(unique_keywords)}")
                if unique_keywords:
                    st.table(pd.DataFrame(sorted(unique_keywords), columns=["Keywords"]))
                else:
                    st.write("No keywords found with the specified term.")
            else:
                st.error("Please enter a search term.")

    # Add footer
    footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: black;
        text-align: center;
        padding: 10px;
        font-family: Arial, sans-serif;
        font-size: 12px;
    }
    </style>
    <div class="footer">
        <p>Created by Vihaan Subhash</p>
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)

if __name__ == "__main__":
    main()


