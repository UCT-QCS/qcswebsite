import streamlit as st
import calendar
import datetime
import json
import pandas as pd
import utils.helpers as helpers

# Page Config
st.set_page_config(
    page_title="QCS Events",
    page_icon="assets/logo.png",
    layout="wide",
)

helpers.render_navigation("pages/02_Events.py")

st.markdown("# 📅 QCS Events Calendar")
st.markdown("Stay up to date with the latest workshops, hackathons, and socials.")

# --- LOAD DATA ---
@st.cache_data
def load_events():
    with open('data/events.json', 'r') as f:
        data = json.load(f)
    return data

events_data = load_events()
df_events = pd.DataFrame(events_data)
df_events['date'] = pd.to_datetime(df_events['date'])

# --- CALENDAR CONTROLS ---
col1, col2 = st.columns([2, 1])

with col2:
    # Month selector
    today = datetime.date.today()
    # If today is before 2026, set default to Feb 2026 for demo purposes
    if today.year < 2026:
        default_date = datetime.date(2026, 2, 1)
    else:
        default_date = today

    selected_date = st.date_input("Select Month", value=default_date, min_value=datetime.date(2026, 1, 1), max_value=datetime.date(2026, 12, 31))
    year = selected_date.year
    month = selected_date.month

with col1:
    st.markdown(f"## {calendar.month_name[month]} {year}")

# --- CALENDAR RENDERING ---
# Get month matrix
cal = calendar.monthcalendar(year, month)
day_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Render Header
header_cols = st.columns(7)
for i, day_name in enumerate(day_names):
    header_cols[i].markdown(f"**{day_name}**", unsafe_allow_html=True)

# Filter events for this month
month_events = df_events[(df_events['date'].dt.year == year) & (df_events['date'].dt.month == month)]

# Create a dictionary of events by day
events_by_day = {}
for _, event in month_events.iterrows():
    day = event['date'].day
    if day not in events_by_day:
        events_by_day[day] = []
    events_by_day[day].append(event)

# Render Rows
for week in cal:
    cols = st.columns(7)
    for i, day in enumerate(week):
        with cols[i]:
            if day == 0:
                st.markdown('<div class="calendar-day empty"></div>', unsafe_allow_html=True)
            else:
                # Check for events
                day_events = events_by_day.get(day, [])
                
                # Determine styling
                is_today = (day == today.day) and (month == today.month) and (year == today.year)
                today_class = "current-day" if is_today else ""
                
                # Build HTML for events within the day cell
                events_html = ""
                for event in day_events:
                    events_html += f'<div class="event-marker {event["type"]}">{event["title"]}</div>'
                
                # Render the "card" for the day
                # We can't make it clickable directly to open a modal in standard Streamlit easily without a button.
                # So we will use a button that looks like the whole day or just a button inside.
                # Alternative: Render HTML and use a separate selection mechanism below.
                
                st.markdown(
                    f"""
                    <div class="calendar-day {today_class}">
                        <div class="day-number">{day}</div>
                        {events_html}
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
                
                # If there are events, add a button to view details
                if day_events:
                    if st.button(f"View {day} {calendar.month_abbr[month]}", key=f"btn_{month}_{day}"):
                        st.session_state['selected_event_day'] = day
                        st.session_state['selected_event_month'] = month
                        st.rerun()

# --- EVENT DETAILS ---
st.markdown("---")
# Check if a day is selected via session state
if 'selected_event_day' in st.session_state and st.session_state['selected_event_month'] == month:
    sel_day = st.session_state['selected_event_day']
    sel_events = events_by_day.get(sel_day, [])
    
    if sel_events:
        st.markdown(f"### Events on {sel_day} {calendar.month_name[month]}")
        for event in sel_events:
            with st.expander(f"{event['title']} ({event['time']})", expanded=True):
                st.markdown(f"**📍 Location:** {event['location']}")
                st.markdown(f"**📝 Description:** {event['description']}")
                st.markdown(f"**🏷️ Type:** {event['type']}")
    else:
        st.info("No events on this day.")

elif not month_events.empty:
    st.markdown("### Upcoming Events")
    # Show next 3 events
    upcoming = month_events.sort_values('date').head(3)
    for _, event in upcoming.iterrows():
         with st.expander(f"{event['date'].strftime('%d %b')} - {event['title']}", expanded=False):
            st.write(event['description'])
            if st.button("More Info", key=f"more_{event['id']}"):
                pass # Just expands
else:
    st.info(f"No events scheduled for {calendar.month_name[month]} {year}.")
