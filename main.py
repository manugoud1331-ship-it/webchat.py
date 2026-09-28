import streamlit as st
from ollama import chat

st.title("my AI Bot: Synora")
name = "manu"
st.write("welcome, ",name)
question = st.text_input("Ask a question")
if st.button("Ask"):
    st.write("You asked: ",question)
    response = chat(model = "gemma3:latest",messages=[
        {
            "role":"system",
            "content":"You are a friendly tutor. You explain conceots in a very simple way.Explain in 50 words max."
        },
        {
            "role":"user",
            "content":question
        }
    ])
    answer = response.message.content
    st.write(answer)


#dropdowm
#options = ["c++","Java","Python"]
#choice = st.selectbox("select your favourite language: ",options)
#st.write(f"You selected {choice}")

