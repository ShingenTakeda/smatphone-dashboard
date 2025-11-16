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


