import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import streamlit as st 

# Configuração da página
st.set_page_config(page_title='Dashboard de Vendas', layout='wide')

# Carregamento otimizado dos dados
@st.cache_data
def carregar_dados():
    df = pd.read_excel('dataset_completo_editado.xlsx')
    return df

df = carregar_dados()

# Título e período
st.title("Dashboard de Vendas")
st.markdown(f"**Período:** {df['Data'].min().strftime('%d/%m/%Y')} a {df['Data'].max().strftime('%d/%m/%Y')}")

# Filtros
col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    categoria_sel = st.pills(
        "Categoria",
        df['Categoria'].unique(),
        default=df['Categoria'].unique(),
        selection_mode='multi'
    )

with col2:
    cidade_sel = st.pills(
        "Cidade",
        df['Cidade'].unique(),
        default=df['Cidade'].unique(),
        selection_mode='multi'
    )

# Aplicando filtros
if not categoria_sel or not cidade_sel: 
    df_filtrado = pd.DataFrame()
else: 
    df_filtrado = df[
        (df['Categoria'].isin(categoria_sel)) &
        (df['Cidade'].isin(cidade_sel))
    ]

# KPIs
st.subheader('Resumo Executivo')
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_vendas = df['Valor_Total'].sum()
    st.metric(label='Faturamento Total', value=f'R$ {total_vendas:,.2f}')

with col2:
    qtd_itens = df['Quantidade'].sum()
    st.metric(label='Itens Vendidos', value=f'{qtd_itens:,}')

with col3:
    media_margem = df['Margem_Lucro'].mean()
    st.metric(label='Margem Média', value=f'{media_margem:.1f}')

with col4:
    num_transacoes = df.shape[0]
    st.metric(label="Nº de Transações", value=num_transacoes)

st.divider()

# Gráficos
st.subheader("Visualizações")

chart_col1, chart_col2 = st.columns(2)

# Faturamento por categoria
with chart_col1:
    st.markdown("**Faturamento por Categoria**")
    fig1, ax1 = plt.subplots(figsize=(7, 5))
    if not df_filtrado.empty:
        sns.barplot(data=df_filtrado, x='Categoria', y='Valor_Total', 
                    estimator=sum, ax=ax1, palette='viridis')
        ax1.set_ylabel("Valor Total (R$)")
        ax1.set_xlabel("")
    else: 
        ax1.text(0.5, 0.5, "Sem dados para exibir", ha='center', va='center')
    st.pyplot(fig1)
    plt.close()

# Distribuição da margem
with chart_col2:
    st.markdown("**Distribuição da Margem de Lucro**")
    fig2, ax2 = plt.subplots(figsize=(5, 3))
    if not df_filtrado.empty:
        sns.histplot(df_filtrado['Margem_Lucro'] * 100, bins=10, kde=True, 
                     ax=ax2, color='green')
        ax2.set_xlabel("Margem (%)")
        ax2.set_ylabel("Frequência")
    else: 
        ax2.text(0.5, 0.5, "Sem dados para exibir", ha='center', va='center')
    st.pyplot(fig2)
    plt.close()

# Top 5 produtos
st.markdown("**Top 5 Produtos Mais Vendidos**")
fig3, ax3 = plt.subplots(figsize=(8, 4))
if not df_filtrado.empty:
    top_produtos = df_filtrado.groupby('Produto')['Valor_Total'].sum().sort_values(ascending=False).head(5)
    sns.barplot(x=top_produtos.values, y=top_produtos.index, ax=ax3, palette='viridis')
    ax3.set_xlabel("Faturamento (R$)")
    ax3.set_ylabel("")
else: 
    ax3.text(0.5, 0.5, "Sem dados para exibir", ha='center', va='center')
st.pyplot(fig3)
plt.close()

# Tabela e download
st.subheader("Dados Detalhados")

if st.checkbox("Mostrar tabela de dados"):
    st.dataframe(df_filtrado)

# Botão de download
def converter_para_excel(df):
    from io import BytesIO
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Vendas')
    return output.getvalue()

if not df_filtrado.empty:
    excel_bytes = converter_para_excel(df_filtrado)
    st.download_button(
        label="📥 Baixar Dados Filtrados (Excel)",
        data=excel_bytes,
        file_name="relatorio_vendas.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
