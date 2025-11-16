
import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('processed_data2.csv')
    return data

data = load_data()

# Calculate Cost-Benefit Index
# Formula: (RAM + storage + BATTERY + PPI_Density) / price_USD
# Adding a small epsilon to price to avoid division by zero
data['cost_benefit_index'] = (data['ram'] + data['storage'] + data['battery'] + data['ppi_density']) / (data['price_usd'] + 1e-6)

st.title('Smartphone Custo-Benefício Dashboard')

st.write("""
O propósito deste dashboard de Business Intelligence é servir como uma **ferramenta estratégica de decisão de compra** no mercado de smartphones. Ele é projetado para transformar dados técnicos complexos e preços dispersos em **insights acionáveis e de fácil compreensão**.
""")

# Sidebar filters
st.sidebar.header('Filtros')
brands = st.sidebar.multiselect('Marca', options=data['phone_brand'].unique(), default=data['phone_brand'].unique())
price_ranges = st.sidebar.multiselect('Faixa de Preço', options=data['price_range'].unique(), default=data['price_range'].unique())
years = st.sidebar.multiselect('Ano de Lançamento', options=sorted(data['year'].unique()), default=sorted(data['year'].unique()))

# Filter data
filtered_data = data[
    (data['phone_brand'].isin(brands)) &
    (data['price_range'].isin(price_ranges)) &
    (data['year'].isin(years))
]

# Display filtered data
st.header('Análise de Custo-Benefício')
st.write(f'{len(filtered_data)} smartphones encontrados.')

sorted_data = filtered_data.sort_values('cost_benefit_index', ascending=False)

st.dataframe(sorted_data[[
    'phone_brand', 'phone_model', 'price_usd', 'cost_benefit_index', 'ram', 'storage', 'battery', 'ppi_density', 'year', 'price_range'
]])

# Scatter plot
st.header('Preço vs. Custo-Benefício')
st.scatter_chart(
    data=sorted_data,
    x='price_usd',
    y='cost_benefit_index',
    color='phone_brand'
)
