import streamlit as st
from PIL import Image
from supabase import create_client, Client
import os

# Hawaiian Fonts & Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600&display=swap');
body {
    background: linear-gradient(135deg, #FFF7E2 0%, #FDEAA8 100%) !important;
}
h1, .aloha-title {
    font-family: 'Pacifico', cursive;
    font-size: 3em;
    color: #F76A1A;
    letter-spacing: 2px;
    text-shadow: 1px 2px 10px #FFC8A2, 0 3px #FFCD58;
}
.header-waves {
    background: linear-gradient(90deg, #43e97b 0%, #38f9d7 100%);
    border-radius: 0 0 30px 30px;
    box-shadow: 0 6px 14px -5px #48CAE4;
    padding: 8px 0 24px 0;
    margin-bottom: 16px;
}
.tropical-box {
    background: linear-gradient(130deg, #e63946 30%, #f1faee 100%);
    padding: 16px;
    border-radius: 18px;
    margin: 12px 0;
    border: 2px solid #FFCD58;
    box-shadow: 2px 4px 12px #ffe5b4;
}
.rsvp-form {
    background: #ffe5b4;
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 24px;
}
.rsvp-confirm {
    background: #43e97b22;
    color: #205c38;
    padding: 12px 10px;
    border-radius: 14px;
}
.rsvplist {
    max-width: 540px;
    margin: 0 auto;
}
</style>
""", unsafe_allow_html=True)

# Supabase credentials (replace values)
SUPABASE_URL = "https://lkgbhkgbucucedipqhhp.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxrZ2Joa2didWN1Y2VkaXBxaGhwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA4NDUyNDIsImV4cCI6MjA2NjQyMTI0Mn0.SXM25VqtlipI1Laig_nKzD_Hje8dSZEnc9-0N92I3DQ"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ALOHA HEADER
st.markdown('''
<div class="header-waves">
    <h1 class="aloha-title" style="text-align:center;">🌺 Hawai Themed Cocktail 🍹Garden Party  🍺🌴</h1>
    <p style="text-align: center; font-size: 20px; color:#205c38; font-family:'Quicksand', sans-serif;">
        You’re invited to a garden party!<br><br>
        <b>🌞 Date:</b> Saturday, July 26, 2025 - 4PM <br>
        <b>🌊 Dress code:</b> Wear your best Hawaiian shirt & flip flops 🌴
    </p>
</div>
''', unsafe_allow_html=True)

# TROPICAL IMAGE

# Animated Flower Rain (Streamlit can't animate natively; emoji cascade as a subtle effect)
st.markdown('''
<p style="font-size:1.6em;text-align:center;animation:rain 3s linear infinite;">
    🌺 🌸 🌴 🥥 🍍 🦩
</p>
''', unsafe_allow_html=True)

st.markdown("---")

# RSVP FORM
st.markdown('<div class="tropical-box">', unsafe_allow_html=True)
with st.form("rsvp_form"):
    st.markdown("### 🌊 RSVP Details")
    name = st.text_input("🌺 Name")
    attending = st.radio("🌴 Are you joining the party?", ["Yes, can't wait!", "Sorry, can't make it!"]) == "Yes, can't wait!"
    num_adults = st.number_input("👨‍🌾 Number of adults", min_value=0, max_value=10, value=1)
    num_children = st.number_input("🧒 Number of children", min_value=0, max_value=10, value=0)
    submitted = st.form_submit_button("🌺 RSVP Now!")

    if submitted:
        if name:
            response = supabase.table("rsvps").insert({
                "name": name,
                "attending": attending,
                "num_adults": num_adults,
                "num_children": num_children
            }).execute()
            if hasattr(response, 'status_code') and response.status_code == 201:
                st.success("🌞 Mahalo! Your RSVP is in — grab your hat and glass and get ready to hula! 🤙")
            else:
                 st.error(f"🌞 Mahalo! Your RSVP is in — grab your hat and glass and get ready to hula! 🤙")
        else:
            st.warning("⚠️ Please enter your name before submitting.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")


# Optional: "Play music" widget (UI only, no auto-play for Streamlit):
st.markdown('''
<center>
    <label style="font-family:'Quicksand',sans-serif; color:#264653;">🎵 Island Vibes: <em>Press play for tropical tunes!</em></label><br>
    <audio controls style="width:220px;">
        <source src="https://www.bensound.com/bensound-music/bensound-sunny.mp3" type="audio/mp3">
        Your browser does not support audio.
    </audio>
</center>
''', unsafe_allow_html=True)
