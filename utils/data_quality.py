import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def analyse_qualite_donnees(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        'Type': df.dtypes,
        'N valeurs manquantes': df.isnull().sum(),
        '% manquant': df.isnull().mean() * 100,
        'N valeurs uniques': df.nunique(),
        'N doublons': df.duplicated().sum()
    })

def plot_missing_values(df: pd.DataFrame):
    plt.figure(figsize=(10, 5))
    sns.heatmap(df.isnull(), cbar=False, yticklabels=False)
    st.pyplot(plt.gcf())
