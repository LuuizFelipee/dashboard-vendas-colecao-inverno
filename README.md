# Dashboard de Vendas da Coleção de Inverno

Esse foi meu primeiro dashboard de uso real, desenvolvido para o projeto de extensão **Atlética UFSCar**, com o intuito de apresentar de forma visual alguns resultados das vendas da coleção.

## Tecnologias Utilizadas

- **Pandas** → Tratamento e análise exploratória dos dados  
- **Plotly** → Criação dos gráficos interativos  
- **Streamlit** → Montagem do dashboard e deploy da aplicação  

🔗 **Acesse o Dashboard:**  
[https://dashboard-vendas-colecao-inverno.streamlit.app](https://dashboard-vendas-colecao-inverno.streamlit.app)

---

## Funcionamento

Inicialmente, o filtro de produtos estará vazio.  
Selecione algum item para visualizar uma análise mais específica, incluindo:

- Gráfico de histograma sobre a relação de vendas por tamanho  
- Gráfico de pizza sobre o tipo de pagamento  
- Gráfico de histograma sobre clientes que são sócios (membros da atlética ou atletas) e os que não são  

Ao selecionar **mais de um produto**, o gráfico sobre a relação de tamanhos desaparecerá e serão exibidos os seguintes gráficos:

- Gráfico de barras mostrando quanto cada produto selecionado arrecadou
- Gráfico de histograma com a quantidade vendida de cada produto selecionado  

---

## Observações

- Este projeto foi uma excelente oportunidade para aplicar conhecimentos de **análise de dados**, **visualização interativa** e **desenvolvimento com Streamlit**, unindo teoria e prática em um contexto real.
- Os registros do dataframe utilizado nesse dashboard foram alterados para não divulgar nomes e CPF dos clientes e omitir dados pessoais da instituição
