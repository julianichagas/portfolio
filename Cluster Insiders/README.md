# Clusterização de Clientes - Projeto de Fidelização
Este repositório contém um projeto de clusterização em [Notebook Python](https://github.com/julianichagas/portfolio/blob/main/Cluster%20Insiders/Cluster%20Insiders.ipynb), desenvolvido com o objetivo de identificar os clientes mais valiosos para um programa de fidelização em um e-commerce. O projeto utiliza técnicas de análise de dados e aprendizado de máquina para separar os clientes de acordo com seu perfil de compra.

## Objetivo
O objetivo deste projeto é identificar os clientes mais valiosos para um programa de fidelização em um e-commerce. Através da clusterização dos clientes com base em seu perfil de compra, busca-se encontrar um grupo de clientes que apresentem maior potencial de geração de receita para o negócio. Esses clientes serão convidados a participar do programa "Insiders", que oferece benefícios exclusivos e visa aumentar sua lealdade à marca.

## Dados
Os dados utilizados neste projeto foram obtidos a partir de um arquivo CSV contendo informações sobre compras realizadas no e-commerce durante um período de um ano. O arquivo foi pré-processado, incluindo a limpeza e tratamento dos dados, bem como a realização de feature engineering para extrair informações relevantes dos registros.

### Amostra dos dados carregados:
<table class="dataframe" border="1">
  <thead>
    <tr style="text-align: right;">
      <th>invoice_no</th>
      <th>stock_code</th>
      <th>description</th>
      <th>quantity</th>
      <th>invoice_date</th>
      <th>unit_price</th>
      <th>country</th>
      <th>customer_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>536365</td>
      <td>85123A</td>
      <td>WHITE HANGING HEART T-LIGHT HOLDER</td>
      <td>6</td>
      <td>29-Nov-16</td>
      <td>2.55</td>
      <td>United Kingdom</td>
      <td>17850.00</td>
    </tr>
    <tr>
      <td>536365</td>
      <td>71053</td>
      <td>WHITE METAL LANTERN</td>
      <td>6</td>
      <td>29-Nov-16</td>
      <td>3.39</td>
      <td>United Kingdom</td>
      <td>17850.00</td>
    </tr>
    <tr>
      <td>536365</td>
      <td>84406B</td>
      <td>CREAM CUPID HEARTS COAT HANGER</td>
      <td>8</td>
      <td>29-Nov-16</td>
      <td>2.75</td>
      <td>United Kingdom</td>
      <td>17850.00</td>
    </tr>
  </tbody>
</table>

### Amostra após tratamento dos dados e Feature Engineering:
<table class="dataframe" border="1">
  <thead>
    <tr style="text-align: right;">
      <th>customer_id</th>
      <th>gross_revenue</th>
      <th>recency_days</th>
      <th>qty_invoices</th>
      <th>qty_products</th>
      <th>qty_items</th>
      <th>frequency</th>
      <th>qty_returns</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>14504</td>
      <td>673.26</td>
      <td>47.00</td>
      <td>4.00</td>
      <td>85.00</td>
      <td>308.00</td>
      <td>0.02</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>16686</td>
      <td>3062.83</td>
      <td>47.00</td>
      <td>7.00</td>
      <td>406.00</td>
      <td>2030.00</td>
      <td>0.02</td>
      <td>5.00</td>
    </tr>
    <tr>
      <td>22004</td>
      <td>20.53</td>
      <td>58.00</td>
      <td>1.00</td>
      <td>5.00</td>
      <td>35.00</td>
      <td>1.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>14636</td>
      <td>609.85</td>
      <td>36.00</td>
      <td>2.00</td>
      <td>27.00</td>
      <td>241.00</td>
      <td>0.01</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>19659</td>
      <td>8.50</td>
      <td>298.00</td>
      <td>1.00</td>
      <td>1.00</td>
      <td>1.00</td>
      <td>1.00</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>

## Técnica de Avaliação
A técnica utilizada para avaliar a qualidade da clusterização realizada foi a análise de silhueta. Essa métrica avalia a coesão e a separação dos clusters formados, fornecendo uma medida de quão bem os pontos se encaixam em seus respectivos clusters. A média do Silhouette Score foi de 68%.

## Pré-processamento dos Dados
Antes de realizar a clusterização, foi necessário realizar um pré-processamento dos dados. Esse processo incluiu a limpeza e tratamento dos dados, como remoção de valores ausentes e tratamento de outliers. Além disso, foram aplicadas técnicas de feature engineering para criar novas variáveis que capturam informações relevantes sobre o perfil de compra de cada cliente.

## Clusterização
A clusterização dos clientes foi realizada utilizando o algoritmo K-means. Para isso, foi utilizado o espaço de embedding gerado pela posição das folhas de uma árvore de decisão treinada para prever a receita dos usuários. Esse espaço de embedding representa uma representação compacta dos dados originais, que facilita a clusterização.

O algoritmo K-means foi aplicado aos dados de embedding, dividindo os clientes em 9 clusters distintos. Cada cluster representa um grupo de clientes com características de compra semelhantes. A partir dessa clusterização, identificamos o cluster com a maior receita, que corresponde aos clientes que farão parte do programa "Insiders".

## Resultados
Os resultados da clusterização mostraram que o cluster com a maior receita é composto pelos clientes que farão parte do programa "Insiders". Esses clientes representam quase metade da receita e do volume de compras do e-commerce. Seu ticket médio é mais de 500 vezes maior do que os demais clusters. Esses resultados indicam que esses clientes possuem um alto potencial de geração de receita e são de extrema importância para o sucesso do negócio.

<table class="dataframe" border="1">
  <thead>
    <tr style="text-align: right;">
      <th>cluster</th>
      <th>customer_id</th>
      <th>perc_customer</th>
      <th>gross_revenue</th>
      <th>recency_days</th>
      <th>qty_products</th>
      <th>frequency</th>
      <th>qty_returns</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Insiders</td>
      <td>600</td>
      <td>10.54</td>
      <td>7736.39</td>
      <td>59.31</td>
      <td>253.34</td>
      <td>0.26</td>
      <td>254.02</td>
    </tr>
    <tr>
      <td>Leais</td>
      <td>384</td>
      <td>6.74</td>
      <td>2336.05</td>
      <td>57.63</td>
      <td>69.10</td>
      <td>0.04</td>
      <td>45.11</td>
    </tr>
    <tr>
      <td>Potenciais</td>
      <td>390</td>
      <td>6.85</td>
      <td>2083.69</td>
      <td>158.94</td>
      <td>66.53</td>
      <td>1.06</td>
      <td>1.29</td>
    </tr>
    <tr>
      <td>Novos</td>
      <td>741</td>
      <td>13.01</td>
      <td>2081.56</td>
      <td>102.42</td>
      <td>152.82</td>
      <td>0.47</td>
      <td>0.31</td>
    </tr>
    <tr>
      <td>Acompanhar</td>
      <td>1440</td>
      <td>25.29</td>
      <td>1167.69</td>
      <td>69.22</td>
      <td>33.45</td>
      <td>0.03</td>
      <td>3.11</td>
    </tr>
    <tr>
      <td>Promissor</td>
      <td>675</td>
      <td>11.85</td>
      <td>394.87</td>
      <td>186.01</td>
      <td>28.71</td>
      <td>1.01</td>
      <td>1.88</td>
    </tr>
    <tr>
      <td>Prestes a perder</td>
      <td>539</td>
      <td>9.46</td>
      <td>284.69</td>
      <td>136.00</td>
      <td>14.50</td>
      <td>0.99</td>
      <td>2.83</td>
    </tr>
    <tr>
      <td>Perdendo</td>
      <td>359</td>
      <td>6.30</td>
      <td>160.42</td>
      <td>178.43</td>
      <td>6.96</td>
      <td>1.00</td>
      <td>0.76</td>
    </tr>
    <tr>
      <td>Hibernando</td>
      <td>567</td>
      <td>9.96</td>
      <td>90.49</td>
      <td>189.96</td>
      <td>1.99</td>
      <td>1.00</td>
      <td>0.13</td>
    </tr>
  </tbody>
</table>

### Receita por cluster:
<img src="https://github.com/julianichagas/portfolio/blob/main/Cluster%20Insiders/gross%20revenue.png">
