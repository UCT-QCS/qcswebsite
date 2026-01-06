import streamlit as st
import pandas as pd
import json
import os
import utils.helpers as helpers

# Page Config
st.set_page_config(
    page_title="QCS Blog",
    page_icon="assets/logo.png",
    layout="wide",
)

helpers.render_navigation("pages/04_Blog.py")

st.markdown("# 📰 QCS Research Highlights")

# --- DATA LOADING ---
BLOGS_PATH = "data/blogs.json"

def load_blogs():
    if os.path.exists(BLOGS_PATH):
        with open(BLOGS_PATH, 'r') as f:
            return json.load(f)
    return []

blogs = load_blogs()

# --- LAYOUT ---
if not blogs:
    st.info("No blog posts available yet. Check back soon!")
else:
    # Sidebar for filtering/selection
    st.sidebar.header("Recent Posts")
    
    # Sort blogs by date desc
    blogs.sort(key=lambda x: x['date'], reverse=True)
    
    # Selection
    selected_blog_id = st.sidebar.radio(
        "Select a post",
        options=[b['id'] for b in blogs],
        format_func=lambda x: next((b['title'] for b in blogs if b['id'] == x), "Unknown")
    )
    
    # Find selected blog
    current_blog = next((b for b in blogs if b['id'] == selected_blog_id), None)
    
    if current_blog:
        st.markdown(f"## {current_blog['title']}")
        st.markdown(f"**By {current_blog['author']}** | *{current_blog['date']}* | 🏷️ `{current_blog['tag']}`")
        st.markdown("---")
        st.markdown(current_blog['content'])
        
        # Citation Card
        if 'pdf_url' in current_blog:
            # IEEE Citation format: [1] A. Author, "Title," Source, Month Year. [Online]. Available: URL
            citation_text = f'[1] {current_blog["author"]}, "{current_blog["title"]}", *Nature Communications*, {current_blog["date"]}. [Online]. Available: {current_blog["pdf_url"]}'
            
            st.markdown("---")
            st.markdown("### Citation")
            
            # Card styling
            st.markdown(
                f"""
                <a href="{current_blog['pdf_url']}" target="_blank" style="text-decoration: none; color: inherit;">
                    <div style="
                        border: 1px solid #ddd;
                        border-radius: 8px;
                        padding: 15px;
                        background-color: #f9f9f9;
                        cursor: pointer;
                        transition: box-shadow 0.3s;
                    " onmouseover="this.style.boxShadow='0 4px 8px rgba(0,0,0,0.1)'" onmouseout="this.style.boxShadow='none'">
                        <div style="display: flex; align-items: center;">
                            <div style="font-size: 24px; margin-right: 15px;">📄</div>
                            <div>
                                <div style="font-weight: bold; margin-bottom: 5px; color: #333;">PDF Source</div>
                                <div style="font-size: 0.9em; color: #555;">
                                    {citation_text}
                                </div>
                            </div>
                        </div>
                    </div>
                </a>
                """,
                unsafe_allow_html=True
            )
    else:
        st.error("Blog post not found.")
