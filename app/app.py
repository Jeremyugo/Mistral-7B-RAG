import streamlit as st

st.title(f'Mistral-7B R.A.G App ⚙️🗃️')
st.write("This is a Retrieval Augmented Generation streamlit app powered by the open-source Mistral 7B LLM and llama-index.")


data = st.file_uploader('Upload your document', type=['txt', 'json'])

if data:
    query = st.chat_input("Query your data")