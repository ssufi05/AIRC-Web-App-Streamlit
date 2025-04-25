import streamlit as st
import webbrowser as wb

st.set_page_config(
    page_title="AIRC - Partners",  # Title in browser tab
    page_icon="data/airc_logo.jpg"  # Path to logo file
)

# Set the title of the page
st.title("Partners")

# Introduction to the partners section
st.write("""
We seek partners from industry, academia, and the public sector to advance AI technologies and research. Through collaboration, we can create innovative solutions that benefit communities, especially those with limited resources. We believe in the power of partnerships to drive meaningful change and achieve mutual goals.
""")

st.markdown("---")


# Why partner with us?
st.header("Why Partner with AIRC?")
st.write("""
Partnering with AIRC offers a unique opportunity to be part of cutting-edge research and development in AI. By joining forces, we can:

- **Advance AI Solutions**: Collaborate on projects that bring AI-powered solutions to communities and entities that need them most.
- **Expand Reach and Impact**: Work together to scale the impact of AI technologies in various sectors, from education to healthcare and beyond.
- **Leverage Expertise**: Tap into our team's expertise in AI research, software development, and innovation.
- **Drive Innovation**: Contribute to innovative projects that aim to solve real-world problems and make a positive impact.
- **Build Strategic Relationships**: Connect with key stakeholders in the public, private, and academic sectors to create sustainable, long-term partnerships.
""")

st.markdown("---")


# Call to Action
st.header("Become a Partner")
st.write("""
If you are interested in partnering with AIRC to advance AI research and solutions, we would love to discuss potential collaborations. Together, we can create meaningful change and bring AI innovations to communities around the world.

Please fill out the interest form below to learn more about partnership opportunities.
""")

# Link to Interest Form
if st.button("Fill Out the Interest Form"):
    wb.open_new_tab("https://forms.office.com/r/VWGD8YK81U")