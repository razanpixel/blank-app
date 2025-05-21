import streamlit as st

st.write("🎈~WARZO~")
st.write(
    "warzo_all_the_time."
)
st.image("Screenshot_20250423-175640~2.png")

st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap")
else:
st.write(f"{angka} adalah bilangan ganjil")
