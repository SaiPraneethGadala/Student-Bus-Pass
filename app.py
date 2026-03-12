import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="Student Bus Pass", page_icon="🚌", layout="centered")

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#e3f2fd,#ffffff);
}

.main-title{
    text-align:center;
    font-size:42px;
    color:#1a237e;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

.form-box{
    background:white;
    padding:35px;
    border-radius:15px;
    box-shadow:0px 8px 20px rgba(0,0,0,0.15);
}

.stButton>button{
    background:linear-gradient(45deg,#1a237e,#3949ab);
    color:white;
    font-size:18px;
    border-radius:10px;
    padding:10px 25px;
    border:none;
}

.stButton>button:hover{
    background:linear-gradient(45deg,#0d1b5e,#283593);
    transform:scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.markdown('<p class="main-title">🎓 Student Bus Pass Application</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Apply Online for Student Bus Pass</p>', unsafe_allow_html=True)

# -----------------------------
# Form Container
# -----------------------------
with st.container():

    st.markdown('<div class="form-box">', unsafe_allow_html=True)

    st.subheader("👤 Student Details")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=5)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        mobile = st.text_input("Mobile Number")

    with col2:
        email = st.text_input("Email")

        city = st.selectbox(
            "City",
            ["Hyderabad", "Warangal", "Karimnagar", "Nizamabad", "Khammam"]
        )

        pass_type = st.selectbox(
            "Pass Type",
            ["Student Pass", "General Pass", "Senior Citizen Pass"]
        )

        duration = st.selectbox(
            "Pass Duration",
            ["1 Month", "3 Months", "6 Months"]
        )

    # -----------------------------
    # Travel Details
    # -----------------------------
    st.subheader("🚌 Travel Details")

    places = [
        "Ameerpet",
        "Kukatpally",
        "LB Nagar",
        "Miyapur",
        "Secunderabad",
        "Charminar",
        "Gachibowli",
        "Hitech City"
    ]

    col3, col4 = st.columns(2)

    with col3:
        source = st.selectbox("From", places)

    with col4:
        destination = st.selectbox("To", places)

    start_date = st.date_input("Start Date")

    # -----------------------------
    # Upload Photo
    # -----------------------------
    st.subheader("📷 Upload Pass Photo")

    photo = st.file_uploader("Upload Student Photo", type=["jpg","png","jpeg"])

    if photo is not None:
        st.image(photo, caption="Uploaded Photo", width=150)

    # -----------------------------
    # Address
    # -----------------------------
    address = st.text_area("Address")

    # -----------------------------
    # Submit Button
    # -----------------------------
    if st.button("Apply for Student Bus Pass"):
        st.success("✅ Student Bus Pass Application Submitted Successfully!")
        st.balloons()

    st.markdown('</div>', unsafe_allow_html=True)