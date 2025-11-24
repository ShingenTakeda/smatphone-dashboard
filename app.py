import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    data = pd.read_csv('processed_data2.csv')
    data['nfc_label'] = data['nfc'].apply(lambda x: 'Sim' if x == 1 else 'Não')
    data['foldable_label'] = data['foldable'].apply(lambda x: 'Sim' if x == 1 else 'Não')
    data['cost_benefit_index'] = (data['ram'] + data['storage'] + data['battery'] + data['ppi_density']) / (data['price_usd'] + 1e-6)
    return data

data = load_data()

st.title('Smartphone Custo-Benefício Dashboard')

# --- Sidebar ---
st.sidebar.title("Filtros do Dashboard")
st.sidebar.markdown("Use os filtros abaixo para refinar os dados exibidos nos gráficos.")

st.sidebar.header('Filtros Principais', divider='rainbow')
st.sidebar.caption("Filtre por marca, faixa de preço e ano de lançamento.")
brands = st.sidebar.multiselect('Marca', options=data['phone_brand'].unique(), default=data['phone_brand'].unique())
price_ranges = st.sidebar.multiselect('Faixa de Preço', options=data['price_range'].unique(), default=data['price_range'].unique())
years = st.sidebar.multiselect('Ano de Lançamento', options=sorted(data['year'].unique()), default=sorted(data['year'].unique()))

with st.sidebar.expander("Filtros Avançados de Hardware"):
    st.caption("Filtre por especificações de hardware como tipo de tela, NFC, se é dobrável e fabricante do processador.")
    display_types = st.multiselect('Tipo de Tela', options=data['display_type'].dropna().unique(), default=data['display_type'].dropna().unique())
    nfc_options = st.multiselect('NFC', options=data['nfc_label'].unique(), default=data['nfc_label'].unique())
    foldable_options = st.multiselect('Dobrável', options=data['foldable_label'].unique(), default=data['foldable_label'].unique())
    chip_companies = st.multiselect('Fabricante do Chipset', options=data['chip_company'].dropna().unique(), default=data['chip_company'].dropna().unique())

with st.sidebar.expander("Filtros de Software"):
    st.caption("Filtre pelo sistema operacional do aparelho.")
    os_types = st.multiselect('Sistema Operacional', options=data['os_type'].dropna().unique(), default=data['os_type'].dropna().unique())


# Filter data
filtered_data = data[
    (data['phone_brand'].isin(brands)) &
    (data['price_range'].isin(price_ranges)) &
    (data['year'].isin(years)) &
    (data['display_type'].isin(display_types)) &
    (data['nfc_label'].isin(nfc_options)) &
    (data['foldable_label'].isin(foldable_options)) &
    (data['chip_company'].isin(chip_companies)) &
    (data['os_type'].isin(os_types))
]

# --- Dashboard Body ---

st.header('Visão Geral')
if not filtered_data.empty:
    # Calculate overall averages from the original dataframe
    overall_avg_price = data['price_usd'].mean()
    overall_avg_cost_benefit = data['cost_benefit_index'].mean()
    
    # Calculate filtered averages
    filtered_avg_price = filtered_data['price_usd'].mean()
    filtered_avg_cost_benefit = filtered_data['cost_benefit_index'].mean()

    # Calculate deltas
    delta_price = filtered_avg_price - overall_avg_price
    delta_cost_benefit = filtered_avg_cost_benefit - overall_avg_cost_benefit

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Smartphones Encontrados", f"{len(filtered_data)}")
    with col2:
        st.metric("Preço Médio (USD)", f"${filtered_avg_price:,.2f}", f"${delta_price:,.2f}", help="A seta indica a diferença em relação à média de todos os smartphones no dataset.")
    with col3:
        st.metric("Custo-Benefício Médio", f"{filtered_avg_cost_benefit:,.2f}", f"{delta_cost_benefit:,.2f}", help="A seta indica a diferença em relação à média de todos os smartphones no dataset.")
else:
    st.warning("Nenhum smartphone encontrado com os filtros selecionados.")

st.markdown("---")

if not filtered_data.empty:
    # Row 2: Main Analysis
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Custo-Benefício Médio por Marca')
        avg_brand_performance = filtered_data.groupby('phone_brand')['cost_benefit_index'].mean().sort_values(ascending=False)
        st.bar_chart(avg_brand_performance)

    with col2:
        st.subheader('Preço vs. Custo-Benefício')
        chart = alt.Chart(filtered_data).mark_circle(size=70, opacity=0.7).encode(
            x=alt.X('price_usd:Q', title='Preço (USD)', axis=alt.Axis(format='$,.0f')),
            y=alt.Y('cost_benefit_index:Q', title='Índice de Custo-Benefício'),
            color='phone_brand:N',
            tooltip=['phone_model', 'phone_brand', 'price_usd', 'cost_benefit_index']
        ).interactive()
        st.altair_chart(chart, use_container_width=True)

    st.markdown("---")

    # Row 3: Hardware Specification Analysis
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('RAM vs. Armazenamento (Storage)')
        chart = alt.Chart(filtered_data).mark_circle(size=70, opacity=0.7).encode(
            x=alt.X('ram:Q', title='RAM (GB)'),
            y=alt.Y('storage:Q', title='Armazenamento (GB)'),
            color='price_range:N',
            tooltip=['phone_model', 'ram', 'storage', 'price_range']
        ).interactive()
        st.altair_chart(chart, use_container_width=True)

    with col2:
        st.subheader('Bateria vs. Tamanho da Tela')
        chart = alt.Chart(filtered_data).mark_circle(size=70, opacity=0.7).encode(
            x=alt.X('display_size:Q', title='Tamanho da Tela (polegadas)'),
            y=alt.Y('battery:Q', title='Bateria (mAh)'),
            color='price_range:N',
            tooltip=['phone_model', 'display_size', 'battery', 'price_range']
        ).interactive()
        st.altair_chart(chart, use_container_width=True)

    st.markdown("---")

    # Row 4: Temporal Evolution and Custom Correlation
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Evolução Temporal do Custo-Benefício')
        avg_yearly_performance = filtered_data.groupby('year')['cost_benefit_index'].mean().reset_index()
        chart = alt.Chart(avg_yearly_performance).mark_line(point=True).encode(
            x=alt.X('year:O', title='Ano de Lançamento'),
            y=alt.Y('cost_benefit_index:Q', title='Custo-Benefício Médio'),
            tooltip=['year', 'cost_benefit_index']
        ).interactive()
        st.altair_chart(chart, use_container_width=True)

    with col2:
        st.subheader('Análise de Correlação Customizada')
        numeric_columns = ['price_usd', 'ram', 'storage', 'battery', 'ppi_density', 'display_size', 'weight']
        x_axis = st.selectbox('Eixo X', options=numeric_columns, index=0)
        y_axis = st.selectbox('Eixo Y', options=numeric_columns, index=1)
        if x_axis and y_axis:
            chart = alt.Chart(filtered_data).mark_circle(size=70, opacity=0.7).encode(
                x=alt.X(x_axis, type='quantitative'),
                y=alt.Y(y_axis, type='quantitative'),
                color='phone_brand:N',
                tooltip=['phone_model', x_axis, y_axis]
            ).interactive()
            st.altair_chart(chart, use_container_width=True)
            
    st.markdown("---")

    # Row 5: Categorical Analysis
    st.header("Análise Categórica")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Distribuição de Preço por Tipo de Tela')
        chart = alt.Chart(filtered_data).mark_boxplot(extent='min-max').encode(
            x=alt.X('display_type:N', title='Tipo de Tela'),
            y=alt.Y('price_usd:Q', title='Preço (USD)', axis=alt.Axis(format='$,.0f')),
            color=alt.Color('display_type:N', legend=None)
        )
        st.altair_chart(chart, use_container_width=True)

    with col2:
        st.subheader('Distribuição de Preço por Sistema Operacional')
        chart = alt.Chart(filtered_data).mark_boxplot(extent='min-max').encode(
            x=alt.X('os_type:N', title='Sistema Operacional'),
            y=alt.Y('price_usd:Q', title='Preço (USD)', axis=alt.Axis(format='$,.0f')),
            color=alt.Color('os_type:N', legend=None)
        )
        st.altair_chart(chart, use_container_width=True)
            
    st.markdown("---")

    # Row 6: Detailed Brand Segment Analysis
    st.header("Análise de Segmentos por Marca")
    avg_cb_by_brand_pricerange = filtered_data.groupby(['phone_brand', 'price_range'])['cost_benefit_index'].mean().reset_index()

    chart = alt.Chart(avg_cb_by_brand_pricerange).mark_bar().encode(
        x=alt.X('phone_brand:N', title='Marca', sort='-y'),
        y=alt.Y('cost_benefit_index:Q', title='Custo-Benefício Médio'),
        color=alt.Color('price_range:N', title='Faixa de Preço', sort=['low price', 'medium price', 'high price']),
        tooltip=['phone_brand', 'price_range', 'cost_benefit_index']
    ).properties(
        title='Custo-Benefício Médio por Marca e Faixa de Preço'
    ).interactive()
    
    st.altair_chart(chart, use_container_width=True)