import streamlit as st
import pandas as pd
from utils.data_quality import analyse_qualite_donnees, plot_missing_values

st.title("📊 Dashboard de Qualité des Données")

uploaded_file = st.file_uploader("📂 Chargez un fichier CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Aperçu des données")
    st.dataframe(df.head())

    st.subheader("Analyse qualité")
    stats = analyse_qualite_donnees(df)
    st.dataframe(stats)

    st.subheader("Visualisation des valeurs manquantes")
    plot_missing_values(df)
