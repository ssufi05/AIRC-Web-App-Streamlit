import streamlit as st
import webbrowser as wb

st.set_page_config(
    page_title="AIRC - Volunteers",  # Title in browser tab
    page_icon="data/airc_logo.jpg"  # Path to logo file
)

# Set the title of the page
st.title("Volunteers")

# Introduction to the volunteers section
st.write("""
We are a community led by volunteers committed to advancing the adoption and adaptation of AI technologies. Our volunteers play a vital role in driving forward the mission of AIRC, and we welcome individuals who share our vision for ethical, innovative, and impactful technology.
""")

st.markdown("---")


# Benefits of volunteering
st.header("Why Volunteer with Us?")
st.write("""
Volunteering with AIRC offers many benefits, including:

- **Impactful Work**: Contribute to projects that advance the adoption of AI technologies in various sectors.
- **Professional Growth**: Gain experience in AI, software development, and research while working alongside experts in the field.
- **Networking**: Connect with professionals, industry leaders, and other passionate individuals committed to making a difference.
- **Skill Development**: Enhance your technical, research, and collaboration skills.
- **Community**: Join a supportive and collaborative community of like-minded individuals striving to create positive change.
""")

st.markdown("---")


# Types of volunteer opportunities
st.header("Volunteer Opportunities")
st.write("""
We have various opportunities available for volunteers to get involved, depending on their interests and expertise. Some of the key areas where we need volunteers include:

- **AI Research**: Contribute to ongoing research projects exploring new ways AI can be used to solve real-world problems.
- **Software Development**: Assist with developing AI-powered tools and applications that benefit underrepresented communities.
- **Community Engagement**: Help us build partnerships and raise awareness of our mission and initiatives.
- **Education and Outreach**: Lead workshops, training sessions, and other activities aimed at educating the public about AI technologies.
- **Technical Support**: Provide technical assistance for our projects, ensuring smooth operation and troubleshooting.
""")

st.markdown("---")


# Call to action
st.header("Join Our Volunteer Community")
st.write("""
Are you passionate about technology and committed to ethical AI development? We would love to have you on board!

Please fill out the interest form below to sign up as a volunteer and stay updated on open positions, upcoming events, and other opportunities.
""")

# Link to Interest Form
if st.button("Fill Out the Volunteer Form"):
    wb.open_new_tab("https://forms.office.com/r/qBPxY7L4zt")