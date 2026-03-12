import streamlit as st
import requests
import pandas as pd
import sqlite3


def load_kpis():

    try:
        conn = sqlite3.connect("data/metrics/search_logs.db")

        total_queries = conn.execute(
            "SELECT COUNT(*) FROM query_logs"
        ).fetchone()[0]

        avg_latency = conn.execute(
            "SELECT AVG(latency_ms) FROM query_logs"
        ).fetchone()[0]

        top_queries = conn.execute(
            "SELECT query, COUNT(*) as freq FROM query_logs GROUP BY query ORDER BY freq DESC LIMIT 5"
        ).fetchall()

        conn.close()

    except:
        total_queries = 0
        avg_latency = 0
        top_queries = []

    return total_queries, avg_latency, top_queries


# Dashboard title
st.title("Hybrid Search Dashboard")

# KPI Section
st.header("Search System KPIs")

total_queries, avg_latency, top_queries = load_kpis()

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Queries", total_queries)

with col2:
    st.metric("Average Latency (ms)", round(avg_latency or 0, 2))

st.subheader("Top Queries")

if top_queries:
    for q, count in top_queries:
        st.write(f"{q} — {count} searches")
else:
    st.write("No queries logged yet.")


st.divider()


# Search Section
st.header("Search")

query = st.text_input("Search Query")

st.write("Query:", query)

top_k = st.slider("Top K Results", 1, 10, 5)

alpha = st.slider("Hybrid Weight (BM25 vs Vector)", 0.0, 1.0, 0.5)


if st.button("Search"):

    if query.strip() == "":
        st.warning("Please enter a query.")
    else:

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

        st.subheader("Search Results")

        st.dataframe(df)

        st.subheader("Score Comparison")

        st.bar_chart(df[["bm25_score", "vector_score", "hybrid_score"]])