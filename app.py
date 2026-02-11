import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

datasets = sns.get_dataset_names()

st.title("Bienvenue sur le site web", text_alignment = "center")
st.title("de Dominique\n", text_alignment = "center")
st.header("MANIPULATION DE DONNEES", text_alignment = "center")
st.header("et", text_alignment = "center")
st.header("CREATION DE GRAPHIQUES", text_alignment = "center")

dataset = st.selectbox("Quel dataset veux-tu utiliser ?",
             datasets) 
st.write('___')
df = sns.load_dataset(dataset)
st.dataframe(df)

x = st.selectbox("Quelle colonne pour x ?",
             df.columns) 
st.write('___')

y = st.selectbox("Quelle colonne pour y ?",
             df.columns) 
st.write('___')

visu = st.selectbox("Quel type de graphique ?",["Line Plot",
                                                "Bar Plot",
                                                "Scatter Plot"])

fig, ax = plt.subplots()

if visu == "Line Plot":
    sns.lineplot(data=df, x=x, y=y, ax=ax)
elif visu == "Bar Plot":
    sns.barplot(data=df, x=x, y=y, ax=ax)
elif visu == "Scatter Plot":
    sns.scatterplot(data=df, x=x, y=y, ax=ax)

st.pyplot(fig)

matCorr = st.checkbox("Afficher la matrice de corrélation ?")

if matCorr:
    corr_matrix = df.select_dtypes(include=['number']).corr()
    st.write("### Matrice de corrélation (tableau) :")
    st.dataframe(corr_matrix)
    st.write("### Matrice de corrélation (heatmap) :")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_matrix,
                annot=True,  # Afficher les valeurs dans les cases
                cmap="coolwarm",  # Palette de couleurs
                center=0,  # Centrer la palette sur 0
                ax=ax)
    st.pyplot(fig)

