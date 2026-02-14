import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="House Rent Prediction",
    page_icon="🏡",
    layout="wide"
)

# ---------------- CSS STYLING ----------------
st.markdown("""
<style>

/* Luxury background */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1600585154340-be6161a56a0c");
    background-size: cover;
    background-attachment: fixed;
}

/* Sidebar dashboard */
section[data-testid="stSidebar"] {
    background-color: black;
    padding: 20px;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: white !important;
    font-weight: 600;
}

/* Main title */
.main-title {
    text-align: center;
    font-size: 48px;
    color: lavender;
    font-weight: bold;
    text-shadow: 2px 2px 5px black;
}

/* Sub text */
.sub-text {
    text-align: center;
    font-size: 22px;
    color: lavender;
}

/* Output box */
.output-box {
    background-color: rgba(210, 210, 210, 0.95);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    color: black;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
}

/* Celebration box */
.celebrate {
    text-align: center;
    font-size: 28px;
    margin-top: 30px;
    color: lavender;
    text-shadow: 2px 2px 6px black;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 80px;
    font-size: 20px;
    font-weight: bold;
    color: lavender;
    text-shadow: 1px 1px 4px black;
}

</style>
""", unsafe_allow_html=True)

# ---------------- DUMMY TRAINED MODEL ----------------
X = np.array([[1,500,1],[2,800,2],[3,1200,3],[4,1500,4]])
y = np.array([8000,12000,18000,25000])

model = LinearRegression()
model.fit(X, y)

# ---------------- TITLE ----------------
st.markdown("<div class='main-title'>HOUSE RENT PREDICTION</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-text'>Predict house rent using smart features</div><br>", unsafe_allow_html=True)

# ---------------- SIDEBAR INPUTS ----------------
st.sidebar.header("🏠 Enter House Details")

bhk = st.sidebar.slider("BHK", 1, 5, 2)
size = st.sidebar.slider("House Size (sqft)", 300, 3000, 1000)
bath = st.sidebar.slider("Bathrooms", 1, 4, 2)

# ---------------- PREDICTION ----------------
if st.sidebar.button("Predict Rent 💰"):
    prediction = model.predict([[bhk, size, bath]])[0]

    st.markdown(
        f"""
        <div class="output-box">
            Estimated Monthly Rent<br><br>
            ₹ {prediction:,.0f}
        </div>
        """,
        unsafe_allow_html=True
    )

    # 🎉 Appreciation & Celebration 🎉
    st.markdown("""
    <div class="celebrate">
        👏👏 Congratulations! 👏👏 <br><br>
        🎈🎈 Great Choice! 🎈🎈 <br>
        🎊 Your Prediction is Ready! 🎊 <br><br>
        🏡✨ Enjoy Your Luxury Living ✨🏡
    </div>
    """, unsafe_allow_html=True)

    st.balloons()  # 🎈 Balloon animation

# ---------------- FOOTER ----------------
st.markdown(
    "<div class='footer'>Created by kusuma 💜</div>",
    unsafe_allow_html=True
)