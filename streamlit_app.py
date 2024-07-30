import re
import streamlit as st
import pandas as pd

# Function to extract table names based on a specific prefix
def extract_with_prefix(text, prefix):
    # Regex pattern to find words with the specified prefix
    pattern = re.compile(rf'\b{prefix}\w+\b', re.IGNORECASE)
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
        
        # Input for searching with a specific prefix
        prefix = st.text_input("Enter the prefix to search for (e.g., 'vw_')", "vw_")
        
        if st.button("Search"):
            if prefix:
                unique_keywords = extract_with_prefix(content, prefix)
                
                st.write(f"Total unique keywords with prefix '{prefix}': {len(unique_keywords)}")
                if unique_keywords:
                    st.table(pd.DataFrame(sorted(unique_keywords), columns=["Keywords"]))
                else:
                    st.write("No keywords found with the specified prefix.")
            else:
                st.error("Please enter a prefix to search for.")

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

