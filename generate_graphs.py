import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data():
    data = pd.read_csv('processed_data2.csv')
    data['nfc_label'] = data['nfc'].apply(lambda x: 'Sim' if x == 1 else 'Não')
    data['foldable_label'] = data['foldable'].apply(lambda x: 'Sim' if x == 1 else 'Não')
    data['cost_benefit_index'] = (data['ram'] + data['storage'] + data['battery'] + data['ppi_density']) / (data['price_usd'] + 1e-6)
    return data

def generate_graphs():
    data = load_data()
    
    # Create a directory to store the graphs
    if not os.path.exists('presentation/graphs'):
        os.makedirs('presentation/graphs')

    # Graph 1: Custo-Benefício Médio por Marca
    plt.figure(figsize=(12, 8))
    avg_brand_performance = data.groupby('phone_brand')['cost_benefit_index'].mean().sort_values(ascending=False)
    sns.barplot(x=avg_brand_performance.values, y=avg_brand_performance.index, hue=avg_brand_performance.index, palette='viridis', legend=False)
    plt.title('Custo-Benefício Médio por Marca', fontsize=16)
    plt.xlabel('Índice de Custo-Benefício', fontsize=12)
    plt.ylabel('Marca', fontsize=12)
    plt.tight_layout()
    plt.savefig('presentation/graphs/custo_beneficio_por_marca.png')
    plt.close()

    # Graph 2: Preço vs. Custo-Benefício
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x='price_usd', y='cost_benefit_index', hue='phone_brand', data=data, palette='tab10', s=100, alpha=0.7)
    plt.title('Preço vs. Custo-Benefício', fontsize=16)
    plt.xlabel('Preço (USD)', fontsize=12)
    plt.ylabel('Índice de Custo-Benefício', fontsize=12)
    plt.xscale('log') # Use log scale for better visualization of price distribution
    plt.grid(True, which="both", ls="--", c='0.7')
    plt.tight_layout()
    plt.savefig('presentation/graphs/preco_vs_custo_beneficio.png')
    plt.close()

    # Graph 3: RAM vs. Armazenamento (Storage)
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x='ram', y='storage', hue='price_range', data=data, palette='deep', s=100, alpha=0.7)
    plt.title('RAM vs. Armazenamento (Storage)', fontsize=16)
    plt.xlabel('RAM (GB)', fontsize=12)
    plt.ylabel('Armazenamento (GB)', fontsize=12)
    plt.grid(True, ls="--", c='0.7')
    plt.tight_layout()
    plt.savefig('presentation/graphs/ram_vs_armazenamento.png')
    plt.close()

    # Graph 4: Bateria vs. Tamanho da Tela
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x='display_size', y='battery', hue='price_range', data=data, palette='deep', s=100, alpha=0.7)
    plt.title('Bateria vs. Tamanho da Tela', fontsize=16)
    plt.xlabel('Tamanho da Tela (polegadas)', fontsize=12)
    plt.ylabel('Bateria (mAh)', fontsize=12)
    plt.grid(True, ls="--", c='0.7')
    plt.tight_layout()
    plt.savefig('presentation/graphs/bateria_vs_tela.png')
    plt.close()

    # Graph 5: Evolução Temporal do Custo-Benefício
    plt.figure(figsize=(12, 8))
    avg_yearly_performance = data.groupby('year')['cost_benefit_index'].mean().reset_index()
    sns.lineplot(x='year', y='cost_benefit_index', data=avg_yearly_performance, marker='o', palette='viridis', legend=False)
    plt.title('Evolução Temporal do Custo-Benefício', fontsize=16)
    plt.xlabel('Ano de Lançamento', fontsize=12)
    plt.ylabel('Custo-Benefício Médio', fontsize=12)
    plt.grid(True, ls="--", c='0.7')
    plt.tight_layout()
    plt.savefig('presentation/graphs/evolucao_temporal_custo_beneficio.png')
    plt.close()

    # Graph 6: Distribuição de Preço por Tipo de Tela
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='display_type', y='price_usd', data=data, palette='pastel')
    plt.title('Distribuição de Preço por Tipo de Tela', fontsize=16)
    plt.xlabel('Tipo de Tela', fontsize=12)
    plt.ylabel('Preço (USD)', fontsize=12)
    plt.grid(True, axis='y', ls="--", c='0.7')
    plt.tight_layout()
    plt.savefig('presentation/graphs/preco_por_tipo_tela.png')
    plt.close()

    # Graph 7: Distribuição de Preço por Sistema Operacional
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='os_type', y='price_usd', data=data, palette='pastel')
    plt.title('Distribuição de Preço por Sistema Operacional', fontsize=16)
    plt.xlabel('Sistema Operacional', fontsize=12)
    plt.ylabel('Preço (USD)', fontsize=12)
    plt.grid(True, axis='y', ls="--", c='0.7')
    plt.tight_layout()
    plt.savefig('presentation/graphs/preco_por_os.png')
    plt.close()

    # Graph 8: Custo-Benefício por Marca e Faixa de Preço
    plt.figure(figsize=(14, 8))
    avg_cb_by_brand_pricerange = data.groupby(['phone_brand', 'price_range'])['cost_benefit_index'].mean().reset_index()
    # Ensure consistent order for price_range
    price_order = ['low price', 'medium price', 'high price']
    avg_cb_by_brand_pricerange['price_range'] = pd.Categorical(avg_cb_by_brand_pricerange['price_range'], categories=price_order, ordered=True)
    avg_cb_by_brand_pricerange = avg_cb_by_brand_pricerange.sort_values(['phone_brand', 'price_range'])

    sns.barplot(x='phone_brand', y='cost_benefit_index', hue='price_range', data=avg_cb_by_brand_pricerange, palette='viridis')
    plt.title('Custo-Benefício Médio por Marca e Faixa de Preço', fontsize=16)
    plt.xlabel('Marca', fontsize=12)
    plt.ylabel('Índice de Custo-Benefício', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Faixa de Preço')
    plt.tight_layout()
    plt.savefig('presentation/graphs/custo_beneficio_por_marca_e_faixa_preco.png')
    plt.close()


if __name__ == '__main__':
    generate_graphs()