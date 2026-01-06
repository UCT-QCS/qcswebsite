import streamlit as st
import utils.helpers as helpers
import urllib.parse

# Page Config
st.set_page_config(
    page_title="About QCS",
    page_icon="assets/logo.png",
    layout="wide",
)

helpers.render_navigation("pages/05_About.py")

st.markdown("# ℹ️ About UCT QCS")

st.markdown("""
The **UCT Quantum Computing Society** exists to advocate for Quantum Computing in Africa by building an active ecosystem at the University of Cape Town. 
Our mission is to empower students to become future leaders in the field through education, collaboration, and hands-on exposure to real-world quantum technologies.
""")

st.markdown("---")
st.markdown("## 📜 QCS Constitution Overview")
st.markdown("Below are the key directives from our Society's Constitution.")

with st.expander("1. Objectives", expanded=True):
    st.markdown("""
    **The objectives of the Society are:**
    1.  **Build a Community**: Building a strong community of students passionate about quantum and quantum computing.
    2.  **Foster Learning**: Fostering learning opportunities through meetups, seminars, and hands-on projects.
    3.  **Engagement**: Facilitating meaningful engagement on discussions related to Quantum and Quantum Computing.
    4.  **Leadership**: Facilitate the growth of students by building their leadership and networking skills in the field.
    """)

with st.expander("2. Membership"):
    st.markdown("""
    *   **Ordinary Members**: Any student of the University or staff member (with committee approval).
    *   **Honorary Members**: Nominated by the Committee for significant contribution.
    *   All members submit to the rules and discipline of the Society and the University.
    """)

with st.expander("3. Committee Structure"):
    st.markdown("""
    The Committee shall consist of at least five members:
    *   **Chairperson**
    *   **Vice-Chairperson**
    *   **Treasurer**
    *   **Secretary**
    *   **Additional Member**
    
    Committee members are elected at the **Annual General Meeting (AGM)** held in the third quarter of each year.
    """)

with st.expander("4. Meetings"):
    st.markdown("""
    *   **AGM**: Held annually to elect the committee and review reports.
    *   **General/Special Meetings**: Can be convened by the Committee or by request of members.
    *   **Quorum**: Generally one-quarter of members, or a sliding scale based on total membership size (e.g., 50 for 200-300 members).
    """)

with st.expander("5. Affiliation & Amendments"):
    st.markdown("""
    *   The Society may affiliate with other bodies with approval from the Societies Council.
    *   The Constitution can only be amended at a meeting with at least two-thirds majority vote.
    """)

# --- CONTACT US ---
st.markdown("---")
st.markdown("## 📬 Contact Us")
st.markdown("Have questions or want to collaborate? Reach out to us!")

with st.form("contact_form"):
    c_col1, c_col2 = st.columns(2)
    with c_col1:
        name = st.text_input("Name")
        email = st.text_input("Email")
    with c_col2:
        subject = st.selectbox("Subject", ["General Inquiry", "Membership Support", "Partnership/Sponsorship", "Event Question"])
    
    message = st.text_area("Message")
    
    submit_contact = st.form_submit_button("Send Message")
    
    if submit_contact:
        if name and email and message:
            # Prepare Mailto Link
            mail_subject = f"Contact Form: {subject} - {name}"
            mail_body = f"{message}"
            
            params = {
                "subject": mail_subject,
                "body": mail_body
            }
            query_string = urllib.parse.urlencode(params).replace("+", "%20")
            mailto_link = f"mailto:uctqcs@gmail.com?{query_string}"

            st.success(f"Thank you, {name}! Click the button below to send your message.")
            st.link_button("📤 Send Email", mailto_link)
        else:
            st.warning("Please fill in all fields.")

st.markdown("<br><br>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer">
    <div class="social-icons-container">
        <a href="https://instagram.com" target="_blank" class="social-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-instagram"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
        </a>
        <a href="https://linkedin.com" target="_blank" class="social-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-linkedin"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
        </a>
        <a href="https://youtube.com" target="_blank" class="social-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-youtube"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
        </a>
    </div>
    <p>&copy; 2026 UCT Quantum Computing Society.</p>
</div>
""", unsafe_allow_html=True)
