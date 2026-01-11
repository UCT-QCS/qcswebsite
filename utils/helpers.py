import streamlit as st
import os

def load_css(theme):
    """Loads the CSS file based on the theme."""
    file_name = f"assets/{theme}_style.css"
    if theme == "light":
        file_name = "assets/light_style.css"
    else:
        file_name = "assets/style.css"
        
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file {file_name} not found.")

def render_navigation(current_file_path=None):
    """
    Renders the top navigation bar and handles theme toggling.
    This should be called at the very top of every page.
    """
    
    # Initialize theme in session state if not present
    if 'theme' not in st.session_state:
        st.session_state.theme = 'light' # Default
        
    # Toggle logic
    def toggle_theme():
        if st.session_state.theme == 'dark':
            st.session_state.theme = 'light'
        else:
            st.session_state.theme = 'dark'
            
    # Apply CSS
    load_css(st.session_state.theme)

    # --- SIDEBAR BLUR ---
    if st.session_state.theme == "light":
        # Light frosted
        sidebar_bg = "rgba(255, 255, 255, 0.7)"   
    else:
        # Dark frosted
        sidebar_bg = "rgba(14, 17, 23, 0.7)"    

    st.markdown(f"""
        <style>
            [data-testid="stSidebar"] {{
                background-color: {sidebar_bg} !important;
                backdrop-filter: blur(15px) !important;
                -webkit-backdrop-filter: blur(15px) !important;
                border-right: 1px solid rgba(255, 255, 255, 0.1);
            }}
            /* Ensures no solid nested divs block the blur */
            [data-testid="stSidebar"] > div:first-child {{
                background-color: transparent !important;
            }}
        </style>
    """, unsafe_allow_html=True)
    
    # --- TOP SITES NAVIGATION ---
    # Hide sidebar by default
    # st.markdown(
    #     """
    #     <style>
    #         [data-testid="stSidebarNav"] {display: none;}
    #     </style>
    #     """, 
    #     unsafe_allow_html=True
    # )
    
    # --- MOBILE TOGGLE ---
    with st.container():
        st.markdown('<div id="mobile-controls"></div>', unsafe_allow_html=True)
        # Theme button (Mobile only)
        btn_label = "☀️" if st.session_state.theme == 'dark' else "🌙"
        if st.button(btn_label, key="mobile_theme_toggle", help="Toggle Theme"):
            toggle_theme()
            st.rerun()

    # --- DESKTOP NAVIGATION ---
    with st.container():
        st.markdown('<div id="desktop-navbar"></div>', unsafe_allow_html=True)
        # Render Navbar
        # Using columns to simulate a navbar
        cols = st.columns([1, 1, 1, 1, 1, 0.5]) # Last column for theme toggle
        
        # Define pages
        pages = [
            {"label": "Home", "path": "home.py"},
            {"label": "Events", "path": "pages/02_Events.py"},
            {"label": "Community", "path": "pages/03_Community.py"},
            {"label": "Blog", "path": "pages/04_Blog.py"},
            {"label": "About", "path": "pages/05_About.py"},
        ]
        
        # Highlight active page logic
        active_idx = -1
        for i, page in enumerate(pages):
            if page["path"] == current_file_path:
                active_idx = i
                break
                
        # Inject CSS for active highlight if found
        if active_idx != -1:
            if st.session_state.theme == "light":
                st.markdown(f"""
                <style>
                div[data-testid="column"]:nth-of-type({active_idx + 1}) a {{
                    background-color: rgba(0, 212, 255, 0.2) !important; /* Light Cyan transparent */
                    border: 2px solid #00D4FF !important;
                    color: #000000 !important; /* Force Black text */
                    font-weight: bold;
                    border-radius: 8px !important;
                    font-size: 1.1rem !important;
                }}
                </style>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <style>
                div[data-testid="column"]:nth-of-type({active_idx + 1}) a {{
                    background-color: rgba(0, 255, 255, 0.15) !important;
                    border: 1px solid #00FFFF !important;
                    color: #FFFFFF !important; /* Force White text */
                    border-radius: 8px;
                }}
                </style>
                """, unsafe_allow_html=True)
    
        for i, page in enumerate(pages):
            with cols[i]:
                st.page_link(page["path"], label=page["label"], width="stretch")
                
        with cols[-1]:
            # Theme button (Desktop)
            btn_label = "☀️" if st.session_state.theme == 'dark' else "🌙"
            if st.button(btn_label, key="desktop_theme_toggle", help="Toggle Theme"):
                toggle_theme()
                st.rerun()

    st.markdown("---")
