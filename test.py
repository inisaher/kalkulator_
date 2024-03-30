import streamlit as st

st.header('Aplikasi Penjumlahan Bilangan Numerik', divider='rainbow')

angka_pertama = st.number_input('masukan angka pertama')
st.write('The frist number is ', angka_pertama)

angka_kedua = st.number_input('masukan angka kedua')
st.write('The second number is ', angka_kedua)

operasi_matematika = angka_pertama * angka_kedua
st.write(f'angka pertama{angka_pertama} x {angka_kedua} = {operasi_matematika}')