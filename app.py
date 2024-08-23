import streamlit as st
import google.generativeai as gen
import os

# Configure the API key
gen.configure(api_key="AIzaSyB9y3zCzpzNKzFq7LOWMn7d3SirCDtDYUI")

# Define the function to generate content
def resp(content_type, input_text, num_words):
    model = gen.GenerativeModel("gemini-1.5-flash")
    prompt = f"Write a well-structured and complete {content_type} on the topic '{input_text}' within {num_words} words. Ensure the content flows logically, provides a clear introduction, explores key points, and ends with a strong conclusion."
    response = model.generate_content(prompt)
    return response.text

# Function to load local files
def load_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Streamlit app configuration
st.set_page_config(page_title="Generate Content", layout="centered", initial_sidebar_state="collapsed")

# Load and apply custom CSS
st.markdown(f'<style>{load_file("styles.css")}</style>', unsafe_allow_html=True)

# Load and display custom HTML
st.markdown(load_file("index.html"), unsafe_allow_html=True)

# Optional: Handling form submissions via Streamlit
if st.session_state.get('submitted'):
    response = resp(st.session_state.contentType, st.session_state.inputText, st.session_state.numWords)
    st.write("### Generated Content:")
    st.write(response)
