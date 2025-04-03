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
    👋 Hi! I'm a Data Scientist with expertise in Machine Learning, Deep Learnig, Time Series Forecasting 
    Check out my projects below!
    """)

# Projects Page
elif page == "Projects":
    st.header("My Projects")

    # Project 1
    st.subheader("📌 Customer segmentation using Clustering")
    st.write("Customer segmentation on a retail data using RFM Analysis. RFM (Recency, Frequency, Monetary) analysis is a popularly used technique in marketing to identify high-value customers based on the purchasing behaviour. Here we have used 3 clustering approaches; kmeans, hierarchical clustering and dbscan, and analyse which is effective for the given data")
    st.image("images/hierarchical_clustering.png")
    st.link_button("View on GitHub", "https://github.com/LakshmiRajan05/Customer-Segmentation-using-Clustering")

    # Project 2
    st.subheader("📌 Basic Chatbot using NLP")
    st.write("Built an NLP based chatbot to answer user questions. The application returns best matching answer from a pre-defined FAQ (Frequently Asked Questions) file.")
    st.image("images/chatbot.png")
    st.link_button("View on GitHub", "https://github.com/LakshmiRajan05/FAQ-Chatbot")

# Contact Page
elif page == "Contact":
    st.header("📬 Get in Touch")
    st.write("Feel free to connect with me on [LinkedIn](www.linkedin.com/in/lakshmi-r-20d21")
