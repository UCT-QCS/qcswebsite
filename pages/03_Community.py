import streamlit as st
import pandas as pd
import plotly.express as px
import os
import utils.helpers as helpers


# Page Config
st.set_page_config(
    page_title="QCS Community",
    page_icon="assets/logo.png",
    layout="wide",
)

helpers.render_navigation("pages/03_Community.py")

st.markdown("# 👥 Community Dashboard")

# --- DATA LOADING ---
CSV_PATH = "data/members.csv"
COMMITTEE_PATH = "data/committee.json"

import json
import base64
import urllib.parse


def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

def load_committee():
    if os.path.exists(COMMITTEE_PATH):
        with open(COMMITTEE_PATH, 'r') as f:
            return json.load(f)
    return []

def load_data():
    if os.path.exists(CSV_PATH):
        return pd.read_csv(CSV_PATH)
    else:
        return pd.DataFrame(columns=["ID", "Name", "Student number", "Faculty", "Email"])

df = load_data()

# --- TOP METRIC ---
# Aligning with user request to show this in "Large and Bold"
if not df.empty:
    total_members = len(df)
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 30px;">
        <h2 style="margin:0; font-size: 2rem; color: #b0b0b0;">Total Members</h2>
        <h1 style="margin:0; font-size: 6rem; font-weight: 900; background: linear-gradient(90deg, #00FFFF, #9D00FF); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{total_members}</h1>
    </div>
    """, unsafe_allow_html=True)

# --- FACULTY PIE CHART ---
if not df.empty and "Faculty" in df.columns:
    st.markdown("### 📊 Faculty Distribution")
    faculty_counts = df['Faculty'].value_counts().reset_index()
    faculty_counts.columns = ['Faculty', 'Count']
    
    fig = px.pie(
        faculty_counts, 
        values='Count', 
        names='Faculty', 
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.Bluyl
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#FAFAFA"),
        showlegend=True,
    )
    # Customize traces for nicer hover info
    fig.update_traces(textposition='inside', textinfo='percent+label')
    
    st.plotly_chart(fig, width="stretch")

# --- COMMITTEE SECTION ---
st.markdown("### 👔 QCS Committee 2026")
committee_data = load_committee()

if committee_data:
    # Custom CSS for cards
    st.markdown("""
    <style>
    .committee-card {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 255, 255, 0.1);
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
    }
    .committee-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0, 255, 255, 0.2);
        border-color: #00FFFF;
    }
    .committee-img {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid #00FFFF;
        margin-bottom: 10px;
        background-color: #fff; /* Ensure transparent pngs look okay */
    }
    .committee-role {
        color: #00FFFF;
        font-weight: bold;
        font-size: 0.9rem;
        margin-bottom: 5px;
        height: 40px; /* Fixed height for alignment */
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .committee-name {
        color: #FAFAFA; /* Or inherit */
        font-size: 1rem;
        font-weight: 500;
        margin-bottom: 10px;
    }
    .linkedin-block {
        display: block;
        margin-top: 10px;
        padding: 8px 12px;
        border-radius: 5px;
        font-size: 0.8rem;
        font-weight: bold;
        text-decoration: none;
        transition: all 0.3s ease;
        
        /* Default (Dark Mode) - match theme */
        background-color: rgba(0, 255, 255, 0.1);
        border: 1px solid #00FFFF;
        color: #00FFFF !important;
    }
    .linkedin-block:hover {
        background-color: #00FFFF;
        color: #000 !important;
    }

    /* Light Mode Overrides (assuming body background check or media query) */
    @media (prefers-color-scheme: light) {
        .linkedin-block {
            background-color: #ffffff;
            border: 1px solid #00d4ff; /* Bluish border */
            color: #000000 !important;
        }
        .linkedin-block:hover {
            background-color: #00d4ff;
            color: #ffffff !important;
        }
    }
    /* Explicit light mode class if streamlits theme injection is detectable, 
       but standard media query is safest for system preference. 
       User said "in light mode", might imply the app theme setting. */
    </style>
    """, unsafe_allow_html=True)

    # Grid Layout
    cols = st.columns(4)
    for i, member in enumerate(committee_data):
        with cols[i % 4]:
            # Resolve image path
            img_path = member['image']
            img_b64 = get_base64_image(img_path)
            
            if img_b64:
                img_src = f"data:image/png;base64,{img_b64}"
            else:
                img_src = "https://via.placeholder.com/100?text=QCS"

            # Prepare Card HTML content
            # We construct the inner content first
            card_content = f"""
<img src="{img_src}" class="committee-img">
<div class="committee-role">{member['role']}</div>
<div class="committee-name">{member['name']}</div>
"""
            
            # Add Link Block if available
            linkedin_url = member.get('linkedin', '')
            if linkedin_url:
                # Dynamic Link Text
                if member['name'] == "TBD":
                    link_text = "Follow Us on LinkedIn"
                else:
                    first_name = member['name'].split()[0]
                    link_text = f"Visit {first_name}'s LinkedIn"
                
                # Append the styled block - FLUSH LEFT
                card_content += f"""
<div class="linkedin-block">
{link_text}
</div>
"""
                
                # Wrap entire card in A tag for clickability - FLUSH LEFT
                wrapper = f"""
<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit; display: block; height: 100%;">
<div class="committee-card">
{card_content}
</div>
</a>
"""
                st.markdown(wrapper, unsafe_allow_html=True)
            else:
                # Non-clickable card - FLUSH LEFT
                st.markdown(f"""
<div class="committee-card">
{card_content}
</div>
""", unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True) # Spacing
else:
    st.info("Committee information coming soon.")

st.markdown("---")

# --- MEMBER LIST ---
st.markdown("### 📋 Member List")
if not df.empty:
    # Display only public columns
    # User might not want student numbers publicly visible, but requested to "show names". 
    # Safest is Name + Faculty.
    display_cols = ["Name", "Faculty"]
    
    # Simple search
    search_term = st.text_input("Search members by name", "")
    
    if search_term:
        filtered_df = df[df['Name'].str.contains(search_term, case=False, na=False)]
    else:
        filtered_df = df
        
    # Display as a styled HTML table for full control (Light Mode support)
    # Using st.html or st.markdown with pandas style
    
    # Define custom CSS for the table
    st.markdown("""
    <style>
    .member-table {
        width: 100%;
        border-collapse: collapse;
        color: inherit; /* Inherits #111 in light mode, #FAFAFA in dark */
    }
    .member-table th {
        text-align: left;
        padding: 12px;
        background-color: rgba(0, 255, 255, 0.1);
        color: inherit;
        border-bottom: 2px solid #00FFFF;
    }
    .member-table td {
        padding: 10px;
        border-bottom: 1px solid rgba(128, 128, 128, 0.2);
    }
    /* Light Mode Specific Table Override loaded via JS/CSS class doesn't exist easily here without 'helpers' knowing state.
       But since we forced body color in CSS, 'inherit' should do the work!
       Light Mode Body = #111 text. Dark Mode Body = #FAFAFA text.
       We just need transparent backgrounds.
    */
    </style>
    """, unsafe_allow_html=True)
    
    # Convert to HTML
    html_table = filtered_df[display_cols].to_html(classes="member-table", index=False, escape=False)
    st.markdown(html_table, unsafe_allow_html=True)
    
else:
    st.info("No members found yet.")

# --- SIGN UP section ---
st.markdown("---")
st.markdown("### 📝 Join the Society")

# New Prospective Members File
PROSPECTIVE_PATH = "data/prospective_members.csv"

with st.form("signup_form"):
    col1, col2 = st.columns(2)
    with col1:
        new_name = st.text_input("Full Name")
        new_student_num = st.text_input("Student Number")
    with col2:
        # Pre-populate faculties found in CSV + 'Other'
        existing_faculties = sorted(df['Faculty'].dropna().unique().tolist()) if not df.empty else []
        if "Other" not in existing_faculties:
            existing_faculties.append("Other")

        new_faculty = st.selectbox("Faculty", options=existing_faculties)
        new_email = st.text_input("Email (Optional)")

    submitted = st.form_submit_button("Sign Up")
    
    if submitted:
        if new_name and new_student_num:
            # Check for duplicates in MAIN list and PROSPECTIVE list
            
            # Load prospective to check there too
            if os.path.exists(PROSPECTIVE_PATH):
                df_prospective = pd.read_csv(PROSPECTIVE_PATH)
            else:
                df_prospective = pd.DataFrame(columns=["Name", "Student number", "Faculty", "Email", "Date Joined"])
                
            # Check Main
            exists_main = not df.empty and new_student_num in df['Student number'].astype(str).values
            # Check Prospective
            exists_prospective = not df_prospective.empty and new_student_num in df_prospective['Student number'].astype(str).values
            
            if exists_main or exists_prospective:
                st.error("This student number is already registered or pending approval.")
            else:
                # Append new prospective member
                new_row = {
                    "Name": new_name,
                    "Student number": new_student_num,
                    "Faculty": new_faculty,
                    "Email": new_email,
                    "Date Joined": pd.Timestamp.now().strftime("%Y-%m-%d")
                }
                new_prospective_df = pd.DataFrame([new_row])
                
                updated_prospective = pd.concat([df_prospective, new_prospective_df], ignore_index=True)
                updated_prospective.to_csv(PROSPECTIVE_PATH, index=False)
                
                st.success(f"Welcome, {new_name}! You have been added to the prospective members list.")
                st.balloons()
                
                # Prepare Mailto Link
                subject = f"New Member Registration: {new_name}"
                body = f"Name: {new_name}\nStudent Number: {new_student_num}\nFaculty: {new_faculty}\nEmail: {new_email}"
                
                # Encode params
                params = {
                    "subject": subject,
                    "body": body
                }
                query_string = urllib.parse.urlencode(params).replace("+", "%20")
                mailto_link = f"mailto:uctqcs@gmail.com?{query_string}"
                
                # Open email client
                st.link_button("📧 Click here to complete registration (Send Email)", mailto_link)
                
                # Auto-open (Javascript hack, optional but nice)
                # st.markdown(f'<meta http-equiv="refresh" content="0;url={mailto_link}">', unsafe_allow_html=True)
                
        else:
            st.warning("Please fill in at least Name and Student Number.")
