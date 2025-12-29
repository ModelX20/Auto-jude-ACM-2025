import streamlit as st
import joblib

# =========================
# Page configuration
# =========================
st.set_page_config(
    page_title="AutoJudge",
    page_icon="🧠",
    layout="wide"
)

# =========================
# Load trained models
# =========================
@st.cache_resource
def load_models():
    clf = joblib.load("difficulty_classifier.pkl")
    reg = joblib.load("difficulty_regressor.pkl")
    vec = joblib.load("tfidf_vectorizer.pkl")
    return clf, reg, vec

clf_model, reg_model, vectorizer = load_models()

# =========================
# Session state
# =========================
for key in ["problem", "input", "output", "analyze"]:
    if key not in st.session_state:
        st.session_state[key] = ""

# =========================
# Clear function
# =========================
def clear_all():
    st.session_state.problem = ""
    st.session_state.input = ""
    st.session_state.output = ""
    st.session_state.analyze = ""

# =========================
# Custom CSS (clean + readable)
# =========================
st.markdown(
    """
    <style>
    header {display: none;}
    [data-testid="stToolbar"] {display: none;}

    .stApp {
        background-color: #f4f6fb;
    }

    /* Style Streamlit containers as cards - but not the first one */
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"]:not(:first-child) {
        background-color: white;
        padding: 24px;
        border-radius: 14px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.06);
        margin-bottom: 24px;
    }

    textarea {
        border-radius: 10px !important;
        background-color: #fafafa !important;
        font-size: 16px !important;
        font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif !important;
        line-height: 1.6 !important;
        color: #1f2937 !important;
        border: 2px solid #d1d5db !important;
        transition: border-color 0.2s ease !important;
    }

    textarea:focus {
        border-color: #2563eb !important;
        outline: none !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1) !important;
    }

    /* Bold & bigger labels */
    label {
        font-weight: 700 !important;
        font-size: 1.15rem !important;
        color: #111827 !important;
        margin-bottom: 8px !important;
    }

    /* Make all text larger and more readable */
    .stMarkdown, p, span, div {
        font-size: 16px !important;
        line-height: 1.6 !important;
    }

    div.stButton > button {
        background-color: #2563eb;
        color: white;
        border-radius: 10px;
        height: 3.2em;
        font-size: 17px;
        font-weight: 600;
        letter-spacing: 0.3px;
    }

    div.stButton > button:hover {
        background-color: #1e40af;
    }

    /* Remove default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# Header
# =========================
st.markdown(
    """
    <h1 style="font-weight:800; margin-bottom: 0; font-size: 2.8rem; text-align: center;">🧠 AutoJudge Dashboard</h1>
    <p style="color:#666; font-size:1.25rem; margin-top: 8px; font-weight: 500; text-align: center;">
    Automated Programming Difficulty Classification & Scoring
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# =========================
# Input Section
# =========================
with st.container():
    st.markdown("<h3 style='font-weight:700; margin-bottom: 20px; font-size: 1.6rem;'>📋 Problem Specifications</h3>", unsafe_allow_html=True)

    problem_desc = st.text_area(
        "Problem Description",
        height=160,
        placeholder="Describe the problem statement...",
        key="problem"
    )

    col1, col2 = st.columns(2)

    with col1:
        input_desc = st.text_area(
            "Input Description",
            height=130,
            placeholder="Describe input format...",
            key="input"
        )

    with col2:
        output_desc = st.text_area(
            "Output Description",
            height=130,
            placeholder="Describe output format...",
            key="output"
        )

# =========================
# Buttons (side by side)
# =========================
b1, b2 = st.columns(2)

with b1:
    if st.button("🚀 Analyze Problem", use_container_width=True):
        st.session_state.analyze = "yes"

with b2:
    st.button("🧹 Clear All", use_container_width=True, on_click=clear_all)

# =========================
# Prediction (RESULTS AT BOTTOM)
# =========================
if st.session_state.analyze == "yes":
    if problem_desc.strip() == "":
        st.warning("⚠️ Please enter the problem description.")
    else:
        full_text = f"{problem_desc} {input_desc} {output_desc}"
        X = vectorizer.transform([full_text])

        with st.spinner("Analyzing problem complexity..."):
            label = clf_model.predict(X)[0]
            score = float(reg_model.predict(X)[0])

        # Set color based on difficulty label
        if label.lower() == "easy":
            color = "#2ecc71"
        elif label.lower() == "medium":
            color = "#f1c40f"
        else:
            color = "#e74c3c"

        with st.container():
            st.markdown("<h3 style='font-weight:700; margin-bottom: 20px; font-size: 1.6rem;'>📊 Evaluation Result</h3>", unsafe_allow_html=True)

            r1, r2 = st.columns(2)

            with r1:
                st.markdown(
                    f"<h2 style='color:{color}; margin: 0; font-size: 2.2rem;'>🏷️ {label.upper()}</h2>",
                    unsafe_allow_html=True
                )

            with r2:
                st.markdown(
                    f"<h2 style='margin: 0; font-size: 2.2rem;'>⭐ {score:.2f} / 10</h2>",
                    unsafe_allow_html=True
                )

            st.markdown("<br>", unsafe_allow_html=True)
            st.progress(score / 10)