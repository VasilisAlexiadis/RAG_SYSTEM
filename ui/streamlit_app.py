import streamlit as st
import requests

st.title("Enterprise RAG – LangChain + Ollama + Semantic Chunking")

question = st.text_input("Ask a question:")

if st.button("Submit"):
    response = requests.post(
        "http://localhost:8000/api/query",
        json={"question": question}
    )
    output = response.json()

    st.subheader("Answer")
    st.write(output["answer"])

    st.subheader("Sources")
    for src in output["sources"]:
        st.json(src)
