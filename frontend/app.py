import streamlit as st
import requests
from PIL import Image

# ---------------- CONFIG ---------------- #
API_URL = "http://127.0.0.1:8004/predict"

st.set_page_config(
    page_title="Bone Fracture Detection",
    page_icon="🦴",
    layout="centered"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>
/* Remove Streamlit default top padding */
.block-container {
    padding-top: 1rem !important;
}

/* Optional: tighten header spacing */
.title {
    margin-bottom: 5px;
}

.subtitle {
    margin-top: 0px;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)



# ---------------- HEADER ---------------- #
st.markdown("<div class='title'>🦴 Bone Fracture Detection</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI-powered X-ray fracture analysis</div>", unsafe_allow_html=True)

# ---------------- UPLOAD SECTION ---------------- #
st.markdown("<div class='card'>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "📤 Upload X-ray Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded X-ray Image", use_column_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- DETECTION ---------------- #
if uploaded_file:
    if st.button("🔍 Detect Fracture", use_container_width=True):
        with st.spinner("Analyzing X-ray image..."):
            response = requests.post(
                API_URL,
                files={"file": uploaded_file.getvalue()}
            )

        if response.status_code == 200:
            result = response.json()

            st.markdown("<div class='card'>", unsafe_allow_html=True)

            if result["total_detections"] == 0:
                st.success("✅ No fracture detected")
                st.info("The X-ray image appears normal.")
            else:
                st.success(f"🩻 Fracture Detected: {result['total_detections']}")

                for det in result["detections"]:
                    st.markdown(
                        f"""
                        <div class='result-card'>
                            <div class='result-title'>
                                🦴 {det['class'].replace('_', ' ').title()}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            st.markdown("</div>", unsafe_allow_html=True)

        else:
            st.error("❌ Unable to connect to detection service")

# ---------------- FOOTER ---------------- #
st.markdown("---")

