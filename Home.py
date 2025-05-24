import streamlit as st

st.set_page_config(
    page_title="AIRC",  # Title in browser tab
    page_icon="data/airc_logo.jpg"  # Path to logo file
)

st.image("data/airc_banner.png")

# Set the title of the page
st.title("Help us make a positive impact on the future of AI")

# Display the main content
st.write("""
AIRC is a science and technology research institute, dedicated to creating talent, tools, and bridges necessary to improve the human and economic condition in a world bound by advanced technologies.

We are excited about the future. Harnessing AI technologies to our benefit can help us prosper. However, technology is a double-edged sword. So, we also have to think about potential adverse impacts in order to stay ahead of the curve.
""")

st.markdown("---")


# Section for volunteers
st.header("We are a community led by volunteers")
st.write("""
Technology can bring about great revenues. And we believe that technology should be freely available to everyone. However, what distinguishes us is that we strongly believe that technological advancement should maintain a standard set of core values in order to remain equitable, just, and ethical. 
It's our responsibility as individuals to maintain these standards. Especially during the early stages when the rules aren't clearly defined.
""")


# Navigate to Volunteers
st.page_link("pages/2_Volunteers.py", label="VISIT our Volunteers page for more info.")

st.markdown("---")


# Section for partners
st.header("Partners")
st.write("""
We seek partners from industry, academia, and the public sector. With a focus on providing AI solutions for entities and communities with limited resources. We also seek partners that can help us advance our research efforts.
""")

# Navigate to Partners
st.page_link("pages/3_Partners.py", label="VISIT our Partners page for more info.")

