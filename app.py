import streamlit as st
from data import load_data
from nlp_utils import extract_budget, extract_category, extract_features, extract_brand
from recommender import recommend_products
from styles import load_css

# -------------------------------
# Page Setup
# -------------------------------
st.set_page_config(page_title="AI Shopping Assistant", layout="wide")

# Load CSS
st.markdown(load_css(), unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🛍️ AI Product Recommendation Chatbot</div>', unsafe_allow_html=True)

# Load Data
df = load_data()

# Chat Memory
if "chat" not in st.session_state:
    st.session_state.chat = []

# Input
user_input = st.text_input("💬 Ask something (e.g., 'gaming laptop under 60000')")

if st.button("Send") and user_input:
    st.session_state.chat.append(("user", user_input))

    text = user_input.lower()

    category = extract_category(text)
    budget = extract_budget(text)
    features = extract_features(text)
    brand = extract_brand(text)

    results = recommend_products(df, category, budget, features, brand)

    if not category and not brand:
        st.session_state.chat.append(("bot", "⚠️ Please specify a category or brand."))

    elif results.empty:
        st.session_state.chat.append(("bot", "❌ No products found."))

    else:
        st.session_state.chat.append(("bot", "✅ Here are your recommendations:"))
        st.session_state.chat.append(("products", results))

# Display Chat
for msg_type, msg in st.session_state.chat:
    if msg_type == "user":
        st.markdown(f'<div class="user-bubble">🧑 {msg}</div>', unsafe_allow_html=True)

    elif msg_type == "bot":
        st.markdown(f'<div class="bot-bubble">🤖 {msg}</div>', unsafe_allow_html=True)

    elif msg_type == "products":
        cols = st.columns(3)
        for i, (_, row) in enumerate(msg.iterrows()):
            with cols[i % 3]:
                st.markdown(f"""
                <div class="product-card">
                    <h4>{row['name']}</h4>
                    <p><b>Price:</b> ₹{row['price']}</p>
                    <p><b>Features:</b> {row['features']}</p>
                </div>
                """, unsafe_allow_html=True)