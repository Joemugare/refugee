import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv('C:\\Users\\Qunta\\Desktop\\PYTHON CODES\\Streamlit Projects\\UN Refugee\\Un Refugee.csv')


# Replace 'Unknown' with NaN
df.replace('Unknown', np.nan, inplace=True)

# Convert columns to numeric (ignoring non-numeric values)
df_numeric = df.apply(pd.to_numeric, errors='coerce') 

# Page title
st.markdown(
    """
    <div style="background-color:#f8f9fa;padding:10px;border-radius:10px;margin-bottom:20px">
        <h1 style="color:#007bff;text-align:center;">UNHCR Dataset Analysis</h1>
        <p style="font-size:18px;color:#6c757d;text-align:center;">Explore insights from the UNHCR dataset</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar with filtering options
st.sidebar.header('Filter Data')
selected_year = st.sidebar.slider('Select Year', min_value=int(df['Year'].min()), max_value=int(df['Year'].max()), value=int(df['Year'].min()))
filtered_data = df[df['Year'] == selected_year]

# Display a sample of the filtered data
st.subheader(f'Displaying data for the year {selected_year}')
st.write(filtered_data.head())

# Analyze the distribution of refugees
st.subheader('Distribution of Refugees by Country of Origin')
fig, ax = plt.subplots(figsize=(35, 25))
sns.barplot(x='Refugees under UNHCR\'s mandate', y='Country of origin', data=filtered_data, palette='viridis', ax=ax)
ax.set_title('Refugees by Country of Origin', fontsize=30)
ax.set_xlabel('Number of Refugees', fontsize=26)
ax.set_ylabel('Country of Origin', fontsize=26)
plt.xticks(fontsize=22, rotation=45, ha='right')
plt.yticks(fontsize=22)
st.pyplot(fig)

# Analyze the distribution of asylum-seekers
st.subheader('Distribution of Asylum-Seekers by Country of Asylum')
fig, ax = plt.subplots(figsize=(22, 15))
sns.barplot(x="Asylum-seekers", y='Country of asylum', data=df, palette='viridis', ax=ax)
ax.set_title('Asylum-Seekers by Country of Asylum', fontsize=20)
ax.set_xlabel('Number of Asylum-Seekers', fontsize=16)
ax.set_ylabel('Country of Asylum', fontsize=16)
plt.xticks(fontsize=12, rotation=45, ha='right')
plt.yticks(fontsize=12)
st.pyplot(fig)

# Correlation Heatmap
st.subheader('Correlation Heatmap')
fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(df_numeric.corr(), annot=True, cmap='coolwarm', linewidths=.5, ax=ax)
ax.set_title('Correlation Heatmap')
st.pyplot(fig)