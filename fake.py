import streamlit as st

st.set_page_config(page_title="TruthChecker - Sign Up", layout="centered")

# Background and CSS
page_bg = '''
<style>
body {
background-image: url("https://i.imgur.com/5uVYqCJ.jpg");
background-size: cover;
background-repeat: no-repeat;
background-position: center;
}

.signup-box {
    background-color: rgba(0, 0, 0, 0.6);
    padding: 50px 30px;
    border-radius: 20px;
    color: white;
    max-width: 400px;
    margin: auto;
    margin-top: 80px;
    text-align: center;
}

.signup-box h1 {
    font-size: 30px;
    margin-bottom: 20px;
}

.signup-box .highlight {
    color: #00B4DB;
    font-weight: bold;
}

.signup-input {
    margin: 10px 0;
    background-color: rgba(255, 255, 255, 0.2);
    border: none;
    padding: 12px;
    width: 100%;
    border-radius: 12px;
    color: white;
}

input[type="text"], input[type="password"], input[type="email"] {
    background: none;
    border: none;
    outline: none;
    color: white;
    width: 100%;
}

.signup-box .btn {
    background: linear-gradient(to right, #00B4DB, #0083B0);
    color: white;
    padding: 12px;
    font-size: 18px;
    border: none;
    border-radius: 25px;
    margin-top: 20px;
    cursor: pointer;
    width: 100%;
}

.signup-box .links {
    margin-top: 20px;
    font-size: 14px;
    color: #ccc;
}

.signup-box a {
    color: #00B4DB;
    text-decoration: none;
    font-weight: bold;
}
</style>
'''
st.markdown(page_bg, unsafe_allow_html=True)

# Sign Up Form UI
st.markdown('''
<div class="signup-box">
    <h1>Create an <span class="highlight">Account!</span></h1>
    <div class="signup-input">
        <input type="text" placeholder="👤 Username" />
    </div>
    <div class="signup-input">
        <input type="email" placeholder="📧 Email Address" />
    </div>
    <div class="signup-input">
        <input type="password" placeholder="🔒 Password" />
    </div>
    <div class="signup-input">
        <input type="password" placeholder="🔒 Confirm Password" />
    </div>
    <button class="btn">LOG IN</button>
    <div class="links">
        Already have an account? <a href="#">Sign in</a>
    </div>
</div>
''', unsafe_allow_html=True)
