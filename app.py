import streamlit as st
import pandas as pd

st.set_page_config(page_title="MLB Non-K Prop Engine", layout="wide")

st.title("MLB Non-K Prop Engine v12.1")
st.subheader("Railway + Streamlit Ready")

tabs = st.tabs([
    "Pitching Outs",
    "Hits Allowed",
    "Walks",
    "Earned Runs",
    "Batter Hits",
    "H+R+RBI"
])

sample = pd.DataFrame({
    "Player": ["Example Player"],
    "Projection": [2.5],
    "Line": [1.5],
    "Pick": ["OVER"]
})

for tab in tabs:
    with tab:
        st.dataframe(sample, use_container_width=True)

st.success("App running successfully.")