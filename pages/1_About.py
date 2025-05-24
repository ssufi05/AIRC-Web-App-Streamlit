import streamlit as st

st.set_page_config(
    page_title="AIRC - About",  # Title in browser tab
    page_icon="data/airc_logo.png"  # Path to logo file
)

# Set the title of the page
st.title("About Us")


# Create two columns for better layout
col1, col2 = st.columns([1, 3])

with col1:
    st.image("data/airc_logo.png", width=150)

with col2:
    st.subheader("Mission")
    st.write("""
    Our mission is to provide the public with research and software development services for the purpose of advancing the adoption and adaption of artificial intelligence technologies. 
    And to develop and grow local tech talent. We fulfill our mission by partnering with the private, public, and academic sectors.
    """)

# Add some spacing
st.markdown("---")

# 🎯 **Core Values** Section
st.header("Core Values")
st.write("Our core values define the framework in which we accomplish our mission.")

# Create a 2-column layout for the core values
col1, col2 = st.columns(2)

with col1:
    with st.expander("**Ethical Responsibility**"):
        st.write("""
        AI technologies are going to impact all of humanity. Collectively we share the burden to ensure safe and ethical applications. Not only for ourselves but also for others, and for future generations.
        """)

    with st.expander("**Excellence**"):
        st.write("""
        Excellence starts at the individual level and then collectively reflects on its communities. Our community seeks excellence by putting in the effort, commitment, and dedication required to accomplish smart goals.
        """)

    with st.expander("**Integrity**"):
        st.write("""
        We follow a set of rules and ethical principles to govern our community according to ideals that define what constitutes honorable behavior.
        """)

with col2:
    with st.expander("**Fellowship**"):
        st.write("""
        Fellowship defines a strong community. We enjoy our work, and we are guided by our shared mission and values.
        """)

    with st.expander("**Diversity**"):
        st.write("""
        Our differences eliminate our blind spots and make us stronger. A diverse community is better equipped to eliminate biases and address inequity problems in the technical sectors.
        """)

    with st.expander("**Freedom**"):
        st.write("""
        Modern societies must enjoy new technologies without the threat of control over their privacy and unalienable rights. Freedom of information and speech are essential for the prosperity of democratic societies in a world bound by technology.
        """)

# Add spacing at the bottom
st.markdown("---")