import streamlit as st
import webbrowser as wb

st.set_page_config(
    page_title="AIRC - Contact",  # Title in browser tab
    page_icon="data/airc_logo.jpg"  # Path to logo file
)

# Set the title of the page
st.title("Contact Us")

# Introduction to the contact page
st.write("""
We would love to hear from you! Whether you have questions, suggestions, or want to get involved, feel free to reach out to us. We are here to help and look forward to connecting with you.
""")

# Contact form link
st.header("Get in Touch")
st.write("""
For inquiries or to provide feedback, please fill out the form below. We'll get back to you as soon as possible.
""")


# Navigate to Contact Form
if st.button("Fill Out the Contact Form"):
    wb.open_new_tab("https://forms.office.com/r/dhPsBsggFJ")


# Additional contact info
st.header("Follow Us on Social Media")
st.write("""
Follow us on our social media channels for 
- Youtube: [AI Research Corp (AIRC)](http://www.youtube.com/@airesearchcorpairc8071)
- LinkedIn: [AI Research Corp (AIRC)](https://www.linkedin.com/company/artificialintelliegenceresearchcorp/)
""")
