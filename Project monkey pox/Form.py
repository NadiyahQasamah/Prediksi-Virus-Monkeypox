import streamlit as st
import pickle
import numpy as np

with open('MP.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
    
## Fungsi untuk prediksi data baru
def predict_loan_status(features):
    prediction = loaded_model.predict([features])
    return prediction[0]

st.markdown(
    """
    <h1 style="text-align: center; color:#404040;">Penyebaran Virus Cacar Monyet di Dunia</h1>
    """,
    unsafe_allow_html=True
)

# Menggunakan layout columns untuk menengahkan gambar
col1, col2, col3 = st.columns([2, 8, 2])

with col2:
    st.image("OIP.jpg", caption="Virus Cacar Monyet")

Age = st.number_input('Berapa umur kamu?', min_value=1, max_value = 100, value=1)

Panile_Oedema = st.selectbox('Apakah terjadi pembekakan di penis?', [True, False])
Oral_Lesions = st.selectbox('Apakah timbul lesi pada mulut?', [True, False])
Solitary_Lesion = st.selectbox('Apakah timbul Lesi Soliter?', [True, False])
Swollen_Tonsils  = st.selectbox('Apakah terjadi Pembengkakan pada Amandel?', [True, False])
HIV_Infection = st.selectbox('Apakah terindikasi Infeksi HIV?', [True, False])
Sexually_Transmitted_Infection = st.selectbox('Apakah memiliki penyakit seksual?', [True, False])
Systemic_Illness_Fever = st.selectbox('Apakah mengalami demam?', [True, False])
Systemic_Illness_Muscle_Aches_and_Pain = st.selectbox('Apakah anda mengalami nyeri?', [True, False])
Systemic_Illness_None = st.selectbox('Apakah anda memiliki gejala sistemik?', [True, False])
Systemic_Illness_Swollen_Lymph_Nodes = st.selectbox('Apakah terjadi pembekakan kelenjar getah bening?', [True, False])



## Tombol untuk prediksi
if st.button('Prediksi'):
    ## Membuat array dari input
    features = np.array([Panile_Oedema, Oral_Lesions, Solitary_Lesion, Swollen_Tonsils, HIV_Infection, 
                         Sexually_Transmitted_Infection, Systemic_Illness_Fever, Systemic_Illness_Muscle_Aches_and_Pain, 
                         Systemic_Illness_None, Systemic_Illness_Swollen_Lymph_Nodes])
    
    ## Melakukan prediksi
    prediction = predict_loan_status(features)
    
    ## Menampilkan hasil prediksi
    st.write(f'Prediksi : {"Positif" if prediction == 1 else "Negatif"}')