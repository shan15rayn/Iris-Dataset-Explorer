import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\wen\1 工作 Work\Universiti Teknologi PETRONAS\Study\2 Undergraduate\Y1S2 Sept 25\Data Visualization\Lab\CODE\iris.csv")
    return df

df = load_data()
df.columns = ['Sepal Length (cm)', 'Sepal Width (cm)', 'Petal Length (cm)', 'Petal Width (cm)', 'Species']

st.sidebar.header("Filters")

st.sidebar.subheader("Select Species:")
species_list = df['Species'].unique()
selected_species = []

for species in species_list:
    if st.sidebar.checkbox(species, value=True, key=species):
        selected_species.append(species)

filtered_df = df[df['Species'].isin(selected_species)]

st.title("Iris Dataset Explorer")
st.write("An interactive app to explore the famous Iris dataset.")

st.subheader("Data Summary Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Samples", len(filtered_df))
col2.metric("Number of Features", len(df.columns)-1)
col3.metric("Number of Species", filtered_df['Species'].nunique())

st.subheader("Filtered Data")
st.dataframe(filtered_df)

st.subheader("Scatter Plot of Sepal Length vs Sepal Width")
fig_scatter = px.scatter(
    filtered_df,
    x='Sepal Length (cm)',
    y='Sepal Width (cm)',
    color='Species',
    size='Petal Length (cm)',
    hover_data=['Petal Width (cm)'],
    color_discrete_sequence=px.colors.qualitative.Set2,
)
st.plotly_chart(fig_scatter, use_container_width=True)

st.subheader("Histogram of Petal Length")
fig, ax = plt.subplots()
sns.histplot(
    data=filtered_df,
    x='Petal Length (cm)',
    hue='Species',
    multiple='stack',
    palette='Set2'
)
ax.set_title("Distribution of Petal Length by Species")
st.pyplot(fig) 