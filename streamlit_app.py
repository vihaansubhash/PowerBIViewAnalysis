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
        
        prefix = st.text_input("Enter the text to search for")
        
        if st.button("Search"):
            if prefix:
                unique_views = find_unique_views(content, prefix)
                
                st.write(f"Total unique words with input text '{prefix}': {len(unique_views)}")
                st.write("Unique Words:")
                for view in unique_views:
                    st.write(view)
            else:
                st.error("Please enter a prefix to search for.")

    # Add footer
    st.markdown("""<style>
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
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
