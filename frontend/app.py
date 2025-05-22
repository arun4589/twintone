import streamlit as st
import requests

st.set_page_config(page_title="AI Prompt Generator", layout="wide")
st.title("TwinTone AI")

user_id = st.text_input("Enter your User ID", value="test_user")

query = st.text_area("Your question or topic:")
if st.button("Generate") and query:
    with st.spinner("Generating..."):
        response = requests.post("http://localhost:8000/generate", json={"user_id": user_id, "query": query})
        if response.status_code == 200:
            data = response.json()
            st.subheader("Casual Style")
            st.write(data["casual_response"])
            st.subheader("Formal Style")
            st.write(data["formal_response"])
        else:
            st.error("Failed to get a response from the backend.")

with st.sidebar:
    st.header("Your History")
    history = requests.get(f"http://localhost:8000/history?user_id={user_id}").json()
    for item in history:
        with st.expander(f"{item['query']} ({item['created_at']})"):
            st.markdown("**Casual:** " + item["casual_response"])
            st.markdown("**Formal:** " + item["formal_response"])
