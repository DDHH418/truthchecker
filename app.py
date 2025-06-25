import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import pickle

# Load users from YAML file
with open("users.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create authenticator
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status is False:
    st.error("❌ Incorrect username or password")
elif authentication_status is None:
    st.warning("⌨️ Please enter your login credentials")
elif authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.success(f"👋 Welcome, {name}!")

    # TruthChecker App
    st.title("🕵️‍♀️ TruthChecker - Fake Message Detector")
    st.subheader("Paste any message to check if it's FAKE or REAL.")

    user_input = st.text_area("🔍 Enter your message here:")

    @st.cache_resource
    def load_model():
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)
        with open("vectorizer.pkl", "rb") as f:
            vectorizer = pickle.load(f)
        return model, vectorizer

    model, vectorizer = load_model()

    if st.button("Check Truth"):
        if user_input.strip() == "":
            st.warning("Please enter a message.")
        else:
            vec = vectorizer.transform([user_input])
            pred = model.predict(vec)
            confidence = model.predict_proba(vec).max()

            if pred[0] == 0:
                st.error(f"⚠️ FAKE ({confidence*100:.2f}% confidence)")
            else:
                st.success(f"✅ REAL ({confidence*100:.2f}% confidence)")
