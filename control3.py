import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_base.csv")

df['Horas_estudio'] = pd.to_numeric(df['Horas_estudio'], errors='coerce')
df['Nota'] = pd.to_numeric(df['Nota'], errors='coerce')

st.write("""
# Análisis de horas de estudio
## Relación entre dedicación y rendimiento académico
""")

with st.sidebar:
    st.write("## Ajustes")
    bins_usuario = st.slider("Selecciona número de bins para Horas de Estudio:", 1, 15, 5)
    st.write("Bins elegidos (Horas):", bins_usuario)
    
    bins_nota = st.slider("Selecciona número de bins para Notas:", 1, 15, 7)
    st.write("Bins de Nota elegidos:", bins_nota)

fig, axes = plt.subplots(1, 3, figsize=(15, 4)) 

axes[0].hist(df["Horas_estudio"], bins=bins_usuario, color='skyblue')
axes[0].set_title("1. Distribución de horas de estudio")
axes[0].set_xlabel("Horas de estudio")
axes[0].set_ylabel("Frecuencia")

axes[1].hist(df["Nota"], bins=bins_nota, color='salmon')
axes[1].set_title("2. Distribución de Notas")
axes[1].set_xlabel("Nota (escala 0-70)")
axes[1].set_ylabel("Frecuencia")

aprobado = df[df["Nota"] >= 40]
reprobado = df[df["Nota"] < 40]

cant_aprobado = len(aprobado)
cant_reprobado = len(reprobado)

axes[2].bar(["Aprobados", "Reprobados"], [cant_aprobado, cant_reprobado], color=["green", "red"])
axes[2].set_title("3. Comparación de resultados")
axes[2].set_xlabel("Categoría")
axes[2].set_ylabel("Cantidad")

st.pyplot(fig)

st.write("## Vista de los datos cargados")
st.table(df)