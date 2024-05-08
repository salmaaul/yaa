import streamlit as st

# Electron configuration for atoms 1-118
electron_config = {
    1: "1s1",
    2: "1s2",
    3: "1s2 2s1",
    #... up to 118
}

st.title("Electron Configuration")
st.write("Select an atomic number:")

atomic_number = st.selectbox("Atomic Number", list(electron_config.keys()))

st.write("Electron Configuration:")
st.write(electron_config[atomic_number])