import streamlit as st
import requests
import pandas as pd

st.title("Hybrid Search Dashboard")

query = st.text_input("Search Query")

st.write("Query:", query)

top_k = st.slider("Top K Results", 1, 10, 5)

alpha = st.slider("Hybrid Weight (BM25 vs Vector)", 0.0, 1.0, 0.5)

if st.button("Search"):

    response = requests.post(
        "http://127.0.0.1:8000/search",
        params={
            "query": query,
            "top_k": top_k,
            "alpha": alpha
        }
    )

    results = response.json()["results"]

    df = pd.DataFrame(results)

    st.write("Search Results")
    st.dataframe(df)

    st.bar_chart(df[["bm25_score", "vector_score", "hybrid_score"]])