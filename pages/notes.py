import streamlit as st

st.title("📒 Study Notes")

topic = st.text_input("Topic")

if st.button("Create Notes"):
    st.write(f"Notes for {topic}")
