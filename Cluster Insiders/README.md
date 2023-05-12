# Clusterização de Clientes - Projeto de Fidelização
Este repositório contém um projeto de clusterização em [Notebook Python](https://github.com/julianichagas/portfolio/blob/main/Cluster%20Insiders/Cluster%20Insiders.ipynb), desenvolvido com o objetivo de identificar os clientes mais valiosos para um programa de fidelização em um e-commerce. O projeto utiliza técnicas de análise de dados e aprendizado de máquina para separar os clientes de acordo com seu perfil de compra.

## Objetivo
O objetivo deste projeto é identificar os clientes mais valiosos para um programa de fidelização em um e-commerce. Através da clusterização dos clientes com base em seu perfil de compra, busca-se encontrar um grupo de clientes que apresentem maior potencial de geração de receita para o negócio. Esses clientes serão convidados a participar do programa "Insiders", que oferece benefícios exclusivos e visa aumentar sua lealdade à marca.

## Dados
Os dados utilizados neste projeto foram obtidos a partir de um arquivo CSV contendo informações sobre compras realizadas no e-commerce durante um período de um ano. O arquivo foi pré-processado, incluindo a limpeza e tratamento dos dados, bem como a realização de feature engineering para extrair informações relevantes dos registros.

## Técnica de Avaliação
A técnica utilizada para avaliar a qualidade da clusterização realizada foi a análise de silhueta. Essa métrica avalia a coesão e a separação dos clusters formados, fornecendo uma medida de quão bem os pontos se encaixam em seus respectivos clusters. A média do Silhouette Score foi de 68%.

## Pré-processamento dos Dados
Antes de realizar a clusterização, foi necessário realizar um pré-processamento dos dados. Esse processo incluiu a limpeza e tratamento dos dados, como remoção de valores ausentes e tratamento de outliers. Além disso, foram aplicadas técnicas de feature engineering para criar novas variáveis que capturam informações relevantes sobre o perfil de compra de cada cliente.

## Clusterização
A clusterização dos clientes foi realizada utilizando o algoritmo K-means. Para isso, foi utilizado o espaço de embedding gerado pela posição das folhas de uma árvore de decisão treinada para prever a receita dos usuários. Esse espaço de embedding representa uma representação compacta dos dados originais, que facilita a clusterização.

O algoritmo K-means foi aplicado aos dados de embedding, dividindo os clientes em 9 clusters distintos. Cada cluster representa um grupo de clientes com características de compra semelhantes. A partir dessa clusterização, identificamos o cluster com a maior receita, que corresponde aos clientes que farão parte do programa "Insiders".

## Resultados
Os resultados da clusterização mostraram que o cluster com a maior receita é composto pelos clientes que farão parte do programa "Insiders". Esses clientes representam quase metade da receita e do volume de compras do e-commerce. Seu ticket médio é mais de 500 vezes maior do que os demais clusters. Esses resultados indicam que esses clientes possuem um alto potencial de geração de receita e são de extrema importância para o sucesso do negócio.
