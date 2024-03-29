import streamlit as st
from streamlit_chat import message
import requests
 
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
API_TOKEN = st.secrets["api_key"]


headers = {"Authorization": f"Bearer {API_TOKEN}"}
 
st.header("🤖ks's BlenderBot (Demo)")
st.header("Disclaimer: AI의 법률조언에 대해 책임지지 않습니다. 정확한 상담은 info@schunglaw.com 으로 예약하시면 됩니다.  ")
st.markdown("[referrence Chung & Associates](https://schunglaw.com)")
 
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
 
if 'past' not in st.session_state:
    st.session_state['past'] = []
 
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
 
 
with st.form('form', clear_on_submit=True):
    user_input = st.text_input('You: ', '', key='input')
    submitted = st.form_submit_button('Send')
 
if submitted and user_input:
    output = query({
        "inputs": {
            "past_user_inputs": st.session_state.past,
            "generated_responses": st.session_state.generated,
            "text": user_input,
        },
        "parameters": {"repetition_penalty": 1.33},
    })
 
    st.session_state.past.append(user_input)
    with st.spinner("waiting for response..."):
        st.session_state.generated.append(output["generated_text"])
 
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        with st.spinner("waiting for response..."):
            message(st.session_state["generated"][i], key=str(i))



        #requirements.txt  만들고
       # requests
        #message
        #streamlit

        #  .gitignore   만들고
        #   .streamlit/*
 
        #.streamlit  folder만들고
        #secrets.toml 파일생성
        #api_key = "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"
