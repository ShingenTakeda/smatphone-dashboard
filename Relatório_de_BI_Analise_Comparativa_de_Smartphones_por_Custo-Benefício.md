# **![][image1]**

**Relatório de BI: Análise Comparativa de Smartphones por Custo-Benefício**

**Responsáveis:**  
Mariana Carneiro \- 2219168  
João Paolo Cavalcante Martins Oliveira \- 2010387  
Gustavo Mitsuo Fernandes Valente Takeda \- 2218547  
Iandra Gabriele \- 2217710

Definição do Problema e Objetivos do Dashboard.…………………..…………………1

      Propósito do Dashboard.………………………………………………..….………………..1

      Definição dos Pontos a Serem Abordados no Dashboard…………………...…..1

Diagnóstico dos Processos………………………………………………………..……………..3

      Processos Críticos Identificados………………………………………..………………..3

      Processos ITIL Selecionados para Análise……………….………………….………..3

Proposição de Indicadores (KPIs)……………………………………………………..……...4

      KPIs para Gerenciamento de Incidentes e Problemas….………………………..4

      KPIs para Gerenciamento de Capacidade…………………………………….…......4

Aplicação do Balanced Scorecard (BSC).……………………………………………………5

      BSC da Galactic Foods…………………………………………………………..……………5     Análise e Plano de Ação..………………………………………………………………………...6

      Análise dos Resultados Simulados…………...………………………………………...6

      Gargalos Identificados……………………………………………………………………....6

      Planos de Ação Recomendados……………………………………….…….…………...6

Conclusões e Recomendações…………………………………………………………………7

      Conclusões……………………………………………………………………………………….7  
      Recomendações Estratégicas……………………………………………………………..7

1. **Definição do Problema e Objetivos do Dashboard**  
   1. **Propósito do Dashboard**

O propósito deste dashboard de Business Intelligence é servir como uma **ferramenta estratégica de decisão de compra** no mercado de smartphones. Ele é projetado para transformar dados técnicos complexos e preços dispersos em **insights acionáveis e de fácil compreensão**.

O dashboard auxilia na tomada de decisão de duas maneiras principais:

1. **Para o Consumidor Final:** Atua como um "consultor virtual", permitindo que usuários identifiquem rapidamente os modelos que oferecem o **melhor equilíbrio (balanceamento) entre custo e desempenho** dentro de seu orçamento. Em vez de analisar dezenas de especificações técnicas manualmente, o usuário pode visualizar de forma interativa quais celulares oferecem "mais pelo seu dinheiro", otimizando seu processo de escolha e garantindo uma compra mais satisfatória.  
2. **Para Profissionais do Varejo e Análise de Mercado:** Ajuda a **identificar oportunidades de mercado e tendências**. Por exemplo, um varejista pode usar o dashboard para montar um portfólio de produtos com boa relação custo-benefício, atraindo assim um público maior. A análise pode revelar quais marcas estão dominando certas faixas de preço ou se há uma lacuna no mercado para specs específicas, auxiliando na definição de estratégias de vendas e marketing.

Em resumo, o dashboard propõe ações baseadas nos dados ao responder diretamente à pergunta: **"Dado o meu orçamento, qual celular me oferece o conjunto de características técnicas mais robusto e balanceado?"**

2. **Definição dos Pontos a Serem Abordados no Dashboard**

Para cumprir seu propósito, o dashboard se baseará nas seguintes variáveis, dados e métricas, explorando as correlações entre eles:

**Variáveis e Dados Principais:**

|  Preço  | price\_USD | A variável central de custo, já convertida para USD, permitindo comparações diretas entre dispositivos. |
| :---: | :---- | :---- |
|  **Especificações Técnicas (Features)** | RAM e storage | Indicadores diretos de performance multitarefa e capacidade de armazenamento. |
|  | BATTERY | Capacidade da bateria em mAh, fator crucial para autonomia do dispositivo. |
|  | Chipset, CPU e GPU | O "cérebro" do dispositivo, determinando poder de processamento e performance gráfica. |
|  | Display\_Size e PPI\_Density | Tamanho da tela em polegadas e densidade de pixels para qualidade visual. |
|  | Display\_Type | Tecnologia do display (ex: OLED, IPS) que impacta na qualidade de imagem. |
|  | NFC | Flag (0/1) que indica presença de tecnologia para pagamentos sem contato. |
|  | OS | Sistema operacional e versão, importante para compatibilidade e experiência do usuário. |
|  **Metadados** | phone\_brand | Para análise comparativa entre marcas e identificação de padrões por fabricante. |
|  | Year e Launch | Para entender a evolução temporal dos lançamentos e identificar tendências. |
|  | price\_range |  Classificação fornecida pelo dataset (low/medium/high) baseada nos quantis, essencial para segmentação. |
|  | Foldable | Flag (0/1) que identifica dispositivos dobráveis, um segmento de mercado específico. |
|  | Weight e Dimensions | Peso e dimensões do aparelho, relevantes para portabilidade e ergonomia. |

**Metas e Métricas Derivadas:**

* **Meta Principal**: Criar um **"Índice de Custo-Benefício"** ou **"Score de Balanceamento"**. Esta métrica será calculada combinando as especificações técnicas mais relevantes (normalizadas) e dividindo pelo preço. Por exemplo:  
  * **Fórmula proposta:** (RAM \+ storage \+ BATTERY \+ PPI\_Density) / price\_USD  
  * Os modelos com os **scores mais altos** serão classificados como os **"mais balanceadamente melhores"**.  
* **Segmentação Estratégica:**  
  * Utilizar a coluna price\_range para comparar dispositivos dentro de segmentos de mercado similares (ex: identificar os melhores custo-benefício exclusivamente na faixa "low price").  
  * **Análise por Marca**: Comparar o desempenho médio das marcas em cada faixa de preço.  
  * **Evolução Temporal**: Analisar como o custo-benefício evoluiu ao longo dos anos (Year).

**Correlação entre os Dados:**

O dashboard explorará visualmente as correlações entre:

* **Preço vs. Especificações:** Para identificar dispositivos que fogem da tendência esperada (alta especificação a preço baixo).  
* **Especificações entre si:** Para entender trade-offs comuns (ex: dispositivos com muita RAM tendem a ter bateria menor?).  
* **Marca vs. Score de Custo-Benefício:** Para identificar quais fabricantes consistentemente oferecem melhor balanceamento.

[image1]: <data:image/png;base64,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>