import streamlit as st
import google.generativeai as gen

# Configure the API key
gen.configure(api_key="AIzaSyB9y3zCzpzNKzFq7LOWMn7d3SirCDtDYUI")

# Define the function to generate content
def resp(content_type, input_text, num_words):
    model = gen.GenerativeModel("gemini-1.5-flash")
    prompt = f"Write a well-structured and complete {content_type} on the topic '{input_text}' within {num_words} words. Ensure the content flows logically, provides a clear introduction, explores key points, and ends with a strong conclusion."
    response = model.generate_content(prompt)
    return response.text

# Streamlit app configuration
st.set_page_config(page_title="Generate Content", layout="centered", initial_sidebar_state="collapsed")

# Header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Generate Content</h1>", unsafe_allow_html=True)
st.markdown("### Enter details below to generate content:")

# User inputs
input_text = st.text_input("**Content Topic:**")
num_words = st.text_input("**Number of Words:**")
content_type = st.selectbox('**Genre of Content:**', ('Article', 'Speech', 'Story', 'Poem'))

# Space between inputs and button
st.markdown("<br>", unsafe_allow_html=True)

# Submit button
submit = st.button("Generate Content")

# Generate and display the response
if submit:
    if input_text and num_words.isdigit():
        response = resp(content_type, input_text, num_words)
        st.markdown("### Generated Content:")
        st.write(response)  # Display the generated content
    else:
        st.error("Please enter a valid topic and number of words.")
