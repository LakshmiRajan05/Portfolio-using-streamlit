import streamlit as st

# Set Page Title
st.set_page_config(page_title="My Data Science Portfolio", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

# Home Page
if page == "Home":
    st.title("Welcome to My Portfolio")
    st.write("""
    👋 Hi! I'm a Data Scientist with expertise in ML, NLP, and MLOps.
    Check out my projects below!
    """)

# Projects Page
elif page == "Projects":
    st.header("My Projects")

    # Example Project 2
    st.subheader("📌 Basic Chatbot using NLP")
    st.write("Built an NLP based chatbot to answer user questions. The application returns best matching answer from a pre-defined FAQ (Frequently Asked Questions) file.")
    st.image("images/chatbot.png")
    st.link_button("View on GitHub", "https://github.com/LakshmiRajan05/FAQ-Chatbot")

# Contact Page
elif page == "Contact":
    st.header("📬 Get in Touch")
    st.write("Feel free to connect with me on [LinkedIn](www.linkedin.com/in/lakshmi-r-20d21")
