import streamlit as st

def find_word_in_text(text, word_to_find):
    words = text.split()
    matching_words = [word for word in words if word == word_to_find]
    return matching_words

def main():
    st.title("WortSodhana - Text Searcher")
    
    uploaded_file = st.file_uploader("Choose a text file", type=["txt"])
    
    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")
        st.text_area("Text content", text, height=200)
        
        word_to_find = st.text_input("Enter the word to find")
        
        if word_to_find:
            matching_words = find_word_in_text(text, word_to_find)
            st.write(f"Found {len(matching_words)} occurrences of the word '{word_to_find}':")
            st.write(matching_words)

if __name__ == "__main__":
    main()
