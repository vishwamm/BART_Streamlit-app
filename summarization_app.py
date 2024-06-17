from transformers import pipeline
import streamlit as st
st.title("Hugging face model-Bart")
paragraph=st.text_input("Give me a paragraph to summarize:")
if paragraph:
    if st.button("Summarize"):
        with st.spinner("summarizing .....it may take a while"):
            summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
            a=summarizer(paragraph, max_length=130, min_length=30, do_sample=False)
        data=a[0]
        value=data['summary_text']
        st.success("Successfully summarized!")
        st.write(value)
