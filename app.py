import streamlit as st
from PIL import Image
from datetime import datetime

st.set_page_config(
    page_title="CrackGuard AI",
    page_icon="🏗️",
    layout="wide"
)

st.title("🏗️ CrackGuard AI")
st.subheader("AI-Powered Building Crack Inspection Support")

st.info(
    "Upload a building image to begin a preliminary "
    "visual inspection."
)

st.warning(
    "This prototype does not yet contain a trained AI "
    "detection model. Results are not structural safety "
    "assessments."
)

if "history" not in st.session_state:
    st.session_state.history = []

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a page",
    ["Home", "Inspection History", "About"]
)

if page == "Home":
    st.header("🔍 Building Image Inspection")

    building_id = st.text_input(
        "Building ID or Name",
        placeholder="Example: Building A"
    )

    uploaded_file = st.file_uploader(
        "Upload a wall image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(
            image,
            caption="Uploaded building image",
            use_container_width=True
        )

        st.caption(
            "Image uploaded successfully. "
            "AI detection is not connected yet."
        )

        if st.button("Save Inspection Record"):
            st.session_state.history.append({
                "Building": building_id or "Unnamed",
                "Date": datetime.now().strftime(
                    "%d-%m-%Y %H:%M"
                ),
                "Image": uploaded_file.name,
                "Status": "Pending professional review"
            })

            st.success("Inspection record saved!")

elif page == "Inspection History":
    st.header("📋 Inspection History")

    if st.session_state.history:
        st.dataframe(
            st.session_state.history,
            use_container_width=True
        )
    else:
        st.write("No inspection records saved in this session.")

elif page == "About":
    st.header("About CrackGuard AI")

    st.write(
        "CrackGuard AI is a prototype designed to support "
        "building image inspection and maintenance records."
    )

    st.write("Planned future features:")
    st.write("- AI-based crack detection")
    st.write("- Crack image comparison")
    st.write("- Inspection reports")
    st.write("- Maintenance notifications")

st.divider()

st.caption(
    "CrackGuard AI | College Project Prototype | "
    "Professional structural assessment is essential."
)
