import streamlit as st
import glob
import re

st.set_page_config(
    page_title="AIRC - Search",  # Title in browser tab
    page_icon="data/airc_logo.jpg"  # Path to logo file
)

st.title("Website Search")

search_query = st.text_input("Search the website", "")

# Function to extract displayed text from Streamlit files
def extract_displayed_text():
    content_dict = {}
    for file in glob.glob("pages/*.py"):  # Extract text from all pages
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()

            # Extract text from Streamlit display functions (st.title, st.header, st.write, etc.)
            matches = re.findall(r'st\.(title|header|subheader|write|markdown)\((r?["\'].*?["\'])\)', code, re.DOTALL)
            
            extracted_text = []
            for function, text in matches:
                cleaned_text = eval(text)  # Convert string literals safely
                
                extracted_text.append({
                    "type": function,  # header, write, etc.
                    "text": cleaned_text
                })

            if extracted_text:
                content_dict[file] = extracted_text  # Store extracted text in dict
                
    return content_dict

if search_query:
    st.write("Search Results:")
    content = extract_displayed_text()
    
    results_found = False  # Track if we find results

    for page, sections in content.items():
        matched_sections = [sec for sec in sections if search_query.lower() in sec["text"].lower()]
        
        if matched_sections:
            results_found = True
            st.write(f"### Page: {page.split('/')[-1]}")  # Show file name
            
            for section in matched_sections:
                if section["type"] in ["title", "header", "subheader"]:
                    st.subheader(section["text"])  # Display headers properly
                else:
                    st.write(section["text"])  # Display normal text
                
            st.write("---")  # Divider between results

    if not results_found:
        st.write("No results found.")
