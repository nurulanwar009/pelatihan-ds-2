import streamlit as st
import joblib
import numpy as np

# Memuuat model regresi linier yang sudah disimpan
lin_reg_load = joblib.load('lin_reg_model.joblib')

# judul aplikasi
st.title("Prediksi Gaji Berdasarkan Lama Bekerja")

# Input tahun pengalaman kerja
years_experience = st.number_input("Masukan jumlah tahun bekerja:", min_value=0.0, step=0.1)

# Prediksi gaji
if st.button("Prediksi Gaji"):
	gaji = lin_reg_loaded.predict([[years_experience]])
	st.write(f"Gaji seorang setelah bekerja selama {years_experience} tahun adalah ${gaji[0]:,.sf}") 
