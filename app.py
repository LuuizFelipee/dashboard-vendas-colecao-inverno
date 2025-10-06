from cProfile import label
from re import I
import pandas as pd 
import plotly.express as px
import streamlit as st

df = pd.read_csv('dataframe-vendas.csv')

st.set_page_config(
    page_title='Análise de Vendas da Coleção Inverno',
    page_icon='',
    layout="wide"
)

#barra lateral 
st.sidebar.header("Filtros")

#Filtro do produto
produtos_disponiveis = sorted(df["produto"].unique())
produtos_selecionados = st.sidebar.multiselect("Produtos", produtos_disponiveis)

#Filtro do Modelo
modelos_disponiveis = sorted(df["modelo"].unique())
modelos_selecionados = st.sidebar.multiselect("Modelos", modelos_disponiveis, default= modelos_disponiveis)


#Filtro do Tipo de Pafamento
pagamento_disponiveis = sorted(df["tipo de pagamento"].unique())
pagamento_selecionados = st.sidebar.multiselect("Tipos de pagamento", pagamento_disponiveis, default= pagamento_disponiveis)

#criando um dataframe a partir dos filtros para eles mudarem em tempo real
df_filtrado = df[
    (df['produto'].isin(produtos_selecionados)) &
    (df['modelo'].isin(modelos_selecionados)) &
    (df['tipo de pagamento'].isin(pagamento_selecionados))
]

#Conteudo Principal
st.title("Dashboard de vendas da coleção de inverno")
st.markdown("Dashboard interativo para analisar as vendas dos produtos da coleção núvens de 2025")

#Métricas principais
st.subheader("Métricas gerais")

if not df_filtrado.empty:
    total_vendas = df_filtrado['valor produto'].sum()
    tipo_mais_utilizado = df_filtrado['tipo de pagamento'].mode()[0]
    produto_mais_vendido = df_filtrado['produto'].mode()[0]
    quantidade_de_produtos = df_filtrado.shape[0]
else: 
    total_vendas, tipo_mais_utilizado, produto_mais_vendido, quantidade_de_produtos = 0, "", "", 0

col1 ,col2, col3, col4 = st.columns(4)
col1.metric("Arrecadação das vendas", f"${total_vendas:,.0f}")  
col2.metric("Método de pagamento mais utilizado", tipo_mais_utilizado)  
col3.metric("Produto mais vendido", produto_mais_vendido)
col4.metric("Quantidade de Vendas", quantidade_de_produtos)

st.markdown("---")

#Gráficos
col_graf1, col_graf2= st.columns(2)


if (len(produtos_selecionados) > 1): 

    with col_graf1:
        if not df_filtrado.empty:
            mais_vendidos = df_filtrado.groupby('produto')['valor produto'].sum().sort_values(ascending=True).reset_index()
            grafico_vendidos = px.bar(
                mais_vendidos,
                x='valor produto',
                y='produto',
                title="Arrecadação dos produtos",
                labels={'valor produto': 'Arrecadação', 'produto': ''},
                color='produto'
            )
            grafico_vendidos.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(grafico_vendidos, use_container_width=True)
        else: 
            st.warning("Nenhum dado para exibir no gráfico de distribuição.")

    with col_graf2:     
        if not df_filtrado.empty: 
            grafico_quantidade = px.histogram(
                df_filtrado,
                x='produto',
                nbins= 30,
                title= 'Quantidade de venda dos produtos',
                labels={'produto': 'Produtos', 'count': ''},
                color='produto'
            )
            st.plotly_chart(grafico_quantidade,use_container_width=True)
        else:
            st.warning("Nenhum dado para exibir no gráfico de distribuição.")

    with col_graf2:
        if not df_filtrado.empty:
            sem_duplicata = df_filtrado.drop_duplicates(subset='cpf')
            grafico_socio = px.histogram(
                sem_duplicata,
                x= 'compra sócio',
                nbins= 20,
                title= 'Relação entre sócios ou não',
                labels= {'compra sócio':'Sócios', 'count':''}
            )
            st.plotly_chart(grafico_socio, use_container_width= True, key = 'grafico1')
        else:
            st.warning("Nenhum dado para exibir no gráfico de distribuição.")



with col_graf1:
    if not df_filtrado.empty:
        pagamentos = df_filtrado['tipo de pagamento'].value_counts().reset_index()
        tipo_de_pagamento = px.pie(
            pagamentos, 
            names='tipo de pagamento',
            values= 'count',
            title= 'Proporção na forma de pagamento',
            hole = 0.5,
            labels={'Dinheiro': 'Débito'}
        )
        tipo_de_pagamento.update_traces(textinfo='percent+label')
        tipo_de_pagamento.update_layout(title_x=0.1)
        st.plotly_chart(tipo_de_pagamento, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")



if (len(produtos_selecionados) <= 1):

    with col_graf2:
        if not df_filtrado.empty:
            grafico_tamanho = px.histogram(
                df_filtrado,
                x='modelo',
                nbins= 30,
                title= 'Quantidade de vendas por tamanho',
                labels = {'modelo': 'Modelos', 'count':''}
            )
            st.plotly_chart(grafico_tamanho, use_container_width= True)
        else:
            st.warning("Nenhum dado para exibir no gráfico de distribuição.")

    if not df_filtrado.empty:
        sem_duplicata = df_filtrado.drop_duplicates(subset='cpf')
        grafico_socio = px.histogram(
            sem_duplicata,
            x= 'compra sócio',
            nbins= 20,
            title= 'Relação entre sócios ou não',
            labels= {'compra sócio':'Sócios', 'count':''}
        )
        st.plotly_chart(grafico_socio, use_container_width= True, key = 'grafico1')
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")
#dados detalhados 
st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)
