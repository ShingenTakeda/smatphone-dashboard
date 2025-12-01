---
title: Análise de Custo-Benefício de Smartphones
author: Mariana Carneiro, João Paolo Cavalcante, Gustavo Mitsuo, Iandra Gabriele
---

## Visão Geral do Projeto

Este projeto apresenta um dashboard interativo de Business Intelligence para análise comparativa de smartphones, focado na relação custo-benefício.

O objetivo é transformar dados técnicos complexos e preços em insights acionáveis e de fácil compreensão para consumidores e profissionais do mercado.

<!-- end_slide -->

Problema
---

O mercado de smartphones é saturado de opções, tornando a escolha do aparelho ideal uma tarefa complexa.

* **Consumidores:** Dificuldade em comparar especificações técnicas e encontrar o melhor valor pelo dinheiro.
* **Varejistas:** Desafio em identificar tendências de mercado e otimizar o portfólio de produtos.

<!-- end_slide -->

Solução
---

Um dashboard interativo desenvolvido com Streamlit que serve como um "consultor virtual".

Ele permite aos usuários:
* Filtrar smartphones por marca, preço, ano e especificações.
* Visualizar e comparar aparelhos através de gráficos interativos.
* Identificar rapidamente os modelos com o melhor custo-benefício.

<!-- pause -->

```python
# app.py
import streamlit as st
import pandas as pd
import altair as alt

st.title('Smartphone Custo-Benefício Dashboard')

# ... (código do dashboard)
```

<!-- end_slide -->

Features principais
---

O dashboard oferece uma variedade de filtros e visualizações:

* **Filtros:** Marca, faixa de preço, ano, tipo de tela, NFC, etc.
* **Métricas:** Preço médio, custo-benefício médio.
* **Gráficos:**
    * Custo-benefício por marca.
    * Preço vs. Custo-benefício.
    * RAM vs. Armazenamento.
    * Bateria vs. Tamanho da tela.
    * Evolução temporal do custo-benefício.

<!-- end_slide -->

Índice de Custo-Benefício
---

O núcleo da análise é o "Índice de Custo-Benefício", uma métrica que resume a performance de um smartphone em relação ao seu preço.

```python
# Fórmula do Índice de Custo-Benefício
cost_benefit_index = (ram + storage + battery + ppi_density) / price_usd
```

<!-- pause -->

Essa métrica permite uma comparação justa e objetiva entre diferentes modelos e marcas.

<!-- end_slide -->

Tecnologias Utilizadas
---

<!-- column_layout: [2, 3] -->

<!-- column: 0 -->

O projeto foi desenvolvido utilizando tecnologias de código aberto:

* **Python:** Linguagem de programação principal.
* **Pandas:** Para manipulação e análise de dados.
* **Streamlit:** Para a criação do dashboard interativo.
* **Altair:** Para a geração de gráficos declarativos.

<!-- column: 1 -->

```python
# pyproject.toml
[tool.poetry.dependencies]
python = "^3.11"
pandas = "^2.2.2"
streamlit = "^1.35.0"
altair = "^5.3.0"
```

<!-- reset_layout -->

<!-- end_slide -->

Visualizações do Dashboard
---

O dashboard dá vida aos dados com uma variedade de gráficos interativos:

*   **Custo-Benefício por Marca:** Um gráfico de barras que classifica as marcas pelo seu índice de custo-benefício médio, revelando quais fabricantes oferecem o melhor valor.
*   **Preço vs. Custo-Benefício:** Um gráfico de dispersão que ajuda a identificar outliers — smartphones que oferecem um alto benefício por um baixo custo.
*   **Análise de Hardware:** Gráficos que correlacionam especificações importantes, como RAM vs. Armazenamento e Bateria vs. Tamanho da Tela, para entender os trade-offs de engenharia.
*   **Evolução Temporal:** Um gráfico de linha que mostra como o custo-benefício médio dos smartphones evoluiu ao longo dos anos.

<!-- end_slide -->

Conclusão
---

Este projeto demonstra como a análise de dados e a visualização podem capacitar a tomada de decisões no mercado de tecnologia.

O dashboard oferece uma ferramenta poderosa para consumidores e profissionais, trazendo clareza e transparência para a escolha de smartphones.
