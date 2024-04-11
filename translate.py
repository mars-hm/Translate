import streamlit as st
from googletrans import Translator

st.header("Machine Tralation Demo")

input=st.text_area("please enter the text", value="")
option = st.selectbox(
    "To which language you wish to tranlate this text to?",
    ("Malayalam", "Hindi", "Tamil")
)
if st.button("Translate"):
    translator=Translator()
    translation=translator.translate(input, dest=option)
    st.write(translation.text)    