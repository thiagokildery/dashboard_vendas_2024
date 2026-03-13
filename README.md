# Dashboard de Vendas com Streamlit

Dashboard interativo para visualização e análise de dados de vendas, desenvolvido com Streamlit.

## Sobre o Projeto

Este projeto faz parte do meu aprendizado em criação de dashboards interativos com Python. O objetivo foi transformar análises de dados em uma aplicação web que pode ser usada por outras pessoas, sem precisar saber programar.

## Funcionalidades

- **Indicadores (KPIs):** Faturamento total, itens vendidos, margem média e número de transações
- **Filtros interativos:** Por categoria de produto e cidade
- **Gráficos:**
  - Faturamento por categoria
  - Distribuição da margem de lucro
  - Top 5 produtos mais vendidos
- **Exportação:** Download dos dados filtrados em formato Excel

## Arquivos do Projeto

| Arquivo | Descrição |
|---------|-----------|
| `04_dashboard_vendas.ipynb` | Notebook explicando o processo de criação |
| `dashboard_vendas.py` | Código do dashboard para executar |
| `dataset_completo_editado.xlsx` | Base de dados utilizada |

## Como Executar

1. Instale as dependências:
```bash
pip install pandas matplotlib seaborn streamlit xlsxwriter openpyxl
```

2. Coloque o arquivo de dados na mesma pasta do dashboard

3. Execute o dashboard:
```bash
streamlit run dashboard_vendas.py
```

4. O navegador abrirá automaticamente com o dashboard

## O que Aprendi

**Componentes do Streamlit:**
- `st.title()`, `st.markdown()` - textos e títulos
- `st.columns()` - organização em colunas
- `st.metric()` - indicadores numéricos
- `st.pills()` - filtros de seleção
- `st.pyplot()` - exibir gráficos
- `st.download_button()` - botão de download

**Performance:**
- `@st.cache_data` - evitar recarregar dados a cada interação

**Boas práticas:**
- Tratar casos onde filtros resultam em dados vazios
- Separar lógica de dados da visualização
- Manter o código organizado e legível

## Tecnologias Utilizadas

- Python 3
- Streamlit
- Pandas
- Matplotlib
- Seaborn

---

*Este projeto foi desenvolvido como parte dos meus estudos em análise de dados e criação de dashboards.*
