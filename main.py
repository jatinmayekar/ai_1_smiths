import streamlit as st
import base64
from datetime import datetime
import openai
from dotenv import load_dotenv
from openai import OpenAI
import os


load_dotenv()
ai_model = "gpt-4-1106-preview"
openai.api_key = os.getenv("OPEN_API_KEY")

if 'client' not in st.session_state:
    st.session_state.client = OpenAI()

# Set the page config to wide mode
st.set_page_config(layout="wide")


# Function to get base64 of an image
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# Function to set a background image
def set_background(image_path):
    base64_image = get_image_base64(image_path)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{base64_image}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


set_background('images/abstract-design-creativity-background-blue-600nw-161025986.webp')

# Updated CSS to include the rectangular box
css = """
<style>
@import url('https://fonts.googleapis.com/css?family=Roboto&display=swap');

body {
    font-family: 'Roboto', sans-serif;
    background-color: #7EA4B4; /* Your specified background color */
    color: #2E566A; /* Your specified text color */
}

/* Darken the background slightly to improve contrast */
.stApp {
    filter: brightness(85%);
}

.command-output {
    background-color: rgba(255, 255, 255, 0.7); /* White background with slight transparency */
    padding: 10px;
    font-weight: bold; /* Make text thicker */
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1); /* Shadow for the box */
    margin-left: 10px; /* Space for the arrow */
    text-align: right;
}

.command-input {
    background-color: rgba(255, 255, 255, 0.7); /* White background with slight transparency */
    padding: 10px;
    font-weight: bold; /* Make text thicker */
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1); /* Shadow for the box */
    margin-left: 10px; /* Space for the arrow */
}

.rect-box {
    background-color: #FFFFFF; /* Set the box color to white */
    padding: 10px;
    margin: 10px 0;
    border-radius: 10px; /* Optional: for rounded corners */
}

.flex-container-input {
    display: flex;
    align-items: center;
    margin-bottom: 10px; /* Space between the boxes */
}

/* Container holding both the time and the command output, spaced to the right */
.flex-container-output {
    display: flex;
    justify-content: flex-end; /* Aligns the container content to the right */
    align-items: center;
    margin-bottom: 20px; /* Space between the boxes */
}

.time-text-input {
    font-size: 0.75em; /* Smaller font size for the time text */
    color: #2E566A; /* Adjust the color if needed */
    margin-right: 10px; /* Space between time text and the command box */
}

.time-text-output {
    font-size: 0.75em; /* Smaller font size for the time text */
    color: #2E566A; /* Adjust the color if needed */
    margin-left: 10px; /* Space between time text and the command box */
}

/* Style for the arrow */
.arrow-input {
    margin-right: 10px; /* Space between the arrow and the text */
}

.arrow-output {
    margin-left: 10px; /* Space between the arrow and the text */
}

div.stTextInput > div > div > input {
    background-color: white !important; /* Complete white background */
    color: black !important; /* Text color */
    border-color: white !important; /* Border color */
    border-radius: 0 !important; /* Make corners sharp */
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    z-index: 999;
}

div.stTextInput > div {
    background-color: white !important; /* Complete white background */
    color: black !important; /* Text color */
    border-color: white !important; /* Border color */
    border-radius: 0 !important; /* Make corners sharp */
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    z-index: 999;
}

.sticky-bottom-container {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    z-index: 999;
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)


# Function to create a flex container with time and text
def create_flex_container(ctype, time, text):
    # Assuming ctype 'output' is for user input where text should be right-aligned.
    if ctype == "output":
        return f"""
                <div class="flex-container-output">
                    <div class="command-output">{text}<span class="arrow-output">&lt;</span></div>
                    <div class="time-text-output">{time}</div>
                </div>
                """
    else:
        # For 'input' and other types, you might keep the original layout or adjust accordingly.
        return f"""
                <div class="flex-container-input">
                    <div class="time-text-input">{time}</div>
                    <div class="command-input"><span class="arrow-input">&gt;</span>{text}</div>
                </div>
                """


# Get current time and format it as HH:MM
current_time = datetime.now().strftime("%H:%M")

# Displaying static lines or prompts
st.markdown(create_flex_container("input", current_time, "hihi"), unsafe_allow_html=True)
st.markdown(create_flex_container("output", current_time, "MISSION COMPLETE"), unsafe_allow_html=True)

user_input = st.text_input("Enter some text:", value="", key="user_input", label_visibility="collapsed")
if user_input:
    st.markdown(create_flex_container("output", current_time, user_input), unsafe_allow_html=True)

