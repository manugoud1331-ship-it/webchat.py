import streamlit as st
from ollama import chat

st.title("MY AI Chatbot:")
#messages = []
system_message = "You are a shakespearean tutor. Answer in a sentence of 50 words max."
#messegs.append(
#    {
#        "role":"user",
#        "content":system_messages
#    }
#)
if "messages" not in st.session_state:
    st.session_state.message = [
        {
            "role":"",
            "content":system_message
        }
]
#display pervious messages
for message in st.session_state.message:
    #Don't dispaly system message
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

question = st.chat_input("Ask something...")
if question :
    with st.chat_message("user"):
        st.write(question)
    st.session_state.messages.append({
        "role":"user",
        "content":question
    })
    with st.spinner("Thinking..."):
        response = chat(model = "gemma3:latest",
        messages=st.session_state.messages)  
        answer = response.message.content
        with st.chat_message("assistant"):
            st.write(answer)
        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":answer
            }
        )  
