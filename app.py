import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
# from langchain_community.llms import CTransformers
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

def getLlamaResponse(input_text, no_words, blog_style):

    llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q8_0.bin",
                      model_type='llama',
                      config={'max_new_tokens':256,'temperature':0.01})
    
    template= " Write a blog for {blog_style} job profile for a topic {input_text} witin {no_words}."
    
    prompt = PromptTemplate(input_variables= ["blog_style", "input_text", "no_words"], template=template)

    response = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response



st.set_page_config(page_title="Generate Blogs", layout="centered", initial_sidebar_state="collapsed")

st.header("Generate Blogs")

input_text=st.text_input("Enter the Blodg Topic")

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("Number of Words")

with col2:
    blog_style = st.selectbox('Writing the blog for', ('Researchers', 'Data Scientists', 'Common People'), index=0)

submit=st.button("Generate")

if submit:
    st.write(getLlamaResponse(input_text, no_words, blog_style))



