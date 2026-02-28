import streamlit as st
import pickle
import pandas as pd
import json

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Spam Detector",
    page_icon="🛡️",
    layout="centered"
)

# ---------------- MOBILE OPTIMIZED CSS ----------------
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 1rem;
    padding-right: 1rem;
}

textarea {
    border-radius: 12px !important;
}

.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 3em;
    font-size: 16px;
}

.highlight {
    background-color: #ff4b4b;
    color: white;
    padding: 3px 6px;
    border-radius: 6px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LANGUAGE TOGGLE ----------------
language = st.selectbox("🌍 Select Language", ["English", "Hindi"])

translations = {
    "English": {
        "title": "🛡️ AI Spam Detection System",
        "subtitle": "Hybrid AI-powered spam & scam detection engine",
        "input": "✉️ Enter a message to analyze:",
        "button": "🔍 Analyze Message",
        "spam": "⚠️ This message is SPAM!",
        "safe": "✅ This message appears safe.",
        "prob": "📊 Spam Probability:",
        "risk": "🔐 Risk Level:",
        "dashboard": "📊 Live Dashboard",
        "total": "Total Checked",
        "spam_detected": "Spam Detected",
        "safe_msg": "Safe Messages",
        "empty": "Please enter a message."
    },
    "Hindi": {
        "title": "🛡️ एआई स्पैम डिटेक्शन सिस्टम",
        "subtitle": "हाइब्रिड एआई आधारित स्पैम और स्कैम पहचान प्रणाली",
        "input": "✉️ संदेश दर्ज करें:",
        "button": "🔍 जांचें",
        "spam": "⚠️ यह संदेश स्पैम है!",
        "safe": "✅ यह संदेश सुरक्षित है।",
        "prob": "📊 स्पैम संभावना:",
        "risk": "🔐 जोखिम स्तर:",
        "dashboard": "📊 लाइव डैशबोर्ड",
        "total": "कुल जांच",
        "spam_detected": "स्पैम पाया गया",
        "safe_msg": "सुरक्षित संदेश",
        "empty": "कृपया संदेश दर्ज करें।"
    }
}

t = translations[language]

# ---------------- SESSION STATE ----------------
if "total_checked" not in st.session_state:
    st.session_state.total_checked = 0
if "spam_count" not in st.session_state:
    st.session_state.spam_count = 0
if "ham_count" not in st.session_state:
    st.session_state.ham_count = 0

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ---------------- HEADER ----------------
st.title(t["title"])
st.markdown(f"##### {t['subtitle']}")
st.markdown("---")

# ---------------- INPUT ----------------
message = st.text_area(t["input"], height=130)

# ---------------- DASHBOARD (TOP) ----------------
st.subheader(t["dashboard"])
col1, col2, col3 = st.columns(3)
col1.metric(t["total"], st.session_state.total_checked)
col2.metric(t["spam_detected"], st.session_state.spam_count)
col3.metric(t["safe_msg"], st.session_state.ham_count)

st.markdown("---")

# ---------------- ANALYSIS ----------------
if st.button(t["button"]):

    if message.strip() == "":
        st.warning(t["empty"])

    else:
        data = vectorizer.transform([message])
        probability = model.predict_proba(data)[0][1]

        suspicious_words = ["win", "free", "click", "offer", "prize", "urgent", "money"]
        detected_words = [word for word in suspicious_words if word in message.lower()]

        # Highlight suspicious words
        highlighted_message = message
        for word in detected_words:
            highlighted_message = highlighted_message.replace(
                word,
                f"<span class='highlight'>{word}</span>"
            )

        # ---------------- SHOW ANALYZED MESSAGE ----------------
        st.markdown("### 🔎 Analyzed Message:")
        st.markdown(highlighted_message, unsafe_allow_html=True)

        # ---------------- HYBRID DECISION ----------------
        if probability > 0.4 or len(detected_words) >= 2:
            st.error(t["spam"])
            st.session_state.spam_count += 1
        else:
            st.success(t["safe"])
            st.session_state.ham_count += 1

        st.session_state.total_checked += 1

        # ---------------- PROBABILITY ----------------
        st.markdown(f"### {t['prob']} {probability * 100:.2f}%")

        # ---------------- SPEEDOMETER ----------------
        percent = int(probability * 100)

        if percent < 40:
            color = "#00c853"
            risk_level = "🟢 LOW"
        elif percent < 75:
            color = "#ff9800"
            risk_level = "🟠 MEDIUM"
        else:
            color = "#ff1744"
            risk_level = "🔴 HIGH"

        st.markdown(f"""
        <div style="display:flex; justify-content:center; margin-top:20px;">
            <svg width="200" height="120">
                <circle cx="100" cy="100" r="80" stroke="#2c2f36" stroke-width="20" fill="none" />
                <circle cx="100" cy="100" r="80" stroke="{color}" stroke-width="20"
                        stroke-dasharray="{2.513 * percent}, 251.3"
                        stroke-linecap="round"
                        transform="rotate(-90 100 100)" />
                <text x="100" y="110" font-size="24" text-anchor="middle" fill="white" font-weight="bold">{percent}%</text>
            </svg>
        </div>
        """, unsafe_allow_html=True)

        # ---------------- RISK LEVEL ----------------
        st.markdown(f"### {t['risk']} {risk_level}")

        # ---------------- KEYWORD ALERT ----------------
        if detected_words:
            st.warning("⚠️ Suspicious keywords detected:")
            st.write(", ".join(detected_words))

        # ---------------- UPDATED DASHBOARD ----------------
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        col1.metric(t["total"], st.session_state.total_checked)
        col2.metric(t["safe_msg"], st.session_state.ham_count)
        col3.metric(t["spam_detected"], st.session_state.spam_count)