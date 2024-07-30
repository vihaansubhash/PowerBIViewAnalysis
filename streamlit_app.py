import re
import streamlit as st
import pandas as pd  # Import pandas

# Function to extract table names
def extract_table_names(text):
    # Regex pattern to find table names after "FROM" or "JOIN"
    pattern = r'\b(from|join)\s+((?:[a-zA-Z0-9_]+\s*\.\s*)?[a-zA-Z0-9_]+\s*\.[a-zA-Z0-9_]+|(?:[a-zA-Z0-9_]+\s*\.\s*)?[a-zA-Z0-9_]+)'
    matches = re.findall(pattern, text, re.IGNORECASE)
    
    # Filter out matches with 'join (select'
    filtered_matches = [match for match in matches if not re.search(r'\bjoin\s+\(\s*select\b', match[0], re.IGNORECASE)]
    
    # Extract the second group from matches and remove any extraneous spaces or brackets
    table_names = [re.sub(r'[\[\]\s]+', '', match[1]) for match in filtered_matches if match[1]]
    
    return table_names

# Function to extract words containing a specific search term
def extract_with_search_term(text, search_term):
    # Regex pattern to find words containing the search term
    pattern = re.compile(rf'\b\w*{re.escape(search_term)}\w*\b', re.IGNORECASE)
    matches = pattern.findall(text)
    return set(matches)

def main():
    st.title("Table Name Extractor and Keyword Search")

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
        
        # Extract table names from the modified content
        table_names = extract_table_names(content)
        
        # Convert table names to uppercase, remove duplicates, and sort
        unique_table_names = sorted(set(name.upper() for name in table_names))
        
        st.subheader("Extracted Table Names")
        if unique_table_names:
            st.write(f"Total unique table names: {len(unique_table_names)}")
            st.table(pd.DataFrame(unique_table_names, columns=["Table Names"]))
        else:
            st.write("No table names found.")
        
        st.subheader("Search for Keywords")

        # Input for searching with a specific search term
        search_term = st.text_input("Enter the keyword or prefix to search for", "")
        
        if st.button("Search Keywords"):
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



