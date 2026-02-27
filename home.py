import streamlit as st
import base64
import utils.helpers as helpers

# Page Config
st.set_page_config(
    page_title="UCT QCS",
    page_icon="assets/logo.png",
    layout="wide",
)

helpers.render_navigation("home.py")

# --- HERO SECTION ---
with st.container():
    st.image("assets/opening-event-header.png", width='stretch')

# --- INAUGURAL EVENT ANNOUNCEMENT ---
st.markdown("---")
with st.container():
    st.markdown('<div class="feature-card" style="margin-top: 10px; border-left: 5px solid #00d4ff;">', unsafe_allow_html=True)
    c1, c2 = st.columns([3, 1])
    with c1:
        st.markdown("### � UCT QCS Inaugural Opening Event")
        st.markdown("""
        **Date:** Wednesday, 4 March 2026 | **Time:** 17:30 - 18:30 | **Venue:** SNAPE LT1
        
        Join us for our first major step in demonstrating the multidisciplinary power of quantum technology. 
        Featuring **Ndivhuwo Nyase**, Research Scientist at IBM Research, on *"Journey into Quantum Applications"*.
        
        **Classical vs Quantum Quiz & Prizes:** Top performer wins official UCT QCS merchandise!
        """)
    with c2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.link_button("RSVP Now", "https://forms.gle/2pkbioVZcVwQhD2WA", width='stretch')
        if st.button("View Event Details", key="view_event_btn"):
            st.switch_page("pages/02_Events.py")
    st.markdown('</div>', unsafe_allow_html=True) 

# --- FEATURES SECTION ---
st.markdown("### Why Join UCT QCS?")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="card-icon">🎓</div>
        <div class="card-title">Education & Skills</div>
        <div class="card-text">
            Master the Qiskit SDK and quantum algorithms through our <b>Quantum Computing Educational Talks (QCET)</b>.
            Get access to world-class learning resources and documentation.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="card-icon">🤝</div>
        <div class="card-title">IBM Research Collaboration</div>
        <div class="card-text">
            Direct collaboration with <b>IBM Research Africa</b>. 
            Gain access to real <b>Quantum Hardware</b> (10 mins/month) and mentorship from IBM scientists.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="card-icon">🌍</div>
        <div class="card-title">Community & Events</div>
        <div class="card-text">
            Join the <b>Quantum Computing Roundtables</b>, Hackathons, and even Quantum Movie Nights.
            Connect with industry leaders and like-minded students.
        </div>
    </div>
    """, unsafe_allow_html=True)


# --- MEMBERSHIP DETAILS ---
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

m_col1, m_col2 = st.columns([1, 1])

with m_col1:
    st.image("assets/ndivhuwo-keynote.png", width='stretch')

with m_col2:
    st.markdown("### Membership Details")
    st.markdown("""
    Becoming a member of UCT QCS opens the door to the future of computing. 
    
    **Registration Fee:** <span class="highlight-text">free</span>
    
    **Exclusive Benefits:**
    - ⚛️ **IBM Quantum Access**: Open plan account access to IBM's quantum computers.
    - 📚 **Learning Platform**: Free access to IBM Quantum Learning courses.
    - 🗣️ **Seminars**: Annual in-person seminars led by IBM scientists.
    - 💼 **Career Opportunities**: Internships and co-supervision possibilities.
    """, unsafe_allow_html=True)

    st.markdown('<div class="cta-button-container">', unsafe_allow_html=True)
    if st.button("Become a Member"):
        st.switch_page("pages/03_Community.py")
    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer">
    <div class="social-icons-container">
        <a href="https://instagram.com" target="_blank" class="social-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-instagram"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
        </a>
        <a href="https://www.linkedin.com/company/uct-qcs" target="_blank" class="social-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-linkedin"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
        </a>
        <a href="https://www.youtube.com/@UCTQCS" target="_blank" class="social-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-youtube"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
        </a>
    </div>
    <p>&copy; 2026 UCT Quantum Computing Society.</p>
</div>
""", unsafe_allow_html=True)
